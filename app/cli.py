import click, requests, os


def register(app):
    @app.cli.group()
    def track():
        """Track resources and commands through the API."""
        pass

    @track.command()
    def create_track():
        """
        This creates a new track
        """
        res = requests.post('http://127.0.0.1:5000/api/track', json={"track_name":"Wrecking Ball",
                                                                "artist": "Miley Cyrus",
                                                                "storage_location": "06-miley_cyrus-wrecking_ball.flac",
                                                                "audio_format": "flac"})
        if res.ok:
            print(res.json())
        return 0

    @track.command()
    def get_tracks():
        """
        Get all tracks
        """
        res = requests.get('http://127.0.0.1:5000/api/track')
        if res.ok:
            print(res.json())
        return 0