## ReNet

Segmentation을 공부하다 보니 RNN을 이용한 CNN에서 자주쓰던 Convolution + Pooling방법을 RNN을 통해서 구현한 것을 알게 되었다. 그것이 바로 ReNet인데, 4개의 방향이 다른 RNN을 이용하였다. 자세한 내용은 [논문](https://arxiv.org/pdf/1505.00393.pdf)을 참고해보자.

![](https://images.velog.io/images/sanha9999/post/96d52f17-708e-4237-9f1f-9c26216d49d5/image.png)

이 ReNet을 기반으로 나온 Segmentation model 중 하나가 ReSeg이다.

## ReSeg

ReNet을 기반으로 나온 이 논문의 제목은 "ReSeg: A Recurrent Neural Network-based Model for Semantic Segmentation"이다. 논문을 읽으려면 [링크](https://arxiv.org/pdf/1511.07053.pdf)로 들어가보자.

### ReSeg의 구조

![](https://images.velog.io/images/sanha9999/post/94aff15d-c48d-43d6-8b53-14eeb2495b7d/image.png)<center><h6>ReSeg의 구조</h6></center>

ReSeg는 CNN + RNN의 구조로 되어있는데, 앞의 CNN부분은 VGG16의 앞 7 layer만 사용하였고, CNN의 뒤에는 ReNet을 연결하여 end-to-end 학습이 가능하도록 하였다. 앞 7 layer만 사용한 이유는 모든 layer를 사용하면 이미지의 크기가 줄어들어 해상도가 너무 낮아지는 문제가 있기 때문에 앞부분 7 layer만 사용하는 것이다.

### Transposed convolution

Segmentation을 할 때에는 줄어든 크기를 원 이미지 크기로 복원하기 위해서 upsampling을 해야하는데, 전에 공부한 FCN은 Bilinear interpolation 대신에 Transposed convolution을 사용하였다. ReSeg에서는 Transposed convolution(or Fractionally strided convolution)을 적용하였다. Fractionally strided convolution은 stride의 크기가 1보다 작은 경우로 convolution을 진행하기 때문에 원영상의 중간에 0을 넣고 convolution을 진행하여 map의 크기를 크게 만드는 효과를 얻을 수 있다. 그러므로 upsampling이 가능해진다.

![](https://images.velog.io/images/sanha9999/post/4eb83b2e-fe58-4017-98d2-af94bbb3d55d/image.png)<center><h6>Transposed convolution</h6></center>

## 결과

![](https://images.velog.io/images/sanha9999/post/bcc42534-b370-4b76-8ab1-22afca0e6c94/image.png)<center><h6>Weizmann Horses dataset에 대한 result</h6>
</center>

보다시피 픽셀별 예측을 나타내는 Global acc와 Avg IoU가 ReSeg가 굉장히 높은 것을 알 수 있다.

>### IoU란??
IoU는 "Intersection over Union"의 약자로써, classification문제에서는 top-1, 5 error가 검증 지표였다면 object detection, Segmentation분야에서는 이 IoU가 지표로 사용된다. IoU의 공식은 교집합 영역 넓이 / 합집한 영역 넓이이다. 