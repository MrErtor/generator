#!/usr/bin/sh

MAKER=pyinstaller
SOURCE=generator.py
ICON=-i logo.png
FLAGS=-F -w

$MAKER $FLAGS $ICON $SOURCE