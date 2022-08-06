# from pynput.keyboard import Key,Controller
# import mediapipe as mp
# import cv2,time,os,sys


#                         ######################  Variables  ######################

# global prev_x,prev_y , distance , pointer , selected_mode , data , frame1 , required_path

# prev_x,prev_y = 320,240
# distance = 0
# pointer = -1
# selected_mode = 2
# data = []
# frame1 = cv2.imread(r'C:\Users\TUF\OneDrive\Pictures\Camera Roll/home.png')

#         ######################  Webcam and hand detection and keyboard objects  ######################

# cap = cv2.VideoCapture(0)

# keyboard = Controller()

# hand_obj = mp.solutions.hands
# hand = hand_obj.Hands()
# draw = mp.solutions.drawing_utils

#             ######################  Button  to  be  pressed  ######################

# def Choose_mode():
#     global selected_mode
#     print('Select Mode : ')
#     print('     1. Presentstion mode')
#     print('     2. Gallery mode (Default)')

#     while True:
#         m = int(input())
#         if m==1:
#             selected_mode = 1
#             break
#         elif m==2:
#             selected_mode=2
#             break
#         else:
#             print('Invalid  Choice.....')
#             print('     *************       *************       *************')

#                     ######################  Mode  Execute  ######################

# def move_forward():
#     keyboard.press(Key.right)
#     print('Move forward')

# def move_backward():
#     keyboard.press(Key.left)
#     print('Move backward')

# def resize_frame():
#     global frame1
#     frame1 = cv2.resize(frame1,(1920,1080))

# def right_swipe():
#     global pointer , frame1 , required_path
#     if pointer < len(data)-1:
#         pointer += 1
#         img = required_path + data[pointer]
#         print(pointer)
#         frame1 = cv2.imread(img)
#         resize_frame()
#         # print(img)
#         cv2.imshow('Show',frame1)
#     else:
#         print('End Point')
#     print('Right Move')

# def left_swipe():
#     global pointer , frame1 , required_path
#     if pointer > 0:
#         pointer += -1
#         img = required_path + data[pointer]
#         # print(pointer)
#         frame1 = cv2.imread(img)
#         resize_frame()
#         # print(img)
#         cv2.imshow('Show',frame1)
#     else:
#         print('End Point')
    
#     print('Left Move')

#             ######################  Main  code  ######################

#                 ##############  Mode selection  ##############

# # Choose_mode()

#                 ##############  Execution  Start  ##############
# def main():
#     global prev_x,prev_y , distance , pointer , selected_mode , data , frame1 , required_path
#     Choose_mode()
#     while True:
#         if selected_mode==2:
#             # required_path = input("Enter  your path :")
#             try:
#                 required_path = r'C:\Users\TUF\OneDrive\Pictures\Camera Roll/'
#                 data = os.listdir(required_path)
#                 del data[0]
#                 # print(len(data),data)
#             except:
#                 print('Error')
#         if (selected_mode==2 and data and len(data)>0) or selected_mode==1:
#             success , frame = cap.read()
#             frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             hand_found = hand.process(frame_rgb)
#             hand_found = hand_found.multi_hand_landmarks

#             height,width,c = frame.shape
#             cv2.putText(frame,"C",(width//2,height//2),cv2.FONT_ITALIC,1,(0,235,0),5)
#             cv2.putText(frame,"L",(200,240),cv2.FONT_ITALIC,1,(0,235,0),5)
#             cv2.putText(frame,"R",(440,240),cv2.FONT_ITALIC,1,(0,235,0),5)

#             if hand_found:
#                 for hand_details in hand_found:
#                     # print(len(hand_details.landmark))
#                     for id,location in enumerate(hand_details.landmark):
#                         # print(id,location)
#                         # print()
#                         if id==12:
#                             x , y = location.x , location.y
#                             x , y = int(x*width) , int(y*height)
#                             cv2.circle(frame,(x,y),5,(255,0,0),cv2.FILLED)
#                             if x > prev_x and x>width//2:
#                                 if x < 440:
#                                     prev_x = x+10
#                                     distance+=1
#                                     # print("going right")
#                                 if x>440 and distance>3:
#                                     cv2.putText(frame,"Swipped right",(400,50),cv2.FONT_ITALIC,1,(0,220,0),5)
#                                     if selected_mode==2:
#                                         right_swipe()
#                                     elif selected_mode==1:
#                                         move_forward()
#                                     distance,prev_x,prev_y=0,320,240
                                
#                             if x < prev_x and x<width//2:
#                                 if x > 200:
#                                     prev_x = x-10
#                                     distance+=1
#                                     # print("going left")
#                                 if x<200 and distance>3:
#                                     cv2.putText(frame,"Swipped left",(180,50),cv2.FONT_ITALIC,1,(0,220,0),5)
#                                     if selected_mode==2:
#                                         left_swipe()
#                                     elif selected_mode==1:
#                                         move_backward()
#                                     distance,prev_x,prev_y=0,320,240


#         cv2.imshow('swipe',frame)
#         if cv2.waitKey(1) == ord('q'):
#             break

# if __name__=='__main__':
#     main()
def main():
    while True:
        print('hi')