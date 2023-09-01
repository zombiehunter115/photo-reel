import cv2

video = cv2.VideoCapture("AnthonyShkraba.mp4")
if (video.isOpened()==False):
    print("unable tor read the feed")
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))
while(True):
    ret,frame = video.read()
    cv2.imshow("webcam",frame)
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break
video.release()
out.release()
cv2.destroyAllWindows()
