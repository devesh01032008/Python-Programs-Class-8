import os

word = input("Enter Word or Sentence You want to Pronounce\n")
os.system("termux-tts-speak "+word)
