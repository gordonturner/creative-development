# Pixelmogrifier

## macOS Install

- Install dependencies:

```
brew update
brew upgrade
```

```
brew install opencv3
```

```
pip3 install --upgrade numpy 
```


## Linux Install

- TODO: Accepting documentation PRs


## Windows Install

- TODO: Accepting documentation PRs


## Input Images

- Suggest downloading image from wikipedia:

https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg

https://en.wikipedia.org/wiki/File:Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg

https://en.wikipedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg


## Run

- Run:

```
./pixelify.py -i ./input-images/mona-lisa.jpg -o ./output-images/mona-lisa.jpg

./pixelify.py -i ./input-images/van-gogh-self-portrait.jpeg -o ./output-images/van-gogh-self-portrait.jpeg

./pixelify.py -i ./input-images/van-gogh-starry-night.jpg -o ./output-images/van-gogh-starry-night.jpg
```


## Credit

- Most of the heavy lifting is leveraged from this SO post:

https://stackoverflow.com/questions/55508615/how-to-pixelate-image-using-opencv-in-python

- Added command line argument handling etc 