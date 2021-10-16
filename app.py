from flask import Flask, jsonify

from fetch import fetch

app = Flask(__name__)


@app.route("/<profile>")
def profile_load(profile):
    res = fetch(profile)
    response = jsonify({'xp':res[0],'level':res[1],'following':res[2],'followers':res[3],'name':res[4],'country':res[5],'courses':res[6],'codes':res[7],'id':profile})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/")
def index():
    response = jsonify({'get':'success'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/favicon.ico') 
def favicon(): 
    return '' # send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
