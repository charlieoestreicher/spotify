def get_followers(sp, user):
    result = sp.user(user)
    return result["followers"]["total"]


def get_playlist_followers(sp, user):
    playlistsInfo = {}
    offset = 0
    while True:
        result = sp.user_playlists(user, offset=offset)
        for item in result["items"]:
            playlistId = item["id"]
            playlistObject = sp.playlist(playlistId)
            playlistFollowers = playlistObject["followers"]["total"]
            playlistsInfo[item["id"]] = playlistFollowers
        if len(result["items"]) < 50:
            break
        offset += 50
    return playlistsInfo
