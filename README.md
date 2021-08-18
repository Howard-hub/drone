# dronekit測試程式

## 使用Mavlink協議令raspberry pi4和mini pixhawk4連接
前置作業：在Raspberry Pi 4安裝好Raspbian OS
+ 1.打開終端機，依序輸入下列指令
    + sudo apt-get update
    + sudo apt-get install screen python-wxgtk3.0 python-matplotlib python-opencv python-pip python-numpy python-dev libxml2-dev libxslt-dev
    + sudo pip install future
    + sudo pip install pymavlink
    + sudo pip install mavproxy 
+ 2.連接Raspberry Pi 4和mini Pixhawk4
    ![連接Raspberry Pi 3和Pixhawk](image/RaspberryPi_Pixhawk_wiring1.jpg)
    + <font color=#FF0000>注意! 當Raspberry Pi 4是額外接穩定的5V電源時，千萬不要再接上圖的紅線，會燒掉</font>
+ 3.設定Pixhawk
    + 1.電腦開啟Mission Planner，透過USB to Micro USB接上mini Pixhawk4
    + 2.選擇COM?，然後以115200連接
    + 3.等載入完設定，選擇上方的"配置/測試"，點選左側的"Full Parameter List"
    + 4.找到SERIAL?_BAUD這個參數(此參數為serial?的參數)，雙擊數值欄位，改成57(代表57600)
    + 5.找到SERIAL?_PROTOCOL，值改成1，儲存
+ 4.開始測試
    + 測試前需要先禁用raspberry pi的藍芽 
    ```py
    nano /boot/config.txt
    dtoverlay=disable-bt#添加在最後兩行
    ```
    + mavproxy.py --master=/dev/ttyAMA0 --baudrate 57600 --aircraft MyCopter



## 參考資料
網址:
+ https://rmotex.blogspot.com/2017/10/raspberry-pi-3-pixhawk-mavlinkmacos.html
+ https://rmotex.blogspot.com/2017/10/raspberry-pi-3-pixhawk-dronekitpython.html