const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  selectDirectory: () => ipcRenderer.invoke('select-directory'),
  createFolder: (basePath, folderName) => ipcRenderer.invoke('create-folder', basePath, folderName),
  listFolders: (basePath) => ipcRenderer.invoke('list-folders', basePath),
  listVideos: (folderPath) => ipcRenderer.invoke('list-videos', folderPath),
  deleteVideo: (videoPath) => ipcRenderer.invoke('delete-video', videoPath),
  saveVideoChunk: (folderPath, fileName, dataURL) => ipcRenderer.invoke('save-video-chunk', folderPath, fileName, dataURL),
  saveVideo: (folderPath, fileName, blob) => ipcRenderer.invoke('save-video', folderPath, fileName, blob)
});
