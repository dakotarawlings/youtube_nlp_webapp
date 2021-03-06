
#import flask tools
from flask import Flask, jsonify, render_template, request

#Import image an file processing tools

import numpy as np
import pandas as pd
import pickle

import get_youtube_comment_data
import spacy 
#Call flask constructor

app=Flask(__name__)

#Define flask endpoint for the main html page



@app.route('/')
def index():

    return render_template('index.html')

@app.route('/youtubeVideoSentiment', methods=[ 'GET', 'POST'])

def temperatureForecast():
    
    if request.method=='POST':

        request_json=request.get_json()

        videoURL=request_json['URL']

        #monitor the success of the API through a success attribute
        response={'success': False}
        [predictions, sentimentRatio]=get_youtube_comment_data.getVideoCommentSentiments(videoURL)
        response['sentimentRatio']=sentimentRatio


    return jsonify(response)

if __name__=='__main__':
    
    app.run(debug=True)
    

