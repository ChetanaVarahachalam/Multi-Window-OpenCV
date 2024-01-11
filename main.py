import cv2

rows=int(input('Please Enter The No.of Rows You Would Like? '))
columns=int(input('And Also The No.Of Columns? '))

width=640
height=320

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,100)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame=cam.read()
    frame=cv2.resize(frame,(int(width/columns),int(height/columns)))

    for i in range(rows):
        for j in range(columns):
            windName= 'Window'+str(i)+'x'+str(j)
            cv2.imshow(windName,frame)
            cv2.moveWindow(windName,int(width/columns)*j,int(height/columns+30)*i)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()
