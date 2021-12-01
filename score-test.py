
import time
import score

start = time.time()
from konlpy.tag import Komoran

komoran = Komoran()
answer = '제 취미는 영화보기에요.저는 시간있을 때 영화관에 가요. 재미있는 영화를 봐요.'
fname = '/Users/jihyun/project/tokic/score/test/TEST1.mp3'
# 모의고사 점수내기
member_test_score = score.Member_Test()
print(member_test_score.evaluate(fname,answer,komoran))

print("오디오 채점 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


start = time.time()
audio_segment = member_test_score.processing_audio(fname)
audioContents = member_test_score.segment(audio_segment, interval=5000)
print(member_test_score.pcm_evaluate(audio_segment, audioContents,answer,komoran))
print("pcm 채점 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간