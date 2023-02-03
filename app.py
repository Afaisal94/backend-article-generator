from flask import Flask, request, jsonify, make_response
from chatgpt import get_article, get_image
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Article Genarator Using ChatGPT OpenAi"

@app.route('/articles', methods=['GET','POST'])
def articles():
    if request.method == 'POST':

        keyword = request.form.get('keyword')
        paragraph = request.form.get('paragraph')
        apikey = request.form.get('apikey')

        # Scrape Image & Content
        image = get_image(keyword)
        content = get_article(keyword, paragraph, apikey)

        # Setup Image & Content
        newImage = '<center><img src="' + image + '" alt="' + keyword + '" style="margin-top:10px; margin-bottom:10px; width:500px"></center>'
        newContent = content.replace('<br>', newImage)

        input = {
            'title': keyword,
            'image': image,
            'content': newContent
        }

        with open('articles.json', 'r+') as file:
            file_data = json.load(file)
            file_data["articles"].append(input)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        return make_response(jsonify(input)), 200

    else:

        file_json = open("articles.json")
        data = json.loads(file_json.read())

        return make_response(jsonify(data)), 200


if __name__ == '__main__':
    app.run(debug=True)

# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run