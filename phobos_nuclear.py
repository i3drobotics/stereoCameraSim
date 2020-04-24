import os
import subprocess
import time
from scripts.stereoCameraSim import *
import platform

resolution=[2448,2048]
pixel_pitch=0.00000345
focal_length=0.008
view_range=10
baseline=0.3

position=[1.45,-3.6,1.0]
orientation=[10,-15,-60]
camera_name="PhobosNuclear"
api_port=20000

# scale image for better speed (resolution > 500x500 will be slow)
image_scale = 0.25

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
scs.run(simulation_filepath=os.path.join(os.getcwd(),"simulations","StereoCameraSimulationScene.ttt"))