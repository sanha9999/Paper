YOLACT, "You Only Look At CoefficienTs"의 줄임말으로 논문의 부제는 Real-time Instance Segmentation이다. 원래대로라면 Mask-RCNN을 다뤄보려했었지만, Mask-RCNN을 공부하고 정리하던 와중에 이 YOLACT를 알게되어 급선회하게 되었다. 

## Instance Segmentation
우선 Instance Segmentation에 대해 집고 넘어가겠다. 
![](https://images.velog.io/images/sanha9999/post/5e5c9511-8b0b-4ce4-8c49-2df81c892bcc/image.png)<center><h6>이미지 분류의 구분</h6></center>

Image Segmentation은 이미지를 픽셀 단위의 다양한 segment로 분할하는 task이다. Image Segmentation은 두가지로 나뉘는데, 동일한 클래스에 해당하는 픽셀을 같은 색으로 칠하는 Semantic Segmentation(저번에 리뷰한 ReSeg가 이 분야에 속한다)과 동일한 클래스여도 다른 사물의 픽셀이면 다른 색으로 칠하는 Instance Segmentation으로 나뉜다.

### Instance Segmentation 모델의 문제점
그동안의 Instance Segmentation 모델(Mask R-CNN, FCIS)은 Object detection모델에 병렬적으로 모델을 추가하여 발전하였었는데, Instance Segmentation이라는게 워낙 복잡하고 어려운 분야이기 때문에 모델의 속도를 올릴 수 없다는게 문제였다. 하지만 YOLACT는 localizition 단계를 생략하여 속도가 굉장히 빨라졌다고 한다.
![](https://images.velog.io/images/sanha9999/post/2c9d0a12-7583-4776-bf8a-2c4588dc65f6/image.png)<center><h6>모델의 속도 차이</h6></center>

### Instance Segmentation의 Metrics
Semantic Segmentation의 Metrics는 IoU를 사용했었다. Instance Segmentation은 mAP라는 Metrics를 사용하는데, 한번 알아보도록하자. mAP는 (mean Average Precision)의 약자이다. Precision은 Positive(긍정)으로 예측을 했을때 실제로 Positive인 것의 비율을 말한다.
자세한 내용은 [잘 정리된 블로그](https://ddamddi.github.io/mldl/2021/05/09/obj_det_and_inst_seg_metric/)를 참조하기 바란다.

## YOLACT Network
![](https://images.velog.io/images/sanha9999/post/b178a109-040e-4ef9-94f1-5fb8b57287c1/image.png)
<center><h6>YOLACT Architecture</h6></center>

YOLACT의 네트워크는 ResNet101 + FPN을 사용하여 기본모델으로 one-stage object detection 모델인 RetinaNet을 사용하였다. 이 one-stage 모델에 feature localization step없이 mask brach를 추가하기 위해서 instance segmentation task를 두가지의 간단한 task로 병렬처리한다. 또한 두 task의 결과물을 linear하게 합쳐서 NMS를 통해 살아남은 instance의 mask를 생성하는 형식이다.