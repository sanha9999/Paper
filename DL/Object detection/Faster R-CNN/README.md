## 논문의 제목과 초록과 도표를 먼저보자!
### 논문 제목
논문의 제목은 "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks"이다. 저번에 읽었던 YOLO와 목적이 실시간 객체 감지로 같다. 하지만 뒤에 Region Proposal Networks라는 말이 붙어 있는것으로 보아 YOLO와는 많이 다를 것으로 예측이 된다. YOLOv1논문을 봤을 때 FPS는 YOLOv1이 높았지만 mAP는 Faster R-CNN이 높은 것으로 봐서 이부분도 중점적으로 살펴봐야겠다.
 
### 논문 초록(abstract)
Faster R-CNN은 Region proposal algorithm을 통해 새로운 접근법을 제시한다. SPPNet이나 Fast R-CNN은 Region proposal에 많은 시간을 사용하여 병목현상을 일으키지만, Faster R-CNN은 detection network와 convolutional features를 공유하는 Region proposal network(RPN)을 제안한다고 한다. RPN은 end-to-end로 학습된다. Faster R-CNN은 GPU환경에서 5fps를 보여줬고, ILSVRC, COCO2015에서 1등을 차지했다고 한다.

### 도표 보기
![](https://images.velog.io/images/sanha9999/post/d672f682-923d-43aa-bd72-f68830311fb3/image.png)

Faster R-CNN은 다양한 규모와 크기를 다루기 위해 여러 체계를 사용한다. (a)는 이미지 및 feature map의 피라미드가 구축되고 분류기가 실행되고, (b)는 여러 크기를 가진 필터로 feature map을 만드는 것이고, (c)는 회귀 함수에 reference boxes의 피라미드를 사용한다.

![](https://images.velog.io/images/sanha9999/post/249eaac6-f79a-4f71-95b4-bd7de3888ea7/image.png) 

Faster R-CNN은 YOLO와 마찬가지로 한 개의 통합적인 network로 이루어져있다. Fast R-CNN과 다른점은 RPN이 추가되었다는 정도이다. 그렇다면 RPN은 무엇인가?

![](https://images.velog.io/images/sanha9999/post/3f514424-fe43-4edb-8ac3-33f953ad03ac/image.png)

위의 그림이 Region Proposal Network(RPN)의 구조이다. Conv layer를 통해 뽑아낸 feature map을 입력으로 받고, 이 받은 feature map에 3 * 3 convolution을 수행한다. 그리고 2번째 feature map을 통해 Classification과 box regression 예측 값을 계산한다.

### 결론
RPN을 제시하여 Convolutional features와 Region proposal generation을 공유함으로써 cost가 거의 들지 않고, 이 Faster R-CNN은 실시간에 가까운 속도로 실행할 수 있다. 또한 RPN으로 Region proposal의 성능을 향상시켜 전체적인 객체 탐지 정확도를 향상한다.


## 논문을 읽고 해야할 것!
1. 저자가 뭘 해내고 싶어 했는가?
- 실시간으로 Object detection이 될 수 있는 모델을 만들어내기 위해 그 전의 모델이었던 Fast R-CNN에서 RPN을 추가하여 통합된 네트워크를 만들었다.
2. 이 연구의 접근에서 중요한 요소는 무엇인가?
- 논문에서 가장 많이 강조한 RPN인 것같다. RPN덕분에 Region proposal의 성능을 향상시켜 Faster R-CNN의 전체적인 객체 탐지 정확도를 향상하기때문이다.
3. 나는 스스로 이 논문을 이용할 수 있겠는가?
- Faster R-CNN이 YOLO보다 정확도가 높은건 사실이지만, 실시간...FPS에서는 YOLO에 비해 아무래도 부족하기 때문에 공부하는 용도로 쓸 것같다.
4. 내가 참고하고 싶은 다른 레퍼런스에는 어떤 것이 있나?
- RPN에 대한 지식을 더 쌓아보고싶다.

