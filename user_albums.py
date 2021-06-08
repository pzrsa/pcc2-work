def make_album(artist_name, album_title, songs_amount=None):
    if songs_amount:
        album = {'Artist': artist_name.title(), 'Album': album_title.title(), 'Songs': songs_amount}
    else:
        album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    return album

active = True

while active:
    print("\nPress 'q' at anytime to quit.")
    artist = input("\nType in an artist: ")
    if artist == 'q':
        break

    album = input("\nType in an album from that artist: ")
    if album == 'q':
        break

    print(make_album(artist, album))

