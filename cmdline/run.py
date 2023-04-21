import requests

def create_new_track():
    """
    Creates new track using the API
    """
    res = requests.post('http://127.0.0.1:5000/api/track', json={"track_name":"Wrecking Ball",
                                                                 "artist": "Miley Cyrus",
                                                                 "storage_location": "06-miley_cyrus-wrecking_ball.flac",
                                                                 "audio_format": "flac"})
    if res.ok:
        print(res.json())
    return 0

create_new_track()