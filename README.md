# OpenCV-QRCodeDetector-Sample
OpenCVでのQRコード検出サンプルプログラムです。<br>
<img src="https://user-images.githubusercontent.com/37477845/134704001-ac8e0d21-a5ec-4e48-b4ce-61a5153922b4.gif" width="60%">

2021年9月25日現在サポートされている以下の機能を実装しています。
* QRCodeDetector：detectAndDecode
* QRCodeDetector：detectAndDecodeMulti
* QRCodeDetector：detectAndDecodeCurved
* WeChatQRCode：detectAndDecode

# Requirement 
* opencv-python 4.5.3.56 or later

# Demo
デモの実行方法は以下です。
```bash
python sample_QRCodeDetector_detectAndDecode.py
python sample_QRCodeDetector_detectAndDecodeMulti.py
python sample_QRCodeDetector_detectAndDecodeCurved.py
python sample_WeChatQRCode_detectAndDecode.py
```
* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --width<br>
カメラキャプチャ時の横幅<br>
デフォルト：960
* --height<br>
カメラキャプチャ時の縦幅<br>
デフォルト：540

# Reference
* [OpenCV Document](https://docs.opencv.org/master/namespaces.html)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
AprilTag-Detection-Python-Sample is under [Apache v2 License](LICENSE).
