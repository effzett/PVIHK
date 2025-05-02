# NSIS-Installer für pvihk
!define ROOT_DIR ".."
!define DIST_DIR "${ROOT_DIR}\\dist"

# Erstelle dist-Verzeichnis, falls es fehlt
!system 'mkdir "${DIST_DIR}" >nul 2>&1'

OutFile "${ROOT_DIR}\\dist\\pvihk_setup.exe"
InstallDir "$PROGRAMFILES64\\pvihk"
RequestExecutionLevel admin

# Deutsche Sprache
LoadLanguageFile "${NSISDIR}\\Contrib\\Language files\\German.nlf"

Page license
Page directory
Page instfiles
UninstPage uninstConfirm
UninstPage instfiles

LicenseData "..\\LICENSE.txt"

Section "Installieren"
  SetOutPath "$INSTDIR"
  File "${DIST_DIR}\\pvihk.exe"
  WriteUninstaller "$INSTDIR\\Uninstall.exe"

  # Startmenü-Verknüpfung
  CreateShortCut "$SMPROGRAMS\\pvihk.lnk" "$INSTDIR\\pvihk.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\\pvihk.exe"
  Delete "$INSTDIR\\Uninstall.exe"
  Delete "$SMPROGRAMS\\pvihk.lnk"
  RMDir "$INSTDIR"
SectionEnd

