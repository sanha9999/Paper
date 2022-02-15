논문의 제목은 "SIMPLE ONLINE AND REALTIME TRACKING", 줄여서 SORT로 트래킹 알고리즘중 하나이다.

## ABSTRACT
본 논문은 온라인과 실시간 application을 위해 객체를 효과적으로 연결하는 것이 focus인 multiple object tracking에 대한 실용적인 접근 방식을 탐구한다. 이를 위해 detection quality는 tracking performance를 위한 핵심 요소로 여겨지며, detector를 변경하면 tracking performance를 최대 18.9%까지 향상할 수 있다. 칼만 필터(Kalman Filter)와 헝가리안 알고리즘(Hungarian algorithm)같은 친숙한 기술의 조합만 사용함에도 불구하고, 이 접근은  SOTA(state-of-the-art)에 버금가는 정확도를 달성했다. 뿐만 아니라, 우리의 tracking method는 간단하기 때문에 다른 SOTA tracker보다 20배 이상 빠른 260Hz의 속도로 업데이트된다.

## INTRODUCTION
이 논문은 다중 객체 추적(Multiple object tracking, MOT)문제에 대한 detection framework의 구현을 제시한다. 많은 배치 기반 추적 접근과는 달리, 이 작업은 online tracking을 목표로 한다. 또한, realtime tracking을 가능하게 하고 자율 주행 자동차에서의 보행자 추적과 같은 응용 분야에서 더 큰 활용을 위한 효율성에 초점을 둔다. MOT문제는 비디오 시퀀스에서 프레임 전체에 결쳐 detection들을 연결하는 것이 목적인 data association 문제로 볼 수 있다. data association process를 지원하기 위해 tracker는 motion과 scene에서 물체의 모습을 모델링하기 위해 다양한 method를 사용한다. 이 논문이 채택한 방법은 최근에 확립 된 visual MOT benchmark 관찰을 통해 동기 부여되었다. 첫번째로 Multiple Hypothesis Tracking(MHT)와 Joint Probabilistic Data Association(JPDA)를 포함한 훌륭한 data association 기술을 부활시켰다. 두번째로 Aggregate Channel Filter(ACF)를 사용하지 않은 tracker는 상위권의 tracker이기 때문에, detection quality가 다른 detector를 방해할 수 있다는 것을 의미한다. 뿐만아니라 accuracy와 speed사이의 관계가 명확히 나타난다.
![](https://images.velog.io/images/sanha9999/post/15b2af6b-9a76-4dea-a866-606bd39832d9/image.png)

위의 그림은 여러 tracker들과 비교한 figure이다. 더 오른쪽이고 더 높은것이 좋은 것이다. SORT가 Acccuracy도 높고 Speed도 높다는 것을 알 수 있다.

상위권의 batch tracker 사이에서 전통적인 data association techniques가 부각되고 다양한 detections이 사용돠면서 이 작업은 MOT가 얼마나 단순하고 잘 수행될 수 있는지 살펴볼 수 있다. **Occam’s Razor**(오컴의 면도날, 어떤 사항을 설명하기 위한 가설의 체계는 간결해야 한다는 원리)에 따라 detection component를 벗어난 appearance features는 무시하고 data association과 motion estimation에는 bounding box position만 사용된다. 뿐만아니라 단기 및 장기 occlusion에 관한 문제는 드물게 발생하고 그것의 명시적 처리는 tracking framework에 바람직하지 않은 복잡성을 초래하기 때문에 무시된다. 또한 논문의 저자는 object를 재식별의 형태로 처리하면 tracking framework에 상당한 overhead가 추가되어 실시간 애플리케이션에서의 사용이 제한될 수 있다고 주장했다. 추가적으로 Kalman filter와 Hungarian method로 tracking에서의 motion prediction와 data association을 처리하는데 사용된다.
