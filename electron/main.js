const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');
const fs = require('fs').promises;
const fsSync = require('fs');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadURL(
    isDev
      ? 'http://localhost:3000'
      : `file://${path.join(__dirname, '../build/index.html')}`
  );

  if (isDev) {
    mainWindow.webContents.openDevTools();
  }
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// Sélectionner le dossier de destination (disque dur externe)
ipcMain.handle('select-directory', async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory']
  });
  
  if (!result.canceled && result.filePaths.length > 0) {
    return result.filePaths[0];
  }
  return null;
});

// Créer un nouveau dossier dans le répertoire de destination
ipcMain.handle('create-folder', async (event, basePath, folderName) => {
  try {
    const folderPath = path.join(basePath, folderName);
    await fs.mkdir(folderPath, { recursive: true });
    return { success: true, path: folderPath };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Lister les dossiers dans le répertoire de destination
ipcMain.handle('list-folders', async (event, basePath) => {
  try {
    const items = await fs.readdir(basePath, { withFileTypes: true });
    const folders = items
      .filter(item => item.isDirectory())
      .map(item => ({
        name: item.name,
        path: path.join(basePath, item.name)
      }));
    return { success: true, folders };
  } catch (error) {
    return { success: false, error: error.message, folders: [] };
  }
});

// Lister les vidéos dans un dossier
ipcMain.handle('list-videos', async (event, folderPath) => {
  try {
    const items = await fs.readdir(folderPath);
    const videos = [];
    
    for (const item of items) {
      const fullPath = path.join(folderPath, item);
      const ext = path.extname(item).toLowerCase();
      
      if (['.mp4', '.webm', '.mkv', '.avi', '.mov'].includes(ext)) {
        const stats = await fs.stat(fullPath);
        videos.push({
          name: item,
          path: fullPath,
          size: stats.size,
          created: stats.birthtime,
          modified: stats.mtime
        });
      }
    }
    
    return { success: true, videos };
  } catch (error) {
    return { success: false, error: error.message, videos: [] };
  }
});

// Supprimer une vidéo
ipcMain.handle('delete-video', async (event, videoPath) => {
  try {
    await fs.unlink(videoPath);
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Sauvegarder un chunk de vidéo
ipcMain.handle('save-video-chunk', async (event, folderPath, fileName, dataURL) => {
  try {
    // Convertir le data URL en buffer
    const base64Data = dataURL.split(',')[1];
    const buffer = Buffer.from(base64Data, 'base64');
    
    const filePath = path.join(folderPath, fileName);
    
    // Si le fichier existe, on ajoute les données (pour les chunks)
    if (fsSync.existsSync(filePath)) {
      await fs.appendFile(filePath, buffer);
    } else {
      await fs.writeFile(filePath, buffer);
    }
    
    return { success: true, path: filePath };
  } catch (error) {
    return { success: false, error: error.message };
  }
});

// Sauvegarder la vidéo complète
ipcMain.handle('save-video', async (event, folderPath, fileName, blob) => {
  try {
    const filePath = path.join(folderPath, fileName);
    await fs.writeFile(filePath, Buffer.from(blob));
    return { success: true, path: filePath };
  } catch (error) {
    return { success: false, error: error.message };
  }
});
