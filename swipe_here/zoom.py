from math import dist
from cvzone.HandTrackingModule import HandDetector
import cv2

global cur_x , cur_y , new_x , new_y
cur_x , cur_y , new_x , new_y = 500 ,500 ,500 ,500

cap = cv2.VideoCapture(0)
hand_detect_model = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    global cur_x , cur_y , new_x , new_y
    while True:
        success , frame = cap.read()
        hand_found = hand_detect_model.findHands(frame,draw=False)
        # if len(hand_found)==2:
        #     print((hand_found))
        if hand_found and len(hand_found) == 2:
            fingers_up_1 = hand_detect_model.fingersUp(hand_found[0])
            fingers_up_2 = hand_detect_model.fingersUp(hand_found[1])

            if fingers_up_1==[1,1,1,1,1] and fingers_up_2==[1,1,1,1,1]:
                distance , info = hand_detect_model.findDistance( hand_found[0]['lmList'][12][:2] , hand_found[1]['lmList'][12][:2] )
                cv2.line(frame,hand_found[0]['lmList'][12][:2],hand_found[1]['lmList'][12][:2],(0,255,0),2)
                
                if 100<=distance<=500:
                    # print(fingers_up_1,fingers_up_2)
                    resize_percentage = (distance-100)//2
                    if resize_percentage<30:
                        resize_percentage=30
                    cur_x , cur_y , alpha_channel = frame.shape
                    new_x , new_y = int(cur_x*(resize_percentage/100)) , int(cur_y*(resize_percentage/100))
                    cur_x , cur_y = new_x , new_y
                    print(cur_x,cur_y)
                    print(new_x,new_y)
                    print()

        frame = cv2.resize(frame,(cur_x,cur_y))


        cv2.imshow('Zoom',frame)
        if cv2.waitKey(1)==ord('q'):
            break


if __name__=='__main__':
    main()
    
# def main():
#     while True:
#         print('Hello')