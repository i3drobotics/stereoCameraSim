# Stereo Camera Sim
This package allows for quick testing of stereo configurations. Simulate stereo camera using coppeliaSim vision sensors and generate 3D using the Stereo3D python package.

## Install
Download repository with submodules
```
git clone --recursive https://github.com/i3drobotics/stereoCameraSim
```

*Windows:* add coppeliaSim install directory to the PATH environment variable (See [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) for details on how to add a directory to the PATH environment variable)

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
