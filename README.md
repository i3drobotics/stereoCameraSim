# Stereo Camera Sim
This package allows for quick testing of stereo configurations. This package will create a simulated stereo camera in coppeliasim based on camera specifications. These simulated cameras can be read by the Stereo3D python package to generate 3D. 

## Install
Download repository with submodules
```
git clone --recursive https://github.com/i3drobotics/stereoCameraSim
```

Full CoppeliaSim directory included in this repository, make sure you clone with recursive to pull the submodule. 
*Windows:* add coppeliaSim install directory to the PATH environment variable (See [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) for details on how to add a directory to the PATH environment variable). 

*Linux:* add coppeliaSim to bashrc
```
sudo gedit ~/.bashrc
add this to the end --> export COPPELIASIM_ROOT=/PATH_TO_REPO/coppeliaSim
```

*Note: PyRep is faster than using the remote api but is currently only available on Linux. Will update this step with windows instructions once I figure how out to build pyrep for windows. For now the remote api will be used.*

Install openscad </br>
*Linux:*
```
sudo apt-get install openscad
```
*Windows:* </br>
Download and install from here: https://www.openscad.org/downloads.html
add openscad install directory to the PATH environment variable (See [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) for details on how to add a directory to the PATH environment variable)

Download and install python 3.6+ from [here](https://www.python.org/downloads/)

Install Stereo3D pip package
```
python -m pip install stereo3d
```

## Run
Edit parameters in run.py
```
...
resolution=[2448,2048]
pixel_pitch=0.00000345
focal_length=0.016
view_range=100
baseline=0.3
...
```
Launch run script:
```
python run.py
```
This will launch the simulation and create a stereo camera with your specifications. Stereo3D will attach to this simulation and start generating 3D.
The available view of the stereo system will be shown on the simulation. White is the full view of each camera and green is the overlap (the area that both cameras can see, therfore the area than can have 3D).
![Image of simulated stereo camera view and generated 3D](https://github.com/i3drobotics/stereoCameraSim/Example3.png)