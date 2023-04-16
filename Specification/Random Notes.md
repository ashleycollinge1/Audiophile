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