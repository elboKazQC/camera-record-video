@echo off
title Test Wolfgang GA100 - Diagnostic Rapide
color 0A

echo.
echo ****************************************
echo *      TEST WOLFGANG GA100 WEBCAM     *
echo ****************************************
echo.

echo [ETAPE 1] Verification des peripheriques USB...
echo.
echo Peripheriques USB detectes:
wmic path Win32_PnPEntity where "DeviceID like 'USB%%' AND (Name like '%%camera%%' OR Name like '%%wolfgang%%' OR Name like '%%video%%' OR Name like '%%UVC%%')" get Name,DeviceID 2>nul

echo.
echo [ETAPE 2] Verification service Camera Windows...
sc query FrameServer | findstr "STATE"
if errorlevel 1 (
    echo Service FrameServer: ERREUR
    echo Tentative de demarrage...
    sc start FrameServer >nul 2>&1
) else (
    echo Service FrameServer: OK
)

echo.
echo [ETAPE 3] Test application Camera Windows...
echo Ouverture de l'application Camera...
start ms-camera:
timeout /t 3 >nul

echo.
echo [ETAPE 4] Ouverture du Gestionnaire de peripheriques...
echo Verification manuelle dans le Gestionnaire...
start devmgmt.msc

echo.
echo ========================================
echo           INSTRUCTIONS WOLFGANG GA100
echo ========================================
echo.
echo 1. Sur votre Wolfgang GA100:
echo    - Appuyez sur MENU
echo    - Allez dans Parametres / Settings
echo    - Trouvez "USB Mode"
echo    - Selectionnez "PC Camera" ou "UVC Mode"
echo.
echo 2. Verifiez dans le Gestionnaire de peripheriques:
echo    - Section "Cameras" 
echo    - Ou "Peripheriques d'imagerie"
echo    - Cherchez "Wolfgang" ou "USB Camera"
echo.
echo 3. Si probleme:
echo    - Deconnectez/reconnectez Wolfgang
echo    - Changez de port USB (USB 3.0 de preference)
echo    - Verifiez que Wolfgang n'est PAS en mode "Mass Storage"
echo.

echo Appuyez sur une touche pour ouvrir le test navigateur...
pause >nul

echo Ouverture du test dans le navigateur...
start "" "test-wolfgang-simple.html"

echo.
echo Test termine. Wolfgang est-il detecte?
pause