from fastapi import FastAPI
from pydantic import BaseModel
from model import Spotify_Recommendation  # Importing recommendation model
import numpy as np
import pandas as pd
import json

class SongRequest(BaseModel):
    s_name: str

app = FastAPI()


sdf = pd.read_csv("SpotifySongs.csv")
recommendations = Spotify_Recommendation(sdf)
@app.get('/')
def com():
    return "working"

@app.post('/recommend')
def rec(song_request: SongRequest):
    song_name = song_request.s_name

    if song_name:
        recommended_songs, album_cvr = recommendations.recommend(song_name)
        response = {
            "recommended_songs": recommended_songs,
            "album_covers": album_cvr
        }
    else:
        response = {"error": "Unknown song name"}

    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
from fastapi import FastAPI
from pydantic import BaseModel
import json
from model import Spotify_Recommendation  # Importing recommendation model
import numpy as np
import pandas as pd


class item(BaseModel):
    s_name: str
  
    
app = FastAPI()

sdf = pd.read_csv("SpotifySongs.csv")
recommendations = Spotify_Recommendation(sdf)




@app.post('/recommend')
def rec():
    with open('u_input.json','r') as input_file:
        input_data = json.load(input_file)

    song_name = input_data.get('s_name')

    if song_name:
        recommended_songs,album_cvr = recommendations.recommend(song_name)
        response = recommended_songs
    else:
        response = "Unknown song name"
    
    with open('u_output.json','w') as output_file:
        json.dump(response,output_file)
    
    with open('albm_cvr.json','w') as cvr_file:
        json.dump(album_cvr,cvr_file)

        
        

"""

