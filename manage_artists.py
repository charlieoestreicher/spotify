def get_top_artists(sp):
    topArtistsInfo = {}
    artists = sp.current_user_top_artists(limit=10, time_range="short_term")["items"]
    for artist in artists:
        topArtistsInfo[artist["id"]] = [
            artist["name"],
            artist["external_urls"]["spotify"],
        ]
    return topArtistsInfo


def top_artists_to_string(topArtists):
    topArtistsString = "\n".join(
        [
            "<li>"
            + f"<a style='color:RGB(29, 185, 84)' href={each[1]}>"
            + each[0]
            + "</a>"
            + "</li>"
            for each in topArtists.values()
        ]
    )
    return topArtistsString
