openscad GenerateStereoView.scad -o StereoViewFull.stl ^
-D "resolution_px=[2448,2048]" ^
-D "pixelPitch_um=3.45" ^
-D "focalLength_mm=16" ^
-D "range_m=2.5" ^
-D "baseline_m=0.3" ^
-D "overlap_only=true"