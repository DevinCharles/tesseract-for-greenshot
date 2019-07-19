# Tesseract for Greenshot

This is a simple python script that will send screenshots taken in Windows by Greenshot to Tesseract, and copy the data to the clipboard (dependency: *pyperclip*).

## Instructions

- Download and Install [Greenshot](https://getgreenshot.org/downloads/)
- Download and Install  [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Edit *tess-ocr.bat* to include your full path to *pythonw.exe*, and to *tess-ocr.py*
- Right click on greenshot icon $\to$ **Configure External Commands**
- **New**:
  - **Name**: `Tesseract OCR` 
  - **Command**: `full\path\to\tess-ocr.bat file`
- Leave ""arguements"" as is: `("{0}")`
- Right click on greenshot icon $\to$ Preferences
  - **Destination**: `Tesseract OCR`
  - **Destination**: `Save Directly`
    *(Optional, this will give you a .txt file of the same name in the same location as the .png)*

This will copy the OCR generated text to the clipboard and save a .txt file
