import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from getpass import getpass
from gtts import gTTS
from playsound import playsound
import time
audio='example.mp3'
lang='en'
clip=gTTS(text="HEY HEMANT I AM YOU personal ASSISTANT ",Lang=lang,slow=False)
clip.save()
playsound(audio)
time.sleep(5)
print("hey you are now successful")