from flask import Flask, jsonify
import userRatingModule
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return 'Connected'

@app.route('/top/<topName>/bottom/<bottomName>/shoes/<shoesName>')
def user(topName, bottomName, shoesName):
    temp = userRatingModule.userRating(topName, bottomName, shoesName)
    # temp = temp.to_dict()
    # return str(temp)
    print(type(jsonify(temp)))
    # return jsonify(temp)
    return temp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(5000))

