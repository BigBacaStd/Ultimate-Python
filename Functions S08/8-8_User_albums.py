#Python script

"""
Exercise 8-8: User Albums
	1.	Start with your program from Exercise 8-7: You will be modifying or adding to the code you just wrote.
	2.	Create a while loop: Write a loop that prompts users to enter an album’s artist and title.
	3.	Call your function: Once you have that information from the user, call your make_album() function using the user's input.
	4.	Print the result: Print the dictionary that is created by the function to show it is working correctly.
	5.	Provide a way to quit: Be sure to include a quit value in the while loop so the user can stop entering albums when they are done.
"""

def make_album(artist_name, album_title, songs=None):
    """Returns artist name and album title"""
    album_info = {'artist': artist_name.title(), 'album': album_title.title()}

    # Bringing this back from your last exercise!
    if songs:
        album_info['songs'] = songs
    return album_info

#This is the loop!

while True:
    print("\nPlease enter artist name and album and songs #: ")
    print("(enter 'q' at any time to quit")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    alb_name = input("Album title: ")
    if alb_name == 'q':
        break

    n_songs = input("number of songs: ")
    if n_songs == 'q':
        break

    album_details = make_album(a_name, alb_name, n_songs)
    print(f"\nAlbum Info: {album_details}")