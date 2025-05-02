# NSIS-Installer für pvihk
OutFile "dist\pvihk_setup.exe"
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
  File "dist\\pvihk.exe"
  WriteUninstaller "$INSTDIR\\Uninstall.exe"

  # Startmenü-Verknüpfung
  CreateShortCut "$SMPROGRAMS\\pvihk.lnk" "$INSTDIR\\pvihk.exe"
SectionEnd

Section "Deinstallieren"
  Delete "$INSTDIR\\pvihk.exe"
  Delete "$INSTDIR\\Uninstall.exe"
  Delete "$SMPROGRAMS\\pvihk.lnk"
  RMDir "$INSTDIR"
SectionEnd
