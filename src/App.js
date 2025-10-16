import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [devices, setDevices] = useState([]);
  const [selectedDevice, setSelectedDevice] = useState(null);
  const [stream, setStream] = useState(null);
  const [error, setError] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [recordedChunks, setRecordedChunks] = useState([]);
  
  const videoRef = useRef(null);

  // Fonction pour lister tous les périphériques médias
  const enumerateDevices = async () => {
    try {
      // Demander d'abord les permissions
      await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      
      const devices = await navigator.mediaDevices.enumerateDevices();
      const videoDevices = devices.filter(device => device.kind === 'videoinput');
      
      console.log('Tous les périphériques détectés:', devices);
      console.log('Périphériques vidéo:', videoDevices);
      
      setDevices(videoDevices);
      setError(null);
      
      // Rechercher spécifiquement Wolfgang
      const wolfangDevice = videoDevices.find(device => 
        device.label.toLowerCase().includes('wolfgang') ||
        device.label.toLowerCase().includes('wolfang')
      );
      
      if (wolfangDevice) {
        console.log('Wolfgang détecté:', wolfangDevice);
      } else {
        console.log('Wolfgang non trouvé dans les périphériques');
      }
      
    } catch (err) {
      console.error('Erreur lors de l\'énumération des périphériques:', err);
      setError(`Erreur: ${err.message}`);
    }
  };

  // Fonction pour démarrer la caméra
  const startCamera = async (deviceId) => {
    try {
      // Arrêter le stream existant s'il y en a un
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }

      const constraints = {
        video: {
          deviceId: deviceId ? { exact: deviceId } : undefined,
          width: { ideal: 1920 },
          height: { ideal: 1080 }
        },
        audio: true
      };

      console.log('Tentative de démarrage avec les contraintes:', constraints);
      
      const newStream = await navigator.mediaDevices.getUserMedia(constraints);
      setStream(newStream);
      setError(null);
      
      if (videoRef.current) {
        videoRef.current.srcObject = newStream;
      }
      
      console.log('Caméra démarrée avec succès');
      
    } catch (err) {
      console.error('Erreur lors du démarrage de la caméra:', err);
      setError(`Erreur caméra: ${err.message}`);
    }
  };

  // Fonction pour démarrer l'enregistrement
  const startRecording = () => {
    if (stream) {
      try {
        const recorder = new MediaRecorder(stream);
        const chunks = [];
        
        recorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            chunks.push(event.data);
          }
        };
        
        recorder.onstop = () => {
          const blob = new Blob(chunks, { type: 'video/webm' });
          const url = URL.createObjectURL(blob);
          
          // Créer un lien de téléchargement
          const a = document.createElement('a');
          a.style.display = 'none';
          a.href = url;
          a.download = `wolfgang-video-${Date.now()}.webm`;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
        };
        
        setRecordedChunks(chunks);
        setMediaRecorder(recorder);
        recorder.start();
        setIsRecording(true);
        
      } catch (err) {
        console.error('Erreur lors du démarrage de l\'enregistrement:', err);
        setError(`Erreur enregistrement: ${err.message}`);
      }
    }
  };

  // Fonction pour arrêter l'enregistrement
  const stopRecording = () => {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
      mediaRecorder.stop();
      setIsRecording(false);
    }
  };

  // Fonction pour tester les capacités de la caméra
  const testCameraCapabilities = async (deviceId) => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { deviceId: { exact: deviceId } }
      });
      
      const track = stream.getVideoTracks()[0];
      const capabilities = track.getCapabilities();
      const settings = track.getSettings();
      
      console.log('Capacités de la caméra:', capabilities);
      console.log('Paramètres actuels:', settings);
      
      // Nettoyer
      stream.getTracks().forEach(track => track.stop());
      
    } catch (err) {
      console.error('Erreur lors du test des capacités:', err);
    }
  };

  useEffect(() => {
    enumerateDevices();
    
    // Écouter les changements de périphériques
    navigator.mediaDevices.ondevicechange = () => {
      console.log('Changement de périphériques détecté');
      enumerateDevices();
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Diagnostic Caméra Wolfgang</h1>
        
        <div className="controls">
          <button onClick={enumerateDevices}>
            🔄 Actualiser les périphériques
          </button>
        </div>

        {error && (
          <div className="error">
            <strong>❌ Erreur:</strong> {error}
          </div>
        )}

        <div className="devices-section">
          <h2>Périphériques vidéo détectés ({devices.length})</h2>
          {devices.length === 0 ? (
            <p>Aucun périphérique vidéo détecté</p>
          ) : (
            <div className="devices-list">
              {devices.map((device, index) => (
                <div key={device.deviceId} className="device-item">
                  <div className="device-info">
                    <strong>#{index + 1}:</strong> {device.label || `Caméra ${index + 1}`}
                    <br />
                    <small>ID: {device.deviceId}</small>
                  </div>
                  <div className="device-actions">
                    <button 
                      onClick={() => {
                        setSelectedDevice(device);
                        startCamera(device.deviceId);
                      }}
                      className={selectedDevice?.deviceId === device.deviceId ? 'active' : ''}
                    >
                      📹 Tester
                    </button>
                    <button onClick={() => testCameraCapabilities(device.deviceId)}>
                      🔍 Capacités
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {selectedDevice && (
          <div className="camera-section">
            <h2>Caméra sélectionnée: {selectedDevice.label || 'Sans nom'}</h2>
            
            <div className="video-container">
              <video 
                ref={videoRef} 
                autoPlay 
                playsInline 
                muted
                className="camera-preview"
              />
            </div>
            
            <div className="recording-controls">
              {!isRecording ? (
                <button onClick={startRecording} disabled={!stream}>
                  🔴 Démarrer l'enregistrement
                </button>
              ) : (
                <button onClick={stopRecording}>
                  ⏹️ Arrêter l'enregistrement
                </button>
              )}
            </div>
          </div>
        )}

        <div className="info-section">
          <h3>Informations de diagnostic</h3>
          <div className="diagnostic-info">
            <p><strong>Navigateur:</strong> {navigator.userAgent}</p>
            <p><strong>Support MediaDevices:</strong> {navigator.mediaDevices ? '✅ Oui' : '❌ Non'}</p>
            <p><strong>Support getUserMedia:</strong> {navigator.mediaDevices?.getUserMedia ? '✅ Oui' : '❌ Non'}</p>
            <p><strong>Support enumerateDevices:</strong> {navigator.mediaDevices?.enumerateDevices ? '✅ Oui' : '❌ Non'}</p>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;