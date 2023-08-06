from authenticate import connect_user
from send_email import send_email


def getFollowers(sp, user):
    result = sp.user(user)
    return result["followers"]["total"]


def getPlaylists(sp, user):
    playlistsInfo = {}
    for offset in range(0, 300, 50):
        result = sp.user_playlists(user, offset=offset)
        for item in result["items"]:
            playlistsInfo[item["id"]] = item
    return playlistsInfo


def getPlaylistFollowers(sp, user, playlists):
    playlistsInfo = {}
    for playlist in playlists:
        if playlist["id"] not in playlistsInfo.keys():
            playlistsInfo[playlist["id"]] = 


def run():
    scope = ""
    sp = connect_user(scope)
    user = "charlie.oestreicher"
    followers = getFollowers(sp, user)
    public_playlists = getPlaylists(sp, user)
    


run()
