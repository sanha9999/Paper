오늘 읽어볼 논문은 바로 "A Survey on Moving Object Detection and Tracking Methods"라는 이름의 논문이다. "움직이는 물체 감지와 추적 방법에 대한 조사"라고 볼 수 있겠다. 이번 논문으로 Object Tracking에 대해 알아가볼 예정이다. 그리고 끝으로는 축구공 tracking뿐아니라 경기장안에서 선수의 움직임, 이런 데이터를 다뤄볼 수 있는 프로젝트를 진행해볼예정이다. 

## Abstract
객체 추적(Object Tracking) 알고리즘에는 많은 것이 있는데, 이 알고리즘들의 목적은 비디오에서 영역을 분할(Segmentation)하고 그 움직임과 위치, 맞물림(Occlusion)을 추적하는 것이다.
보통 이미지에서 객체를 추적하기 위한 선행 작업은 객체 감지(Object Detection)과 객체 분류(Object Classification)이다. 일단 영상에 찾고자하는 객체가 존재하는지, 객체가 어디에 있는지에 대해 객체 감지가 수행된다. 감지된 물체는 사람, 차량, 새 등등 다양한 범주로 분류할 수 있다. 객체 추적은 video sequence중에 객체의 존재, 위치, 크기, 모양과 같은 공간적, 시간적 변화를 모니터링함으로 수행된다. 이 논문에서는 객체 추적을 위한 다양한 기법에 대한 분석 및 비교 연구를 포함하여 다양한 알고리즘에 대한 간략한 조사를 제시한다.

## Introduction
객체 추적은 많은 연구자들이 매료되는 분야이다. 또한 computer vision분야에서 매우 중요한 역할을 담당하고 있기도하다. 비디오 시퀀스에서 이미지는 두가지의 픽셀 세트로 나뉘는데 첫번째는 사람, 사물 같은 일반적으로 움직이는 물체인 전경 객체(foreground objects)에 해당하는 픽셀이 포함되고 나머지는 배경(background pixels)에 대한 픽셀 정보를 담고있다. 객체 추적은 실시간 환경에서 중요한데, 가령 보안&감시 분야에서 더 나은 서비스를 제공할 수 있도록 하기 때문이다. 객체 추적을 위한 기본 단계는 아래 그림과 같다.
![](https://images.velog.io/images/sanha9999/post/feebadb9-30ff-4679-9815-78f82a18b8f5/image.png)

## Object Detection Method

### A. Frame Differencing
Frame Differencing은 두 비디오 프레임 간의 차이를 확인하는 기술으로, 프레임 간의 픽셀이 변경된 경우 움직이는 물체(객체)가 있다고 판단하여 그 부분을 찾아내는 기법이다.

![](https://images.velog.io/images/sanha9999/post/4f3cac35-efcb-4d7c-998a-ef799ef897fa/image.png)<center>OpenCV 라이브러리를 이용한 예시 : [출처](https://www.kasperkamperman.com/blog/computer-vision/computervision-framedifferencing/)</center>

### B. Opital Flow
Opital Flow는 이전 프레임과 현재 프레임의 차이를 이용하고 움직임의 벡터 필드를 계산하는 방법이다. 매우 계산량이 많고, noise에 민감하기때문에 real-time 환경에서는 적합하지 않은 방법이다.

![](https://images.velog.io/images/sanha9999/post/561d6f9b-da31-4d19-aa34-e763a3becde5/image.png)

### C. Background Subtraction
Background Subtraction은 배경 제거 기법이다. 이 배경 제거 기법에서 가장 핵심인 것은 배경에서 foreground object(전경 객체, 일반 사물 같은 것)을 먼저 분할하는 배경 모델링 기법이다.
![](https://images.velog.io/images/sanha9999/post/e55dd37c-32cd-4277-b2d2-240e481d0487/image.png)

배경 제거 기법에는 크게 두 가지 기법이 있는데 "Recursive Techniques"와 "Non-Recursive Techniques"이다.

#### Recursive Techniques
이 기술에서는 각 입력 프레임을 기반으로 모델을 반복적으로 업데이트하고 배경 추정을 위한 버퍼는 유지하지 않는 기법이다. 이 기법은 approximate median, adaptive background, Gaussian mixture 같은 다양한 방법을 포함한다.
#### Non-Recursive Techniques
이 기술은 L개의 비디오 프레임을 저장한 버퍼 내에서 각 픽셀의 시간적 변화를 기반으로 슬라이딩 원도우 알고리즘으로 접근하는 기술이다.
