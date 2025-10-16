# Script de diagnostic pour caméra Wolfgang
# Ce script vérifie les périphériques de capture vidéo installés sur le système

Write-Host "=== DIAGNOSTIC CAMERA WOLFGANG ===" -ForegroundColor Cyan
Write-Host ""

# 1. Vérifier les périphériques de capture vidéo via WMI
Write-Host "1. Périphériques de capture vidéo (WMI):" -ForegroundColor Yellow
try {
    $videoDevices = Get-WmiObject -Class Win32_PnPEntity | Where-Object { $_.Name -like "*camera*" -or $_.Name -like "*webcam*" -or $_.Name -like "*video*" -or $_.Name -like "*wolfgang*" -or $_.Name -like "*wolfang*" }
    
    if ($videoDevices) {
        foreach ($device in $videoDevices) {
            Write-Host "  - $($device.Name) [ID: $($device.DeviceID)]" -ForegroundColor Green
            Write-Host "    État: $($device.Status)" -ForegroundColor Gray
        }
    } else {
        Write-Host "  Aucun périphérique de capture vidéo trouvé via WMI" -ForegroundColor Red
    }
} catch {
    Write-Host "  Erreur lors de la vérification WMI: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# 2. Vérifier via le gestionnaire de périphériques (DevCon alternative)
Write-Host "2. Tous les périphériques USB connectés:" -ForegroundColor Yellow
try {
    $usbDevices = Get-WmiObject -Class Win32_PnPEntity | Where-Object { $_.DeviceID -like "USB*" -and $_.Name -notlike "*Root Hub*" -and $_.Name -notlike "*Composite*" }
    
    $wolfangFound = $false
    foreach ($device in $usbDevices) {
        if ($device.Name -like "*wolfgang*" -or $device.Name -like "*wolfang*" -or $device.Name -like "*camera*") {
            Write-Host "  🎥 $($device.Name)" -ForegroundColor Green
            Write-Host "     ID: $($device.DeviceID)" -ForegroundColor Gray
            Write-Host "     État: $($device.Status)" -ForegroundColor Gray
            $wolfangFound = $true
        }
    }
    
    if (-not $wolfangFound) {
        Write-Host "  ⚠️ Aucun périphérique Wolfgang/caméra détecté dans les USB" -ForegroundColor Orange
        Write-Host "  Périphériques USB détectés:" -ForegroundColor Gray
        foreach ($device in $usbDevices) {
            Write-Host "    - $($device.Name)" -ForegroundColor Gray
        }
    }
} catch {
    Write-Host "  Erreur lors de la vérification USB: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# 3. Vérifier les pilotes de caméra
Write-Host "3. Pilotes d'imagerie installés:" -ForegroundColor Yellow
try {
    $imagingDevices = Get-WmiObject -Class Win32_SystemDriver | Where-Object { $_.Name -like "*camera*" -or $_.Name -like "*video*" -or $_.Name -like "*imaging*" -or $_.Name -like "*uvc*" }
    
    if ($imagingDevices) {
        foreach ($driver in $imagingDevices) {
            Write-Host "  - $($driver.Name): $($driver.State)" -ForegroundColor Green
        }
    } else {
        Write-Host "  Aucun pilote d'imagerie spécifique trouvé" -ForegroundColor Orange
    }
} catch {
    Write-Host "  Erreur lors de la vérification des pilotes: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# 4. Vérifier les services liés à la caméra
Write-Host "4. Services de caméra Windows:" -ForegroundColor Yellow
$cameraServices = @("FrameServer", "CameraService", "Windows Camera Frame Server")
foreach ($serviceName in $cameraServices) {
    try {
        $service = Get-Service -Name $serviceName -ErrorAction SilentlyContinue
        if ($service) {
            $statusColor = if ($service.Status -eq "Running") { "Green" } else { "Orange" }
            Write-Host "  - $($service.Name): $($service.Status)" -ForegroundColor $statusColor
        }
    } catch {
        # Service non trouvé, ignorer
    }
}

Write-Host ""

# 5. Vérifier les applications qui peuvent utiliser la caméra
Write-Host "5. Processus utilisant potentiellement la caméra:" -ForegroundColor Yellow
try {
    $processes = Get-Process | Where-Object { $_.ProcessName -like "*camera*" -or $_.ProcessName -like "*video*" -or $_.ProcessName -like "*obs*" -or $_.ProcessName -like "*zoom*" -or $_.ProcessName -like "*teams*" -or $_.ProcessName -like "*skype*" }
    
    if ($processes) {
        foreach ($proc in $processes) {
            Write-Host "  - $($proc.ProcessName) (PID: $($proc.Id))" -ForegroundColor Orange
        }
        Write-Host "  ⚠️ Ces processus peuvent monopoliser la caméra" -ForegroundColor Orange
    } else {
        Write-Host "  ✅ Aucun processus connu utilisant la caméra détecté" -ForegroundColor Green
    }
} catch {
    Write-Host "  Erreur lors de la vérification des processus: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# 6. Informations système
Write-Host "6. Informations système:" -ForegroundColor Yellow
Write-Host "  - OS: $(Get-WmiObject -Class Win32_OperatingSystem | Select-Object -ExpandProperty Caption)" -ForegroundColor Gray
Write-Host "  - Version: $(Get-WmiObject -Class Win32_OperatingSystem | Select-Object -ExpandProperty Version)" -ForegroundColor Gray
Write-Host "  - Architecture: $($env:PROCESSOR_ARCHITECTURE)" -ForegroundColor Gray

Write-Host ""

# 7. Suggestions de dépannage
Write-Host "=== SUGGESTIONS DE DÉPANNAGE ===" -ForegroundColor Cyan
Write-Host "1. Vérifiez que Wolfgang est bien allumé et en mode webcam" -ForegroundColor White
Write-Host "2. Essayez de débrancher/rebrancher le câble USB" -ForegroundColor White
Write-Host "3. Testez sur un autre port USB (de préférence USB 3.0)" -ForegroundColor White
Write-Host "4. Vérifiez dans le Gestionnaire de périphériques (devmgmt.msc)" -ForegroundColor White
Write-Host "5. Essayez de redémarrer le service Windows Camera Frame Server:" -ForegroundColor White
Write-Host "   Get-Service FrameServer | Restart-Service" -ForegroundColor Gray
Write-Host "6. Fermer toutes les applications utilisant potentiellement la caméra" -ForegroundColor White
Write-Host ""
Write-Host "Pour tester dans un navigateur, lancez: npm start" -ForegroundColor Green

# Fin du script
Write-Host ""
Write-Host "Diagnostic terminé. Appuyez sur une touche pour continuer..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")