import os
import subprocess
import time
from scripts.stereoCameraSim import *
import platform

resolution=[2448,2048]
pixel_pitch=0.00000345
focal_length=0.016
view_range=100
baseline=0.3

# scale image for better speed (resolution > 500x500 will be slow)
image_scale = 0.25

# scale resolution
resolution=[resolution[0]*image_scale,resolution[1]*image_scale]
# adjust pixel pitch to keep the same FOV
pixel_pitch=pixel_pitch/image_scale

# create StereoCameraSim object with camera parameters
scs = StereoCameraSim(
    resolution=resolution,
    pixel_pitch=pixel_pitch,
    focal_length=focal_length,
    view_range=view_range,
    baseline=baseline
)
# generate stereo camera viewing angle CAD for loading in simulation
scs.generateStereoCam()

# run simulation using generated CAD and camera parameters
scs.runSimulation(
    simulation_filepath=os.path.join("..","simulations","StereoCameraSimulation.ttt"),
    close_on_stop=True,
    hide_simulation=False,
)
# generate 3D from simulated stereo camera
scs.runStereo3D()
while(True):
    exit_code = scs.nextStereo3DFrame()
    if (exit_code == scs.s3D.EXIT_CODE_QUIT):
        break
    if (exit_code == scs.s3D.EXIT_CODE_FAILED_TO_GRAB_3D):
        time.sleep(1)
    else:
        pos,ori = scs.getCameraPosition()
        print(pos,ori)
