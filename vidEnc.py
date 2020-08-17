import base64



with open("syd.mp4", "rb") as videoFile:
    text = base64.b64encode(videoFile.read())
    print(text)
    file = open("textTest.txt", "wb") 
    file.write(text)
    file.close()

    fh = open("video.mp4", "wb")
    fh.write(base64.b64decode(text))
    fh.close()
