# YOLOV5_product_calculator
yolov5를 이용한 물체탐지_및_yolov5사용법

## 1. 사용법
  ### 1-1 이미지 만들기.
이미지 촬영 후, increase.py를 통해 이미지 증식 *ImageDataGenerator사용. increase.py파일 내부에 자세한 경로설정방법을 각주로 적어놓음.
labelImg.py를 통해 이미지 라벨링을 진행, *사용전 pyqt5가 설치되어 있어야 함.

  ### 2-1 YOLOv5사용을 위해 annotation(디렉토리정리) 설정 및 학습방법
MAIN_CODE 내부에 data - images - train에 학습시킬 데이터를 저장.
MAIN_CODE 내부에 data - images - val에 검증데이터 저장.
label또한 똑같이 저장. *이미지파일 이름과, 라벨텍스트파일 이름이 같아야함.
datapath파일 내에 dataset.py를 열어 경로를 수정, 경로에 " " <-는 필요없음. 데이터 경로를 C:\\ 부터 복사해서 갖다가 붙여놓으면 됨.
CUDA와 파이토치 1.15, 넘파이 1.18 버전 이상을 설치. 
anaconda 가상환경을 활성화 시킨 cmd창을 열어서 yolov5디렉토리 까지 이동. 
학습하고 싶은 모델을 yolov5/models/ 에 있는 yaml확장자 파일 중에서 선택하여 yolov5파일에 복사
python train.py --data datset.yaml --cfg yolov5s.yaml*<-이부분은 욜로학습모델을 적으면 됨  --batch-size 64  코드 입력. 

  ## 3 실행
#3-1학습이 끝나면 weight에 학습한 weight가 저장된 모델이 best.pt와 last.pt로 저장되어 있음.
#3-2학습이 끝나면 yolov5내 detect.py파일을 열어서 맨 및 파라메타에 본인이 학습한 모델명을 입력 후 sorece부분을 input데이터 경로로 설정한 후 실행.

## *실행이 힘든 분을 위한 팁.
* detect.py는 미리 학습되어 있는 yolov5s.pt를 디폴트로 설정하였음, 
* input데이터는 inference/images/에서 학습하는 것을 디폴트로 설정하였기에, 사진파일을 거기다 넣어두면 됨.

* detect2.py는 1.내장 캠이 달린 노트북 환경에서 외장 캠을 추가로 설치하였을 경우, 2. best.pt(내가 학습한 모델)을 디폴트로 설정하였음. 
* 내장 캠을 사용하고자 하는 경우, utils/datasets.py에 들어가서 cap = cv2.VideoCapture(1 if s == '1' else s) <-이부분의 1을 0으로 바꿔주고 실행시켜 주면 됨.
* detect2.py에서 본인이 학습한 모델을 사용하고자 하는 경우, yolov5디렉토리에 본인모델을 best.pt로 저장하고 사용하면 됨.

  ## 4-1 yolo에 대한 학습 자료는 정리ppt 및 자료에 저장되어 있음.

## 정리자료 내의 저작권 및 코드의 저작권은 https://github.com/ultralytics/yolov5와 네이버 블로그 등의 자료를 활용하여 
커스터마이징 하였음을 밝힘.

![img1](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0001.jpg)
![img2](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0002.jpg)
![img3](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0003.jpg)
![img4](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0004.jpg)
![img5](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0005.jpg)
![img6](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0006.jpg)
![img7](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0007.jpg)
![img8](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0008.jpg)
![img9](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0009.jpg)
![img10](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0010.jpg)
![img11](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0011.jpg)
![img12](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0012.jpg)
![img13](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0013.jpg)
![img14](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0014.jpg)
![img15](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0015.jpg)
![img16](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0016.jpg)
![img17](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0017.jpg)
![img18](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0018.jpg)
![img19](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0019.jpg)
![img20](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0020.jpg)
![img21](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0021.jpg)
![img22](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0022.jpg)
![img23](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0023.jpg)
![img24](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0024.jpg)
![img25](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0025.jpg)
![img26](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0026.jpg)
![img27](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0027.jpg)
![img28](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0028.jpg)
![img29](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0029.jpg)
![img30](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0030.jpg)
![img31](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0031.jpg)
![img32](https://github.com/Falconno7/YOLOV5-_product_calculator-KOREAN/blob/master/img/0032.jpg)
