import os
from os.path import join,abspath,splitext,exists
import subprocess
import pyperclip
import sys

def ocr(ifname):
    if ('.png' in ifname) or ('.pdf' in ifname):
        ifname = '"'+abspath(ifname)+'"'
        ofname = ifname.replace('.png','').replace('.pdf','')
        cmd = "tesseract "+ifname+" "+ofname+ \
            " -c page_separator=" " --psm 4 -l eng txt"
        rc = subprocess.run(cmd, shell=True).returncode
        txtfname = ofname.strip('"')+'.txt'
        with open(txtfname, 'rt',
            encoding='utf-8-sig',errors='ignore') as txtfile:
            pyperclip.copy(txtfile.read())
    
def ocr_walk(folder=r'%HOMEPATH%\Pictures\Screenshots'):
    for root, dirs, filenames in os.walk(folder):
        for ifname in filenames:
            if (('.png' in ifname) or ('.pdf' in ifname)) and (not exists(splitext(ifname)[0]+'.txt')):
                ifname = '"'+abspath(join(root,ifname))+'"'
                ofname = ifname.replace('.png','').replace('.pdf','')
                cmd = 'tesseract '+ifname+' '+ofname+' -l eng hocr txt'
                rc = subprocess.run(cmd, shell=True).returncode
                os.replace(ofname.strip('"')+'.hocr',ofname.strip('"')+'.html')
                txtfname = ofname.strip('"')+'.txt'
                with open(txtfname, 'rt',errors='ignore') as txtfile:
                    pyperclip.copy(txtfile.read())

if __name__ == '__main__':
    ifname = str(sys.argv[1])
    ocr(ifname)
