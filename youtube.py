# input the dependancies to use yt-dlp and ffmpeg
# yt-dlp: https://github.com/yt-dlp/yt-dlp
# ffmpeg: https://www.ffmpeg.org/download.html
# #
# import the libraries
import yt_dlp
import os
import sys
import time
import subprocess
import shutil
import argparse
import datetime
import numpy as np
import matplotlib.pyplot as plt

# rewrite this cmd command in python "yt-dlp --get-url "link""
# to get the url of the video
#
link = input("Enter the link: ")
cmd = "yt-dlp --get-url "+ link

try:
    # a, b = s  ubprocess.call(cmd, shell=True)
    a = []
    a = subprocess.call(cmd, shell=True)
    output = subprocess.check_output(cmd, shell=True)
    success = True 
except:
    print("Error: unable to get links")
    sys.exit(1)
    success = True

# separate the output string at \n and write to a, b
# a = output.split('\n')
# convert output from byte object to string
temp = output.decode('utf-8')

# get the first value in the temp string
a = temp.split('\n')[0]
b = temp.split('\n')[1]

# name the two args to video_link and audio_link in different variables
# get the datatype of a
print(type(a))
video_link = a
audio_link = b


# Use ffmpeg to download media from google servers Remember to download audio and video separately using this format "ffmpeg -ss 01:45:43 -to 01:50:16 -i linkv ni_neema.mp4"

# prompt user for start time and stop time and the file name and store in variables
start_time = input("Enter the start time in HH:MM:SS format: ")
stop_time = input("Enter the stop time in HH:MM:SS format: ")

# prompt user for the file name and store in variable
file_name = input("Enter the file name: ")

# rewrite code for this cmd format "ffmpeg -ss start_time -to stop_time -i audio_link file_name.mp4"
# to download the audio and video separately
cmd = "ffmpeg -ss " + start_time + " -to " + stop_time + " -i " + audio_link + " " + file_name + ".mp4"

try:
    subprocess.call(cmd, shell=True)
except:
    print("Error: unable to create audio")
    sys.exit(1)

# to download the video from the start time to the stop time and store in the file name
cmd = "ffmpeg -ss " + start_time + " -to " + stop_time + " -i " + video_link + " " + file_name + ".mp4"

try:
    subprocess.call(cmd, shell=True)
except:
    print("Error: unable to download video")
    sys.exit(1)

# Combine Audio And Video File Without Re-encoding in python using this cmd script as template "ffmpeg -i ni_neema.mp4-i ni_neema.aac -c copy output.mp4"
# to combine the audio and video file into one file
cmd = "ffmpeg -i " + file_name + ".mp4-i " + file_name + ".aac -c copy " + file_name + ".mp4"

# run the cmd command
try:
    subprocess.call(cmd, shell=True)
except:
    print("Error: unable to combine video")
    sys.exit(1)








