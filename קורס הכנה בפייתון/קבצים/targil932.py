def my_mp4_playlist(file_path, new_song):
	'''Gets a file with song names, the artist/s of the song and the length of the sone divided by ';'.
	Adds the new song instead of the song at line 3. If there are no songs than he is appending the new song to line 3.
	   :param file_path: The file we want to check.
	   :type file_path: str.
	   :param new_song: The new song we want to add.
	   :type new_song: str.
	   :return: The data of the file at the end.
	   :rtype: string.
	   '''
	open_file = open(file_path, 'r+')
	data = open_file.read()
	lines = data.split('\n')
	index = 0
	open_file.seek(0)
	for line in lines:
		if index == 2:
			song = line.split(';')
			song[0] = new_song
			modified_line = ';'.join(song)
			open_file.write(modified_line)
		else:
			open_file.write(line)
		open_file.write('\n')
		index += 1
	if index<2:
		open_file.write('\n' * (2-index))
		open_file.write(new_song)
	open_file.seek(0)
	data = open_file.read()
	open_file.close()
	return data
	

def main():
	print(my_mp4_playlist(r"songs.txt", "Python Love Story"))
	
if __name__ == "__main__":
	main()