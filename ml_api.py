from flask import Flask, jsonify, request, render_template
import recommender

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recommendations", methods = ['GET', 'POST'])
def recommend():
    name = request.args.get("name")

    if request.args.get("k"):
        k = int(request.args.get("k")) + 1
    else:
        k = None

    recommendations = recommender.get_recommendations(name, recommender.cosine_sim, k)

    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070, threaded=True, debug=True)
