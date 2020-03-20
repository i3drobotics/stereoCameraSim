from Stereo3D import Stereo3D, StereoCalibration
from Stereo3D.StereoCapture import *

left_api_port = 20000
left_vision_sensor_name = "StereoCameraLeft"
right_api_port = 20001
right_vision_sensor_name = "StereoCameraRight"
camera_name = "vrep"
camL = VREPCapture(left_api_port,left_vision_sensor_name)
camR = VREPCapture(right_api_port,right_vision_sensor_name)
stcapVREP = StereoCaptureVREP(camL,camR)
stcap = StereoCapture(stcapVREP)

# define inout folder
folder = "data/"
# define calibration files for left and right image
left_cal_file = folder + camera_name +"_left.yaml"
right_cal_file = folder + camera_name +"_right.yaml"
# get calibration from yaml files
stcal = StereoCalibration()
stcal.get_cal_from_yaml(left_cal_file,right_cal_file)

# setup Stereo3D
s3D = Stereo3D(stcap,stcal,"BM")
# run Stereo3D GUI for generating 3D
s3D.run(folder)