import requests
url = 'http://localhost:5000/word2vec'
r = requests.get(url, json={'answer':['w','d'],'user':['고양이','사람']})
if r:
    r = r.json()
print(r)

r = requests.get(url, json={'answer':['강아지','개구리'],'user':['고양이','사람']})
if r:
    r = r.json()
print(r)



url = 'http://localhost:5000/score'
answer = '제 취미는 영화보기에요.저는 시간있을 때 영화관에 가요. 재미있는 영화를 봐요.'
r = requests.post(url, json={'answer': answer}).json()
print(r)