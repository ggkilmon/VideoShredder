from moviepy.editor import *

LENGTH_OF_CLIP = 9
NAME_OF_FILE = "sample-mp4-file.mp4"

with VideoFileClip(NAME_OF_FILE) as clip:
    length = clip.duration
    print(f'clip length: {length}s')

    numberOfClips = length / LENGTH_OF_CLIP

    numberOfClipsCount = 0
    while (numberOfClipsCount <= numberOfClips):
        startClip = numberOfClipsCount * LENGTH_OF_CLIP
        endClip = startClip + LENGTH_OF_CLIP
        subClip = clip.subclip(startClip, endClip)
        filename = "./output/{NAME_OF_FILE}_{numberOfClipsCount:06}.gif".format(NAME_OF_FILE = NAME_OF_FILE, numberOfClipsCount = numberOfClipsCount)
        print(filename)
        subClip.write_gif(filename, 24)
        numberOfClipsCount += 1
    
    
