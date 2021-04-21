#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime

import os.path
from inotify_simple import INotify, flags
import json
import thread

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Projet_NP")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        #font.LoadFont("./rpi-rgb-led-matrix/fonts/5x8.bdf")
        font.LoadFont("/home/pi/Projet_NP/rpi-rgb-led-matrix/fonts/5x8.bdf")
        
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        global my_text
        my_text = "   "
        while True:
            global nombre
            my_text = str(nombre) + "/"
            global limite
            my_text += str(limite)
            time = str(datetime.datetime.now().strftime("%H:%M"))
            offscreen_canvas.Clear()
            # print("my_text : " + my_text)
            len = graphics.DrawText(offscreen_canvas, font,4, 7, textColor, my_text)
            len1 = graphics.DrawText(offscreen_canvas, font,4, 15, textColor, time)
            #time.sleep(0.05)
            
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

def _readfileParam():
    try:
        text = open('/home/pi/Projet_NP/parametre_projet.json', "r")
        res = json.load(text)
        return res
    except:
        print("An exception occurred _readfileParam")
        return -1
            

def _readfile():
    try:
        text = open('/tmp/nombre.json', "r")
        res = json.load(text)
        return res
    except:
        print("An exception occurred _readfile")
        return -1

# def _createfile():
#     path = '/tmp/nombre.json'
#     try:
#         f = open(path, "w")
#         f.close()
#         
#     except:
#         print("An exception occurred _createfile")
    
def _inotify_param():
    inotify = INotify()
    watch_flags = flags.MODIFY
    wd = inotify.add_watch('/home/pi/Projet_NP/parametre_projet.json',watch_flags)
    while(True):
        print("_inotify_param : attente de modification dans le fichier")
        for event in inotify.read():
            print(event)
            for flag in flags.from_mask(event.mask):
                print("modification dans le fichier")
                print("start affichage new ")
                param = _readfileParam()
                global limite
                limite = param['limite_personne']
                print("voici les nouveaux param : " + str(param['limite_personne']))
                print("voici les nouveaux param : " + str(param))
                
def _inotify_nombre():
    inotify = INotify()
    watch_flags = flags.MODIFY
    wd = inotify.add_watch('/tmp/nombre.json',watch_flags)
    while(True):
        print("_inotify_nombre : attente de modification dans le fichier")
        for event in inotify.read():
            print(event)
            for flag in flags.from_mask(event.mask):
                print("modification dans le fichier")
                print("start affichage new nombre")
                global nombre
                nombre = _readfile()
                print("voici le nouveau nombre : " + str(nombre))
                global stop
                stop = False
                print("je passe stop " + str(stop))
                print("done")


def affichage_matrice():
    global stop    
    stop = True
    print("stop : " + str(stop))
    while(stop):
        run_text = RunText()
        if (not run_text.process()):
            run_text.print_help()

# Main function
if __name__ == "__main__":
#      _createfile()
     global nombre
     nombre = ""
     param = _readfileParam()
     global limite
     limite = param['limite_personne']
     thread.start_new_thread(_inotify_nombre,())
     thread.start_new_thread(_inotify_param,())
     while(True):
         affichage_matrice()
         print("hey !! ---main----")
