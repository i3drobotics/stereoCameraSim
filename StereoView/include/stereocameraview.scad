include <cameraview.scad>

module stereoCameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m,overlap_only=false) {
    if (overlap_only){
        intersection(){
            echo("Camera 1");
            translate([baseline_m/2,0,0])
            cameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m);
            echo("Camera 2");
            translate([-baseline_m/2,0,0])
            cameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m); 
        }
    } else {
        echo("Camera 1");
        translate([baseline_m/2,0,0])
        cameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m);
        echo("Camera 2");
        translate([-baseline_m/2,0,0])
        cameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m);
    }
}