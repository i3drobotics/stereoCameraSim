include <conversion.scad>

module cameraView(resolution_px,pixelPitch,focalLength,range) {
    sensorSize = pixelPitch*resolution_px;

    echo("sensorSize (m)",sensorSize);

    v = sensorSize/(2*focalLength);

    //FOV (degrees)
    FOV = [2*atan(v[0]),2*atan(v[1])];

    echo("FOV X (degrees)",FOV[0]);
    echo("FOV Y (degrees)",FOV[1]);
    
    focalLength_px=(resolution_px[0]/2)/tan(FOV[0]/2);
    echo("Focal length (px)",focalLength_px);

    //size at range (mm)
    atRange = [range*tan(FOV[0]/2)*2,range*tan(FOV[1]/2)*2];

    echo("Image size X @ range (m)",atRange[0]);
    echo("Image size Y @ range (m)",atRange[1]);

    x=atRange[0]/2;
    y=atRange[1]/2;
    z=range;

    rotate(180, [ 1, 0, 0 ])
        translate([0,0,-z])
            polyhedron(
              points=[ [x,y,0],[x,-y,0],[-x,-y,0],[-x,y,0], // the four points at base
                       [0,0,z]  ],                          // the apex point 
              faces=[ [0,1,4],[1,2,4],[2,3,4],[3,0,4],      // each triangle side
                          [1,0,3],[2,1,3] ]                 // two triangles for square base
            );
};