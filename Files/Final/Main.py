#Modules
import os
import re
import webbrowser
from datetime import datetime
import pyowm
import sys
import time
from PyDictionary import PyDictionary
import random
import math
import psutil
from plyer import notification
import calendar
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import translate
import pyaudio
import struct
import wave
import sounddevice as sd
from scipy.io.wavfile import write
language = 'en'

print('Welcome!\nWhich mode do you want to choose?')

#Changing the mode
option = input('Text or voice:')
if option == 'voice':
    os.system('cls')
    import Voice
else:
    os.system('cls')
    import Cynthia
