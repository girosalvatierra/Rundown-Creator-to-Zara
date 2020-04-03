from mutagen.mp3 import MP3
arxiu = input('Arrossega arxiu: ')
audio = MP3(arxiu)

duradaarxiu = int(audio.info.length*1000)  

print(duradaarxiu)
final = input('Prem intro per acabar')
