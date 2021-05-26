import speech_recognition as sr 
import moviepy.editor as mp

clip = mp.VideoFileClip(r"jnt.mp4") 
 
clip.audio.write_audiofile(r"convertedjnt.wav")
r = sr.Recognizer()

audio = sr.AudioFile("convertedjnt.wav")
with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file, language='ms-MY')
# exporting the result 
with open('jnt.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")

file = open('jnt.txt')
data = file.read()
memohoncount = data.count("memohon")
maafcount = data.count("maaf")
print("Memohon: ",memohoncount,"kali")
print("Maaf: ",maafcount,"kali")


