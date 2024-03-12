@echo off

set MAKER=pyinstaller
set SOURCE=generator.py
set ICON=-i logo.png
set FLAGS=-F -w

%MAKER% %FLAGS% %ICON% %SOURCE%
