from Stereo3D import Stereo3D, StereoCalibration
from Stereo3D.StereoCapture import *
import os
import subprocess
import math
import time
import platform

if platform.system() == "Linux":
    from pyrep import PyRep

class StereoCameraSim:
    def __init__(self,api_port=20000,
                stereo_view_stl=os.path.join(os.getcwd(),"simulations","StereoView","StereoView.stl"),
                stereo_overlap_stl=os.path.join(os.getcwd(),"simulations","StereoView","StereoOverlap.stl"),
                resolution=[2448,2048],pixel_pitch=0.00000345,focal_length=0.016,view_range=2.5,baseline=0.3):
        self.api_port = api_port
        self.stereo_view_stl = stereo_view_stl
        self.stereo_overlap_stl = stereo_overlap_stl
        self.resolution = resolution
        self.pixel_pitch = pixel_pitch
        self.focal_length = focal_length
        self.view_range = view_range
        self.baseline = baseline
        self.FOV = self.calc_FOV(resolution,pixel_pitch,focal_length)

    def runStereo3D(self,left_vision_sensor_name="StereoCameraLeft",right_vision_sensor_name = "StereoCameraRight"):
        camera_name = "vrep"
        stcapVREP = StereoCaptureVREP(left_vision_sensor_name,right_vision_sensor_name,self.api_port)
        stcap = StereoCapture(stcapVREP)

        # define inout folder
        self.folder = "data/"
        # define calibration files for left and right image
        left_cal_file = os.path.join(self.folder, camera_name +"_left.yaml")
        right_cal_file = os.path.join(self.folder, camera_name +"_right.yaml")
        # get calibration from yaml files
        stcal = StereoCalibration()
        stcal.get_cal_from_yaml(left_cal_file,right_cal_file)

        # setup Stereo3D
        self.s3D = Stereo3D(stcap,stcal,"BM")
        # connect to stereo camera
        connected = False
        while(not connected):
            connected = self.s3D.connect()
            time.sleep(1)

    def getCameraPosition(self):
        return self.s3D.stereo_camera.stcam.camera.get_last_pose()

    def nextStereo3DFrame(self):
        exit_code = self.s3D.run_frame(self.folder)
        if (exit_code == self.s3D.EXIT_CODE_QUIT):
            self.s3D.stereo_camera.close()
        return exit_code

    def generateStereoView(self,stl,overlap_only=False):
        resolution_str = "[{},{}]".format(self.resolution[0],self.resolution[1])
        pixelPitch_str = "{}".format(self.pixel_pitch)
        focalLength_str = "{}".format(self.focal_length)
        range_str = "{}".format(self.view_range)
        baseline_str = "{}".format(self.baseline)
        overlap_only_str = "{}".format(overlap_only).lower()

        cmd = ['openscad','GenerateStereoView.scad','-o',stl,
                '-D', 'resolution={}'.format(resolution_str),
                '-D', 'pixelPitch={}'.format(pixelPitch_str),
                '-D', 'focalLength={}'.format(focalLength_str),
                '-D', 'range={}'.format(range_str),
                '-D', 'baseline={}'.format(baseline_str),
                '-D', 'overlap_only={}'.format(overlap_only_str)]
        cwd = os.path.join(os.getcwd(),"simulations","StereoView")

        print("cd " + cwd)

        cmd_str = ""
        for c in cmd:
            cmd_str += c + " "
        print(cmd_str)

        if platform.system() == "Windows":
            proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        else:
            proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, universal_newlines=True)

    def generateStereoCam(self):
        self.generateStereoView(self.stereo_view_stl,False)
        self.generateStereoView(self.stereo_overlap_stl,True)

    def rad2deg(self,rad):
        return(rad * 180 / math.pi)

    def deg2rad(self,deg):
        return(deg * math.pi / 180)

    def calc_FOV(self,resolution,pixel_pitch,focal_length):
        dx = pixel_pitch*resolution[0]
        dy = pixel_pitch*resolution[1]

        vx = dx/(2*focal_length)
        vy = dy/(2*focal_length)

        FOVx = self.rad2deg(2*math.atan(vx))
        FOVy = self.rad2deg(2*math.atan(vy))

        FOV = [FOVx,FOVy]
        return FOV

    def runSimulationPyRep(self,simulation_filepath=os.path.join("simulations","StereoCameraSimulation.ttt"),close_on_stop=False,hide_simulation=False):
        if platform.system() == "Linux":
            pr = PyRep()
            # Launch the application with a scene file in headless mode
            pr.launch(simulation_filepath,headless=hide_simulation) 
            pr.start()  # Start the simulation

            # Do some stuff
            #TODO add PyRep to Stereo3D and grab images directly (rather than with remote api)

            pr.stop()  # Stop the simulation
            pr.shutdown()  # Close the application
        else:
            print("PyRep only available on Linux")

    def runSimulation(self,simulation_filepath=os.path.join("..","..","simulations","StereoCameraSimulation.ttt"),close_on_stop=False,hide_simulation=False):
        resolution_str = "{},{}".format(self.resolution[0],self.resolution[1])
        fov_str = "{}".format(self.FOV[0])
        range_str = "{}".format(self.view_range)
        baseline_str = "{}".format(self.baseline)

        cmd = ['-s',
                    '-Gapi_port={}'.format(self.api_port),
                    '-Gstereo_view_stl={}'.format(self.stereo_view_stl),
                    '-Gstereo_overlap_stl={}'.format(self.stereo_overlap_stl),
                    '-Gstereo_overlap_stl={}'.format(self.stereo_overlap_stl),
                    '-Gresolution={}'.format(resolution_str),
                    '-Gfov={}'.format(fov_str),
                    '-Gview_range={}'.format(range_str),
                    '-Gbaseline={}'.format(baseline_str),
                    simulation_filepath]

        if (close_on_stop):
            cmd.append('-q')
        if (hide_simulation):
            cmd.append('-h')

        if platform.system() == 'Windows':
            cmd.insert(0, 'coppeliaSim')
            cmd.insert(0, '/b')
            cmd.insert(0, 'start ')

        if platform.system() == 'Linux':
            cmd.insert(0, os.getenv('COPPELIASIM_ROOT')+'/coppeliaSim.sh')
            cmd.append('&')

        cwd = os.path.join(os.getcwd(),"coppeliaSim")

        print("cd " + cwd)
        cmd_str = ""
        for c in cmd:
            cmd_str += c + " "
        print(cmd_str)

        if platform.system() == "Windows":
            proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        else:
            proc = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, universal_newlines=True)