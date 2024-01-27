import os
import cv2

detect = 1 

Testing = True
Profiling = False 
write = False 
In_write = False
Out_write = False

debugging = True 

debugging_Lane = True

debugging_L_ColorSeg = True
debugging_L_Est= True
debugging_L_Cleaning= True
debugging_L_LaneInfoExtraction= True

debugging_Signs = True
debugging_TrafficLights = True
debugging_TL_Config = True

enable_SatNav = False


animate_steering = False


angle_orig = 0
angle = 0
 
engines_on = False

clr_seg_dbg_created = False

Detect_lane_N_Draw = True
Training_CNN = False 

vid_path = os.path.abspath("data/vids/Ros2/lane.avi")
loopCount=0


Resized_width = 320#320#240#640#320 # Control Parameter
Resized_height = 240#240#180#480#240

in_q = cv2.VideoWriter( os.path.abspath("data/Output/in_new.avi") , cv2.VideoWriter_fourcc('M','J','P','G'), 30, (Resized_width,Resized_height))
out  = cv2.VideoWriter( os.path.abspath("data/Output/out_new.avi") , cv2.VideoWriter_fourcc('M','J','P','G'), 30, (Resized_width,Resized_height))

if debugging:
    waitTime = 1
else:
    waitTime = 1

Ref_imgWidth = 1920
Ref_imgHeight = 1080


Frame_pixels = Ref_imgWidth * Ref_imgHeight

Resize_Framepixels = Resized_width * Resized_height

Lane_Extraction_minArea_per = 1000 / Frame_pixels
minArea_resized = int(Resize_Framepixels * Lane_Extraction_minArea_per)

BWContourOpen_speed_MaxDist_per = 500 / Ref_imgHeight
MaxDist_resized = int(Resized_height * BWContourOpen_speed_MaxDist_per)

CropHeight = 650 
CropHeight_resized = int( (CropHeight / Ref_imgHeight ) * Resized_height )