import sqlite3
import datetime
import os


def connect(username):
    database_path = os.path.join("user_data", username + ".db")
    conn = sqlite3.connect(database_path)
    conn.execute(
        f"create table if not exists {username} (date DATETIME, follower_count INTEGER, playlist_following_count TEXT, top_tracks TEXT, top_artists TEXT)"
    )
    return conn


def update(
    conn,
    username,
    date,
    follower_count,
    playlist_following_count,
    top_tracks,
    top_artists,
):
    conn.execute(
        f"insert into {username} values (?,?,?,?,?)",
        (date, follower_count, playlist_following_count, top_tracks, top_artists),
    )
    conn.commit()
    return


conn = connect("charlieoestreicher")
yea = conn.execute("select * from charlieoestreicher")
for row in yea:
    print(row)
