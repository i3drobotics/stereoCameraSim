include <include/stereocameraview.scad>

resolution=[2448,2048]; //image resolution
pixelPitch=0.00000345; //m
focalLength=0.016; //m
range=2.5; //m
baseline=0.3; //m
overlap_only=false;

stereoCameraView(resolution,pixelPitch,focalLength,range,overlap_only);