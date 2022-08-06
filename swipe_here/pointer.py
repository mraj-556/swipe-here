from cvzone.HandTrackingModule import  HandDetector
import cv2,numpy as np,pyautogui as pauto

cap = cv2.VideoCapture(0)
hand_detector_model = HandDetector(detectionCon=0.8,maxHands=1)

if __name__=='__main__':
    while True:
        success , frame = cap.read()
        # hand_found , img = hand_detector_model.findHands(frame)
        hand_found = hand_detector_model.findHands(frame,draw=False)
        if hand_found:
            fingers_up = hand_detector_model.fingersUp(hand_found[0])
            if fingers_up==[0,1,0,0,0]:
                # print('activated')
                index_x_location , index_y_location , index_z_location = hand_found[0]['lmList'][8]
                mouse_x , mouse_y = pauto.position()
                cv2.circle(frame,(int(index_x_location)+30,int(index_y_location)-30),5,(225,0,0),cv2.FILLED)


        cv2.imshow('pointer',frame)
        if cv2.waitKey(1)==ord('q'):
            break