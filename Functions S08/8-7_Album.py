#Python script
"""
Exercise 8-7: Album
	1.	Write a function called make_album() that builds a dictionary describing a music album.
	2.	Set the parameters: The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
	3.	Test it out: Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
	4.	Add an optional parameter: Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
	5.	Update the dictionary: If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
	6.	Test the optional parameter: Make at least one new function call that includes the number of songs on an album.
"""

def make_album(artist_name, album_title, songs=None):
    """Returns artist name and album title"""
    album_info = {'artist': artist_name.title(), 'album': album_title.title()}
    if songs:
        album_info['songs'] = songs
    return album_info

disc = make_album('robe', 'destrozares', songs=12)
print(disc)

disc = make_album('the ramones', 'adios amigos')
print(disc)

disc = make_album('the clash', 'london calling')
print(disc)