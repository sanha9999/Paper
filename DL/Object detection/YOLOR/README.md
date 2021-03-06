## YOLOR이란?
YOLOR의 제목은 "You Only Learn One Representation: Unified Network for Multiple Tasks"이다. 해석하면 "한가지 표현만 배워라 : 여러 작업을 위한 통합적 네트워크"이지 않을까 싶다.

## Abstract
사람들은 시각, 청각, 촉각 그리고 과거의 경험을 통해 세상을 이해한다. 그리고 인간의 경험은 일반적인 학습(이걸 우리는 **Explict knowledge, 명시적 지식**이라고 부른다)을 통하거나 또는 잠재의식적(**Implicit knowledge**, 암묵적 지식)으로 학습할 수 있다. 이런 경험들은 일반적이거나 잠재적인 학습을 통해 뇌에 암호화되어 저장된다. 이런 풍부한 경험을 거대한 database로 쌓아 인간은 심지어 보이지 않는 것에 대해서도 효과적으로 데이터를 처리할 수 있다. 이 논문에서는, 인간의 뇌가 지식을 일반/잠재적 학습을 통해 배우는 것처럼 명시적 지식과 암묵적 지식을 함께 인코딩하는 통합된 네트워크를 제안한다. 이 네트워크는 다양한 작업을 동시에 처리하기 위해 통일된 표현을 생성할 수 있다. 우리는 컨볼루션 신경망에서 커널 공간 정렬, 예측 개선 및 다중 작업 학습을 수행할 수 있다. 결과는 암묵적 지식이 신경망에 도입되면 모든 작업의 성능에 도움이 된다는 것을 보여준다. 제안한 통합 네트워크에서는 학습된 **암묵적 표현**을 추가로 분석하고, 다양한 작업의 물질적 의미를 파악하는 데 큰 기능을 보여준다.

요약하자면 인간이 살아갈때 사물을 명시적으로 배우는 것 뿐만아니라 경험을 통해서 암묵적 지식도 쌓게 되는데, 이러한 방식을 신경망에도 적용한다는 말인 것 같다.

## Figure

![](https://images.velog.io/images/sanha9999/post/3ddc6e7b-909e-4532-85ba-8ab96e9e923c/image.png)

위의 강아지사진을 보고 사람은 여러가지 질문에 답을 할 수 있다. 예를 들면 이 개의 이름이 무엇인지, 무슨 종류인지, 무슨 행동을 하는가? 같은 질문말이다. 이 논문의 저자도 하나의 input에서 많은 작업을 수행할 수 있는 네트워크를 만들고자 하였다.

![](https://images.velog.io/images/sanha9999/post/420148b4-b0c8-479a-939f-300a4c3e1382/image.png)

(c)가 논문에서 명시적 지식과 암묵적 지식을 가진, 여러 작업을 수행하기 위한 네트워크이다.

![](https://images.velog.io/images/sanha9999/post/17aea132-496e-400a-8e9b-0aca49fa2afb/image.png)

Manifold space(매니폴드 공간)이라는 것이 있다. 이것에 대해서는 [이 글](https://kh-mo.github.io/notation/2019/03/10/manifold_learning/)에 자세히 나와있다. 그래서 이 논문의 저자는 good representation은 manifold space에서 적절한 projection을 찾을수있다고 한다. 그리고 이 projection을 사용하여 목표로 하는 일을 성공적으로 수행한다. 예를 들어 위의 그림에서와 같이 target이 projection space에서 hyperplane으로 성공적으로 분류된다면 그것이 가장 좋은 결과일 것이라고 하였다.

![](https://images.velog.io/images/sanha9999/post/4ff19110-0784-4056-9579-6586112bb350/image.png)
