# qr-code-website

- This is based on the sample code from:
https://github.com/nayuki/QR-Code-generator/tree/master/python


## Install

- Data file, `data.txt`:

```
https://gordonturner.com
```

- Install python3, use brew or similar

- Install qrcodegen

```
pip3 install qrcodegen
```

- Run the python script:

```
./qr-code-website.py -i "data.txt" -o qr-code-website-output.svg
```

- Create stl files:

```
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -Dmode=1 -o ./output-stl/qr-code-website-border-black.stl qr-code-website.scad
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -Dmode=2 -o ./output-stl/qr-code-website-base-black.stl qr-code-website.scad
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -Dmode=3 -o ./output-stl/qr-code-website-qr_code-black.stl qr-code-website.scad
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -Dmode=4 -o ./output-stl/qr-code-website-qr_code_negative-white.stl qr-code-website.scad
```

- Fill 15%