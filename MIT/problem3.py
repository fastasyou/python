def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    mysize = 0
    songs_copy = songs.copy()
    if len(songs_copy) > 0:
    	song = songs_copy[0]
    	if song[2] > max_size:
    		return []
    	else:
    		playlist.append(song[0])
    		mysize = song[2]
    		del songs_copy[0]
    		while len(songs_copy) > 0:
    			smallest = max_size
    			index = 0
    			for i in range(len(songs_copy)):
    				song = songs_copy[i]
    				if smallest > song[2]:
    					smallest = song[2]
    					index = i
    			if mysize + smallest <= max_size:
    				playlist.append(songs_copy[index][0])
    				mysize += smallest
    				del songs_copy[index]
    			else:
    				break
    return playlist

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
# print(song_playlist(songs, 12.2))
# print(song_playlist(songs, 11))
print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 5.4))