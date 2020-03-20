include <include/stereocameraview.scad>

resolution_px=[2448,2048]; //image resolution
pixelPitch_um=3.45; //um
focalLength_mm=16; //mm
range_m=2.5; //m
baseline_m=0.3; //m
overlap_only=false;

stereoCameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m,overlap_only);