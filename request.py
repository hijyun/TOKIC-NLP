import requests
import score
# 연관성 없는 단어 API get 테스트
url = 'http://localhost:5000/word2vec'
r = requests.get(url, json={'answer':['w','d'],'user':['고양이','사람']})
if r:
    r = r.json()
print('연관성 없는 단어 API get 테스트:', r)

# 연관성 있는 단어 API get 테스트
r = requests.get(url, json={'answer':['강아지','개구리'],'user':['고양이','사람']})
if r:
    r = r.json()
print('연관성 있는 단어 API get 테스트:', r)

# PCM 리스트 전달 API get 테스트
url = 'http://localhost:5000/pcm-score'
pcm_score = score.Member_Test()
answer = '제 취미는 영화보기에요.저는 시간있을 때 영화관에 가요. 재미있는 영화를 봐요.'
audio_file = '/Users/jihyun/project/tokic/score/test/TEST1.mp3'
audio_segment = pcm_score.processing_audio(audio_file)
audioContents = pcm_score.segment(audio_segment, interval=5000)

r = requests.get(url, json={'pcm':audioContents,'answer': answer})
if r:
    r = r.json()
    print('PCM 리스트 전달 API get 테스트:', r)

# audio경로 전달 API post 테스트
url = 'http://localhost:5000/score'
pcm_score = score.Member_Test()
answer = '제 취미는 영화보기에요.저는 시간있을 때 영화관에 가요. 재미있는 영화를 봐요.'
audio_file = '/Users/jihyun/project/tokic/score/test/TEST1.mp3'

r = requests.post(url, json={'audio_path':audio_file,'answer': answer})
if r:
    r = r.json()
    print('audio경로 전달 API post 테스트:',r)