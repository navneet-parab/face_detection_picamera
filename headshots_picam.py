import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

name = 'Aniket' #Name of the Person to be verified

camera= PiCamera(resolution = (512, 304), framerate = 10) #Class initialising camera to python
#camera.resolution = (512, 304)
#camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(512, 304))#Creating a 3-D RGB array from camera capture
    
img_counter = 0

while True:
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): 
        image = frame.array
        
        #Show the frame
        cv2.imshow("Press Space to take a photo", image)
        key = cv2.waitKey(1)
   
        #clear the stream of array for the next frame
        rawCapture.truncate(0)
        if key%256 == 27: # ESC pressed
            break
        elif key%256 == 32:
            # SPACE pressed
            #Image captures saved in dataset/Aniket folder
            img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
    if key%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
