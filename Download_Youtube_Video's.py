from pytube import YouTube

link = "https://youtu.be/Y01NQiOz2nw"

youtube1= YouTube(link)
print(youtube1.title)

print(youtube1.thumbnail_url)
# # get_image

videos= youtube1.streams.all()  #All download format list
# videos= youtube1.streams.filter(only_audio=True) #all audio file list

vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm= int(input("enter : "))
videos[strm].download()
print('succesfully download')
