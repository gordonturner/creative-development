mode = 0;

module border() {
    translate([0,0,2])
    difference(){
    cube([120,120,4],center=true);
    cube([108,108,4],center=true);
    };
}

module base() {
    cube([120,120,2],center=true);
}

module qr_code() {
    translate([0,0,2])
    resize([100,100,0])
    linear_extrude(height = 2){
    	offset(delta=0.001)
    	import(file = "./qr-code-website-output.svg", center=true);
    };
}

module qr_code_negative() {
    difference(){
        translate([0,0,2])
        cube([108,108,4],center=true);
        translate([0,0,2])
        resize([100,100,0])
        linear_extrude(height = 2){
            offset(delta=0.001)
            import(file = "./qr-code-website-output.svg", center=true);
        };
    };
}

module assembly() {
     border();
     base();
     qr_code();
     qr_code_negative();
}

if (mode == 1) {
     border();
} else if (mode == 2) {
     base();
} else if (mode == 3) {
     qr_code();
} else if (mode == 4) {
     qr_code_negative();
} else {
     assembly();
}