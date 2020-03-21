include <cameraview.scad>

module stereoCameraView(resolution,pixelPitch,focalLength,range,overlap_only=false) {
    if (overlap_only){
        intersection(){
            echo("Camera 1");
            translate([baseline/2,0,0])
            cameraView(resolution,pixelPitch,focalLength,range);
            echo("Camera 2");
            translate([-baseline/2,0,0])
            cameraView(resolution,pixelPitch,focalLength,range); 
        }
    } else {
        echo("Camera 1");
        translate([baseline/2,0,0])
        cameraView(resolution,pixelPitch,focalLength,range);
        echo("Camera 2");
        translate([-baseline/2,0,0])
        cameraView(resolution,pixelPitch,focalLength,range);
    }
}