# NSIS-Installer für pvihk
!define ROOT_DIR ".."
!define DIST_DIR "${ROOT_DIR}\\dist"

!system 'mkdir "${DIST_DIR}" >nul 2>&1'

OutFile "${ROOT_DIR}\\dist\\pvihk_setup.exe"

### geändert: Installationsverzeichnis ins Benutzerprofil verlegen
#InstallDir "$PROGRAMFILES64\\pvihk"
InstallDir "$LOCALAPPDATA\\pvihk"

### geändert: Keine Adminrechte mehr erforderlich
#RequestExecutionLevel admin
RequestExecutionLevel user

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

  SetShellVarContext current

  # Startmenüordner anlegen
  CreateDirectory "$SMPROGRAMS\\pvihk"

  # Startmenü-Verknüpfung zur Anwendung
  CreateShortCut "$SMPROGRAMS\\pvihk\\pvihk.lnk" "$INSTDIR\\pvihk.exe" "" "$INSTDIR\\pvihk.exe" 0

  # Startmenü-Verknüpfung zum Deinstallieren
  CreateShortCut "$SMPROGRAMS\\pvihk\\Deinstallieren.lnk" "$INSTDIR\\Uninstall.exe"
SectionEnd

SectionEnd

Section "Uninstall"
  Delete "$SMPROGRAMS\\pvihk\\pvihk.lnk"
  Delete "$SMPROGRAMS\\pvihk\\Deinstallieren.lnk"
  RMDir "$SMPROGRAMS\\pvihk"

  Delete "$INSTDIR\\pvihk.exe"
  Delete "$INSTDIR\\Uninstall.exe"
  RMDir "$INSTDIR"
SectionEnd
