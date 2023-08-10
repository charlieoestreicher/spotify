def get_top_tracks(sp):
    topTracksInfo = {}
    tracks = sp.current_user_top_tracks(limit=10)["items"]
    for track in tracks:
        external_url = track["external_urls"]["spotify"]
        artists = [item["name"] for item in track["artists"]]
        topTracksInfo[track["id"]] = [track["name"], artists, external_url]
    return topTracksInfo


def top_tracks_to_string(topTracks):
    topTracksString = "\n".join(
        [
            "<li>"
            + f"<a style='color:RGB(29, 185, 84)' href={each[2]}>"
            + each[0]
            + "</a>"
            + " by "
            + "and ".join([artist for artist in each[1]])
            + "</li>"
            for each in topTracks.values()
        ]
    )
    return topTracksString
