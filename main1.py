import cv2
from simple_facerec import SimpleFacerec



# encode faces from our folder

sfr = SimpleFacerec()                                       # this simplce rec is class which is used face recognition model
sfr.load_encoding_images("images/")

cap = cv2.VideoCapture(0)               #Load camera   for connection with camera



while True:
    ret, frame = cap.read()                                         #cap.read means it will read the frame through web cam , where frame is image data and ret is boolean idicator hai which tell if it read succesfully or not

    # detect faces
    face_locations, face_names = sfr.detect_known_faces(frame)              # it will detect face in current frame which is going in web cam and recognize known face
    for face_loc, name in zip(face_locations, face_names):
        y1 , x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]   # this is nothing like agar mai detect kr rha hunn face to usme ttop left right botoom and all

        cv2.putText(frame, name, (x1, y1 -10), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)   # this is is the text in detector
        cv2.rectangle(frame, (x1,y1),(x2, y2),(0,0,200),4)




    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()




