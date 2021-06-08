def make_album(artist_name, album_title, songs_amount=None):
    if songs_amount:
        album = {'Artist': artist_name.title(), 'Album': album_title.title(), 'Songs': songs_amount}
    else:
        album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    return album

print(make_album('travis scott', 'astroworld'))
print(make_album('pop smoke', 'meet the woo 2'))
print(make_album('lil uzi vert', 'eternal atake'))
print(make_album('ariana grande', 'positions', 14))
print(make_album('lil baby', 'my turn', 35))