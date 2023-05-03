def my_mp3_playlist(file_path):
	'''Gets a file with song names, the artist/s of the song and the length of the sone divided by ';'.
	Finds the longest song name, the amount of songs in the file and the most common artist/s.
	   :param file_path: The file we want to check.
	   :type file_path: str.
	   :return: A tuple of the things we find.
	   :rtype: tuple.
	   '''
	open_file = open(file_path, 'r')
	longest_song = ""
	longest_song_length = 0.0
	count_songs = 0
	artists_dict = {}
	for line in open_file:
		count_songs += 1
		song = line.split(';')
		if float(song[2].replace(':','.')) > longest_song_length:
			longest_song = song[0]
			longest_song_length = float(song[2].replace(':','.'))
		if song[1] in artists_dict.keys():
			artists_dict[song[1]] += 1
		else:
			artists_dict[song[1]] = 1
	result = (longest_song, count_songs, sorted(artists_dict, key = artists_dict.get)[-1])
	open_file.close()
	return result
	

def main():
	print(my_mp3_playlist(r"songs.txt"))
	
if __name__ == "__main__":
	main()