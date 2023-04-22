from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(300), index=True)
    artist = db.Column(db.String(300))
    storage_location = db.Column(db.String(500))
    audio_format = db.Column(db.String(15))
    
    def __repr__(self):
        return '<Track {0} {1}>'.format(self.track_name, self.artist)

    def serialize(self):
        """
        Custom method used within api to serialize database objects into
        JSON.
        """
        return {
            'id': self.id,
            'track_name': self.track_name,
            'artist': self.artist,
            'storage_location': self.storage_location,
            'audio_format': self.audio_format,
        }


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<User {0}>'.format(self.name)

    def serialize(self):
        """
        Custom method used within api to serialize database objects into
        JSON.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }