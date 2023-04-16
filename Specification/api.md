# API Specification

## Workflows

### Import music to application
To import music into the application we will need to look at the metadata and filenames to
try and work out what the tracks are. All tracks must be on an album (even a single, same name is used),
therefore to add tracks, we need an ALBUM, an ARTIST, and a TRACK

1. Create a new ARTIST using the API:

    CREATE /api/artist
    {
        "artist_name": string:<artist_name>,
    }

2. Create a new ALBUM for that ARTIST using the API:
    CREATE /api/album
    {
        "artist_id": string:<artist_id>,
        "album_name": string:<album_name>,
    }

3. Create a new TRACK for each track, and associate the TRACK to the ALBUM using the API:
    CREATE /api/track

    UPDATE /api/album



TODO
album /api/album
artist /api/artist

GET /api/track/<track_id>
Returns track information for a particular track, ID in url

Return Message:
{
    "track_id": integer:<track_id>,
    "track_name": string:<track_name>,
    "track_duration": datetime:<track_duration>,
    "track_uri": string:<track_uri>,
    "track_album": [ string:<track_album>, ],
    "track_artist": [ string:<track_artist>, ],
    "track_genre": string:<track_genre>,
    "track_length": datetime:<track_length>,
    "global_listens": integer:<global_listens>,
    "track_rating": integer:<track_rating>,
    "track_art": string:<album_art_uri>,
    "release_date": datetime:<track_release_date>,
    "track_credits": {
        "performed_by": string:<performed_by>,
        "written_by": string:<written_by>,
        "produced_by": string:<produced_by>,
        "source": "Musical Freedom",
    }
}

GET /api/<user_id>/playlist
Returns a list of user's playlists, public and private.

Return message:
{
    "username": string:<username>,
    "user_id": integer:<user_id>,
    "user_uri": string:<user_uri>
    "playlists": [
        {
            "playlist_id": integer:<playlist_id>,
            "playlist_uri": string:<playlist_uri>,
            "name": string:<playlist_name>,
            "creator": integer:<user_id_of_creator,
            "private": Bool:<private_bool>
        },
    ]
}

GET /api/<user_id>/playlist/<playlist_id
Returns a playlist object with the track listing.

Return message:
{
    "playlist_id": integer:<playlist_id>,
    "playlist_duration": datetime:<playlist_duration>,
    "private": bool:<private>,
    "date_created": datetime:<date_created>,
    "date_last_modified": datetime:<date_last_modified>,
    "shared_with": [ integer:<user_id>, ],
    "creator": integer:<user_id>,
    "track_listing": [
        {
            "track_id": integer:<track_id>,
            "track_uri": string:<track_uri>,
        },
    ]
}


GET /api
Return Message:

{"Version": <API_version_number}

------------------------------------

POST /api/album

Data:
{"": ""}

Return Message:
{"Status": "Success"}