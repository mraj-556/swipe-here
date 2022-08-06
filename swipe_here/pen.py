import cv2
from cvzone.HandTrackingModule import HandDetector
from matplotlib.pyplot import draw

cur_x , cur_y , prev_x , prev_Y = 0,0,0,0

cap = cv2.VideoCapture(0)
hand_detect_model = HandDetector(maxHands=1,detectionCon=0.8)
location_list = []
while True:
    success , frame = cap.read()
    hand_found = hand_detect_model.findHands(frame,draw=False)
    if len(location_list)>=2:
                for i in range(len(location_list)-1):
                        cv2.line(frame, location_list[i] , location_list[i+1] , (255,0,0),4 )

    if hand_found:
        fingers_up = hand_detect_model.fingersUp(hand_found[0])
        distance , info = hand_detect_model.findDistance(hand_found[0]['lmList'][4][:2] , hand_found[0]['lmList'][8][:2] )
        cv2.line(frame,hand_found[0]['lmList'][4][:2],hand_found[0]['lmList'][8][:2],(0,255,0),2)
        if int(distance)<18 and hand_found[0]['lmList'][8][2]>-20:
            index_x_location , index_y_location = hand_found[0]['lmList'][8][:2]
            # print(index_x_location , index_y_location)
            cur_x , cur_y = index_x_location , index_y_location
            if len(location_list)<2:
                location_list.append((cur_x,cur_y))
            elif len(location_list)>=2:
                moved_distance , info = hand_detect_model.findDistance(location_list[-1] , (cur_x,cur_y))
                if moved_distance>5:
                    location_list.append((cur_x,cur_y))


        if fingers_up==[1,1,1,1,1]:
            while len(location_list):
                del location_list[0]
                print('removing')
                location_list=[]
    frame = cv2.flip(frame,1)
    cv2.imshow('img',frame)
    if cv2.waitKey(1)==ord('q'):
        break