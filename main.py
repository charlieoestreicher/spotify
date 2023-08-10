from authenticate import connect_user
from send_email import send_email
from manage_tracks import get_top_tracks, top_tracks_to_string
from manage_artists import get_top_artists, top_artists_to_string
from manage_followers import get_followers, get_playlist_followers
from manage_data import update, connect
import datetime
import json


def getFollowers(sp, user):
    result = sp.user(user)
    return result["followers"]["total"]


def getPlaylists(sp, user):
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


def notify(followers, public_playlists, topTracks, topArtists, user):
    subject = "Some Peronsal Spotify Statistics"
    topTracksString = top_tracks_to_string(topTracks)
    topArtistsString = top_artists_to_string(topArtists)
    body = (
        f"<div>Hey there {user},<div>"
        f"<div>You currently have {followers} followers</div>"
        + f"<div>A cumulative sum of {sum(list(public_playlists.values()))} people follow your public playlists </div>"
        + f"<div>Your top tracks over the last 4 weeks are:\n <ul>{topTracksString}</ul>\n</div>"
        + f"<div>Your top artists over the last 4 weeks are:\n <ul>{topArtistsString}</ul></div>"
    )
    sender = "charlie.oestreicher@gmail.com"
    recipients = ["charles.oestreicher@duke.edu"]
    password = "ynzxdyiuxgzaxffe"
    send_email(subject, body, sender, recipients, password)


def run():
    scope = ""
    sp = connect_user(scope)
    user = "charlie.oestreicher"
    top_tracks = get_top_tracks(sp)
    top_artists = get_top_artists(sp)
    followers = get_followers(sp, user)
    # playlist_followers = get_playlist_followers(sp, user)
    playlist_followers = {"key": 10}
    username = "".join(char for char in user if char.isalpha()).lower()
    print(type(followers))
    print(json.dumps(playlist_followers))
    print(json.dumps(top_tracks))
    print(json.dumps(top_artists))
    conn = connect(username)
    update(
        conn,
        username,
        datetime.datetime.today(),
        followers,
        json.dumps(playlist_followers),
        json.dumps(top_tracks),
        json.dumps(top_artists),
    )
    notify(followers, playlist_followers, top_tracks, top_artists, user)


run()
