from pytube import YouTube
#replace 'YOUTUBE URL' IN LINE 3 WITH YOUR  OWN URL 
#line 4 downloads the first quality of video
YouTube('YOUTUBE URL').streams.first().download()
#LINES 5,6,7 PRINTS ALL DOWNLOADABLE VIDEO FORMATS/QUALITIES
streams = yt.streams.all()
for x in streams:
    print(x)
