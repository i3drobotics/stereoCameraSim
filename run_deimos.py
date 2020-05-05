import os
import subprocess
import time
from modules.stereoCameraSim import *
import platform

resolution=[752,480]
pixel_pitch=0.000006
focal_length=0.0043
view_range=200
baseline=0.06

position=[2,2,0.1]
orientation=[0,-5,-90]
camera_name="StereoCamera"
api_port=20000

# scale image for better speed (resolution > 500x500 will be slow)
image_scale = 1

# scale resolution
resolution=[resolution[0]*image_scale,resolution[1]*image_scale]
# adjust pixel pitch to keep the same FOV
pixel_pitch=pixel_pitch/image_scale

# create StereoCameraSim object with camera parameters
scs = StereoCameraSim(
    api_port=api_port,
    camera_name=camera_name,
    resolution=resolution,
    pixel_pitch=pixel_pitch,
    focal_length=focal_length,
    view_range=view_range,
    baseline=baseline,
    position=position,
    orientation=orientation,
    stereo_view_stl=os.path.join(os.getcwd(),"data","View.stl"),
    stereo_overlap_stl=os.path.join(os.getcwd(),"data","Overlap.stl"),
    output_folder=os.path.join(os.getcwd(),"data")
)

# run simulation (coppeliasim file must have 'StereoCameraModel' already imported)
scs.run(simulation_filepath=os.path.join(os.getcwd(),"simulations","SimulationSceneBoats.ttt"))