import pickle

model = pickle.load(open('../model/ko.pkl','rb'))

data = {'answer':['d','d'],'user':['d','d']}

sim_list = []
for a in data['answer']:
    for u in data['user']:
        try:
            sim_list.append(model.wv.similarity(a,u))
        except:
            pass

if sim_list:
    output = round(sum(sim_list) / len(sim_list),2)
    print(output)
else:
    print('None')
#print(model.wv.similarity("강아지","고양이"))