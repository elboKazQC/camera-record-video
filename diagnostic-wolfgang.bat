@echo off
echo =====================================
echo    DIAGNOSTIC CAMERA WOLFGANG
echo =====================================
echo.

echo Etape 1: Verification des peripheriques USB connectes
echo ----------------------------------------------------
wmic path Win32_PnPEntity where "DeviceID like 'USB%%'" get Name,DeviceID,Status /format:table
echo.

echo Etape 2: Recherche specifique de cameras/webcams
echo -----------------------------------------------
wmic path Win32_PnPEntity where "Name like '%%camera%%' OR Name like '%%webcam%%' OR Name like '%%video%%' OR Name like '%%wolfgang%%' OR Name like '%%wolfang%%'" get Name,DeviceID,Status /format:table
echo.

echo Etape 3: Verification des pilotes d'imagerie
echo ------------------------------------------
wmic path Win32_SystemDriver where "Name like '%%camera%%' OR Name like '%%video%%' OR Name like '%%imaging%%' OR Name like '%%uvc%%'" get Name,State,Status /format:table
echo.

echo Etape 4: Services Camera Windows
echo ------------------------------
sc query FrameServer 2>nul
if errorlevel 1 (
    echo Service FrameServer: Non trouve
) else (
    echo Service FrameServer: Trouve
)
echo.

echo Etape 5: Processus utilisant potentiellement la camera
echo ----------------------------------------------------
tasklist /FI "IMAGENAME eq obs*" 2>nul
tasklist /FI "IMAGENAME eq *camera*" 2>nul
tasklist /FI "IMAGENAME eq zoom*" 2>nul
tasklist /FI "IMAGENAME eq teams*" 2>nul
tasklist /FI "IMAGENAME eq skype*" 2>nul
echo.

echo SUGGESTIONS DE DEPANNAGE:
echo ========================
echo 1. Verifiez que Wolfgang est allume et en mode webcam
echo 2. Debranchement/rebranchement du cable USB
echo 3. Testez sur un autre port USB (preferablement USB 3.0)  
echo 4. Ouvrez le Gestionnaire de peripheriques (devmgmt.msc)
echo 5. Redemarrez le service Windows Camera:
echo    sc stop FrameServer ^&^& sc start FrameServer
echo 6. Testez dans le navigateur: ouvrir test-wolfgang-simple.html
echo.

echo Appuyez sur une touche pour continuer...
pause >nul