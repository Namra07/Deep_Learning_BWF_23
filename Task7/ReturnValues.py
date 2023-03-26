"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"""
def city_country(city, country):
    return f"{city.title()}, {country.title()}"
print(city_country('santiago', 'chile'))
print(city_country('new york', 'united states'))
print(city_country('tokyo', 'japan'))


"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album."""
def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Led Zeppelin', 'IV', 8)
album3 = make_album('Pink Floyd', 'The Wall', 26)

print(album1)
print(album2)
print(album3)


"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""
def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

while True:
    print("Enter 'q' at any time to quit.")
    artist_name = input("Enter the artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Enter the album title: ")
    if album_title == 'q':
        break
    num_tracks = input("Enter the number of tracks (optional): ")
    if num_tracks == 'q':
        break
    if num_tracks:
        album = make_album(artist_name, album_title, num_tracks)
    else:
        album = make_album(artist_name, album_title)
    print(album)



