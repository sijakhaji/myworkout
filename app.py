from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbmy_project


## HTML 화면 보여주기
@app.route('/')
def my_project():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/workout', methods=['POST'])
def save_workout():
    part_receive = request.form['part_give']
    part2_receive = request.form['part2_give']
    weight_receive = request.form['weight_give']
    count_receive = request.form['count_give']
    total_receive = request.form['total_give']

    print(part_receive, part2_receive, weight_receive, count_receive, total_receive)


    order = {
        'part': part_receive,
        'part2': part2_receive,
        'weight': weight_receive,
        'count': count_receive,
        'total': total_receive
    }

    db.my_project.insert_one(order)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/workout', methods=['GET'])
def view_orders():
    orders = list(db.my_project.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)