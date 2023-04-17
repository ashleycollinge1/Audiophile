https://audiophile.com/api/<username>/playlists/

/api

HTTP POST /api/search
{"search query": "Enrique", "filter": "}
[

]


/api/album/*

HTTP DELETE /api/album/34924

HTTP CREATE /api/album
{"name"

{"status": "okay",
"albumId": "344",
"uri": /api/album/344


/api/album/<album_id>
/api/song
/api/user
/api/

[
	{"Playlist-name": "Playlist1",
	 "URI": "/api/<username>/playlist1},
	{"Playlist-name": "Playlist2",
	 "URI": "/api/<username>/playlist2},
]

https://audiophile.com/api/<username>/playlist1

Link to the music
Music name
Artist
Album art

1) download the album ar, and display
2) display the artist, name
3) pass link to audio file to audio player 
4) start playing 



/api/<username>/playlists

{"name": "playlist1",
"URI": "/api/playlists/2480538"}

/api/playlists/2480538 GET

{"Name": "Playlist1",
"duration": "454",
[{"song_id": 2453, "URI": /api/song/2453}
"song_id": 3330, "URI": /api/song/3330}

/api/song/2453 GET
{"song name": "name",
"duration": 23,
"album art": /api/album/43095/art.png,
"lyrics": /api/song/2453/lyrics
"comments": /api/song/2453/comments


/api/song/2453/comments GET
[
  "timestamp": <time>,
  "username": 310849,
  "text": " fsuehfoajwfdbilawhikh"
]

/api/song/2453/comments POST
[
  "timestamp": <time>,
  "username": 310849,
  "text": " fsuehfoajwfdbilawhikh"
]

{"status": "success", "message": "Added comment to song 248"}

Direct play
Streaming



/api/<username>/playlists/playlist1

[list of song ids (basic)]

/api/song/id

return all informatino referencing song
name duration tags album reference
album_id=2342

/api/album/<id>

## How are we going to import audio into the system?
https://discogs-data-dumps.s3.us-west-2.amazonaws.com/index.html?prefix=data/2023/
Data dumps of new artists/albums etc - lot of data though to store ~100s gbs
Requests are throttled by the server by source IP to 60 per minute for authenticated requests, and 25 per minute for unauthenticated requests, with some exceptions.

https://www.discogs.com/developers

Example request

    curl https://api.discogs.com/releases/249504 --user-agent "Audiophile/0.0.1a"

curl https://api.discogs.com/database/search?artist="Elton John" --user-agent "Audiophile/0.0.1a"

Must set user agent otherwise will get a blank response, or silently blocked. User agent lets
them see who is connecting and what they're doing.

### Authentication for Discogs.com

https://www.discogs.com/developers#page:authentication,header:authentication-discogs-auth-flow

Setup OAuth flow, whereby user must click a link in Audiophile, which takes them to discogs to authorise the app in their account (they must create an account), then Audiophile utilises their
account to do all of the API requests. Somewhat complicated to do right now...


Headers are provided on responses (below) for request rates

X-Discogs-Ratelimit: The total number of requests you can make in a one minute window.

X-Discogs-Ratelimit-Used : The number of requests you’ve made in your existing rate limit window.

X-Discogs-Ratelimit-Remaining: The number of remaining requests you are able to make in the existing rate limit window.

Spotify, Deezer all used apis which require an account, so does change the dynamic slightly

We ought to prioritise free and easily accessible APIs over account req/paid APIs

## Last.FM API

Similar setup to OAuth workflow, we use the user's account to authorise the API requests

https://www.last.fm/api/webauth