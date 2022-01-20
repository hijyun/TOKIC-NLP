# TOKIC - 한국어 회화 연습 및 평가 앱 개발 프로젝트
## 📖  상세 내용
> 한이음ICT멘토링에서 활동하며 진행한 프로젝트입니다. 비대면 한국어 회화 시험 연습용 안드로이드 앱입니다. 오픽 시험의 응시료가 비싼 이유는 사람이 직접 회화 능력을 채점하기 때문입니다. 시·공간의 제약이 없는 학습 환경에서 사용자에게 구체적인 평가 지표를 제공할 수 있다면 회화 학습에 비용을 절감할 수 있어 효율적인 학습이 가능합니다. 따라서 한국어 회화 능력을 평가하는 알고리즘과 개인의 취약점을 보완할 수 있는 비대면 학습 플랫폼을 제시하였습니다. 또한, 사용자가 한국어 회화 시험을 연습할 수 있도록 자동 빈칸 생성, 문장 순서대로 배열하기 등의 학습 모듈을 지원합니다.

<br>
<div align="center">
<img width="500" alt="서비스구성도" src="https://user-images.githubusercontent.com/54613024/150270729-4b27ca16-ecb0-4253-8553-81af4b7ab7a4.png">
</div>
<br>

* 채점 알고리즘은 클라이언트로부터 받은 사용자의 한국어 회화 능력을 평가합니다.
* 음성을 인식한 후 자연어 처리 기술을 통해 사용자의 표현력, 유창성, 문장의 적절성, 발음, 모범답안과의 유사도를 측정합니다.
* 해당 알고리즘은 사용자 음성 파일을 전달받은 후 음성을 1 m/s 단위로 분해하여 유창성을 평가하고, 음성의 원시 데이터를 추출하여 발음 평가 API 로 전달합니다.

<br>

## 🗺  서비스 구성도
<div align="center">
<img width="700" alt="서비스구성도" src="https://user-images.githubusercontent.com/54613024/150285187-cb4b5348-e99e-4343-b5f9-27612b6614b9.png">

</div>

<br>

## 채점 알고리즘 
<div align="center">
<img width="400" alt="서비스구성도" src="https://user-images.githubusercontent.com/54613024/150265223-eb75ccb6-05e3-4fbc-89e2-11596ef20a5d.png">
</div>

1. **유창성** : dBFS 가 -80 보다 작은 경우를 정적 구간으로 계산. 정적으로 측정된 구간이 답안 전체의 1/3 이하인 경우 만점으로 채점하고, 1/3 초과인 경우부터 감점하여 유창성 점수를 산출.
2. **발음** : ETRI 발음 평가 API를 이용하여 사용자의 발음 평가 점수와 음성 인식 결과 텍스트를 반환받음. 음성 인식 텍스트에 대하여 KoNLPy 한국어 형태소 분석기를 사용하여 토큰화.
3. **표현력** : 사용자 답안의 문장의 길이, 사용한 단어의 수, 5 초 당 평균 사용 단어 수를 측정한 뒤 모범답안과 비교.
4. **모범 답안 유사도** : 토큰화 된 문장을 벡터화하고 모범답안과 사용자의 답안의 코사인유사도 거리를 계산.
5. **주제의 연관성** : 사전에 학습한 Word2Vec 모델을 사용해 사용자의 답변에서 얻어낸 키워드와 모범답안의 키워드간 거리를 계산.
<br>

## 채점 알고리즘 사용법
```
$ git clone https://github.com/TOKIC-test/Tokic_NLP.git
$ pip install -r requirements.txt
$ cd Tokic_NLP
$ flask run
```

```python
import requests
import score


url = 'http://localhost:5000/score'
pcm_score = score.Member_Test()
answer = '모범답안 script를 작성해주세요.' # 모범 답안 script
audio_file = '/Users/audio_file.mp3' # audio경로를 전달

r = requests.post(url, json={'audio_path':audio_file,'answer': answer})
if r:
    r = r.json()
    print('test점수 결과 : ',r)
```
<br>

## 관련 문서  
[한이음 한국정보처리학회 2021 추계학술대회 논문](https://www.koreascience.or.kr/article/CFKO202133648924945.page)
<br>
