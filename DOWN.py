from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=himEMfYQJ1w').streams.first().download()
streams = yt.streams.all()
for x in streams:
    print(x)