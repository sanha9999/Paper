논문의 제목은 "SIMPLE ONLINE AND REALTIME TRACKING", 줄여서 SORT로 트래킹 알고리즘중 하나이다.

## ABSTRACT
본 논문은 온라인과 실시간 application을 위해 객체를 효과적으로 연결하는 것이 focus인 multiple object tracking에 대한 실용적인 접근 방식을 탐구한다. 이를 위해 detection quality는 tracking performance를 위한 핵심 요소로 여겨지며, detector를 변경하면 tracking performance를 최대 18.9%까지 향상할 수 있다. 칼만 필터(Kalman Filter)와 헝가리안 알고리즘(Hungarian algorithm)같은 친숙한 기술의 조합만 사용함에도 불구하고, 이 접근은  SOTA(state-of-the-art)에 버금가는 정확도를 달성했다. 뿐만 아니라, 우리의 tracking method는 간단하기 때문에 다른 SOTA tracker보다 20배 이상 빠른 260Hz의 속도로 업데이트된다.

## INTRODUCTION
![](https://images.velog.io/images/sanha9999/post/15b2af6b-9a76-4dea-a866-606bd39832d9/image.png)

위의 그림은 여러 tracker들과 비교한 figure이다. 더 오른쪽이고 더 높은것이 좋은 것이다. SORT가 Acccuracy도 높고 Speed도 높다는 것을 알 수 있다.
