import cv2               
import os

def check_path(path):            
    dir = os.path.dirname(path)  
    if not os.path.exists(dir):
        os.makedirs(dir)

vid_cam = cv2.VideoCapture(0)  

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

face_id = 1  
count = 0    

check_path("dataset/")
while(True):
    _,image_frame = vid_cam.read()       
    
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY) 
    
    faces = face_cascade.detectMultiScale(gray, 1.4, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2) 
        
        count += 1              

        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('Creating Dataset!!!', image_frame)  

    if cv2.waitKey(100) & 0xFF == 27:                   
        break

    elif count>100:                                     
        break

vid_cam.release()                                       

cv2.destroyAllWindows()                                 

