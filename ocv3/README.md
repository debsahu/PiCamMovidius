## Install Paho-MQTT

```
pip3 install paho-mqtt
sudo pip3 install paho-mqtt
```

### OpenCV 3.2 YoLoV2

- Install pre-compiled [OpenCV 3.2](https://yoursunny.com/t/2018/install-OpenCV3-PiZero/)
- Add to apt-source list 
```
echo 'deb [trusted=yes] http://dl.bintray.com/yoursunny/PiZero stretch-backports main' | sudo tee  /etc/apt/sources.list.d/bintray-yoursunny-PiZero.list
```
- Update apt 
```
sudo apt update
```
- Install OpenCV 
```
sudo apt install python3-opencv
```
- Verify Install 
```
python3 -c 'import cv2; print(cv2.__version__)'
```
- Enable V4L driver 
```
sudo modprobe bcm2835-v4l2
```
- Enter into following directory
```
cd ~/PiCamMovidius/ocv3
make
```
- Edit picam.py with appropiate MQTT server IP, port and topic and run python script
```
python3 picam.py
```
