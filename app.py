from flask import Flask, request, jsonify
import pickle
from konlpy.tag import Komoran
import score
app = Flask(__name__)
model = pickle.load(open('model/ko.pkl','rb'))
komoran = Komoran()

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/word2vec', methods=['GET'])
def sim_score():
    data = request.get_json(force=True)

    sim_list = []
    for a in data['answer']:
        for u in data['user']:
            try:
                sim_list.append(model.wv.similarity(a, u))
            except:
                pass
    if sim_list:
        output = int(sum(sim_list) / len(sim_list) * 100)
        return jsonify(output)
    else:
        return None

@app.route('/score', methods=['POST'])
def hello_post():
    data = request.get_json(force=True)
    fname = '/Users/jihyun/project/tokic/score/test/TEST1.mp3'
    member_test_score = score.Member_Test()
    output = member_test_score.evaluate(fname,data['answer'],komoran)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
