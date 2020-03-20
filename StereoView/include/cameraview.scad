include <conversion.scad>

module cameraView(resolution_px,pixelPitch_um,focalLength_mm,range_m) {
    focalLength_m=focalLength_mm/1000;
    sensorSize_m = (pixelPitch_um/1000000)*resolution_px;
    range_mm=range_m*1000;

    echo("sensorSize (m)",sensorSize_m);

    dx = pixelPitch_um/1000*resolution_px[0];
    dy = pixelPitch_um/1000*resolution_px[1];

    vx = dx/(2*focalLength_mm);
    vy = dy/(2*focalLength_mm);

    //FOV (degrees)
    FOVx = 2*atan(vx);
    FOVy = 2*atan(vy);

    echo("FOV X (degrees)",FOVx);
    echo("FOV Y (degrees)",FOVy);
    
    focalLength_px=(resolution_px[0]/2)/tan(FOVx/2);
    echo("Focal length (px)",focalLength_px);

    //size at range (mm)
    atRangeX_mm = (range_mm*tan(FOVx/2)*2);
    atRangeY_mm = (range_mm*tan(FOVy/2)*2);

    atRangeX_m = atRangeX_mm/1000;
    atRangeY_m = atRangeY_mm/1000;

    echo("Image size X @ range (m)",atRangeX_m);
    echo("Image size Y @ range (m)",atRangeY_m);

    x=(atRangeX_m/2);
    y=(atRangeY_m/2);
    z=range_m;

    rotate(180, [ 1, 0, 0 ])
        translate([0,0,-z])
            polyhedron(
              points=[ [x,y,0],[x,-y,0],[-x,-y,0],[-x,y,0], // the four points at base
                       [0,0,z]  ],                          // the apex point 
              faces=[ [0,1,4],[1,2,4],[2,3,4],[3,0,4],      // each triangle side
                          [1,0,3],[2,1,3] ]                 // two triangles for square base
            );
};