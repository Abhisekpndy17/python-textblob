from flask import Flask, render_template, request, url_for, flash

#for NLP
from textblob import TextBlob, Word
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghhgwieweheyen373bheud'

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/analyse', methods=['POST'])
def analyse():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        #NLP stuff
        blob = TextBlob(rawtext)
        recieve_text2 = blob
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        number_of_token = len(list(blob.words))

    return render_template('analyse.html', 
                             recieve_text = recieve_text2,
                             number_of_token= number_of_token,
                             blob_subjectivity=blob_subjectivity,
                             blob_sentiment=blob_sentiment
                             )



if __name__ == '__main__':
    app.run(debug=True)