import json
import sys
from ytmusicapi import YTMusic
from threading import Thread
from Youtube import divide_list_into_chunks
from Youtube import threaded_search


def save_results_to_file(results, file_name):
    with open(file_name, 'w') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)


def read_saved_tracks(file_path):
    with open(file_path, 'r') as file:
        tracks = [line.strip() for line in file]
    return tracks


def main():
    print("Starting...")
    run_type = sys.argv[1]
    match run_type:
        case "Ex-Sp":
            print("Exporting Spotify data...")
            export_spotify()
            print("Exported Spotify data.")
        case "Im-You":
            print("Importing Youtube data...")
            import_youtube_with_data()
            print("Imported Youtube data.")
        case _:
            print("Invalid type, please use one of the following: Export Spotify(Ex-Sp), Import YouTube(Im-You)")
            exit()


def export_spotify():
    tracks = read_saved_tracks('saved_tracks.txt')
    youtube_results = threaded_search(tracks, 100)
    save_results_to_file(youtube_results, 'youtube_search_results.json')
    print("Exported Spotify data.")


def import_youtube_with_data():
    with open('youtube_search_results.json', 'r') as file:
        data = json.load(file)
    print(len(data))
    id_list = [item["videoId"] for item in data]
    yt_music = YTMusic("oauth.json")
    play_lists = yt_music.get_library_playlists()
    test_play_list = next((playlist for playlist in play_lists if playlist["title"] == "LikedSpotifyX"), None)
    if test_play_list is None:
        play_list_id = yt_music.create_playlist("LikedSpotifyX", "Liked Spotify Songs X")
    else:
        play_list_id = test_play_list['playlistId']
    # threaded_add_youtube(id_list, yt_music, play_list_id)
    for x in id_list:
        add_youtube(id_list, yt_music, play_list_id)

    print("Imported Youtube data.")


def add_youtube(id_list, yt_music, play_list_id):
    for chunk in id_list:
        try:
            yt_music.add_playlist_items(play_list_id, [chunk], None, duplicates=True)
            print(f"{chunk} added..")
        except Exception as ex:
            print(f"{chunk} > Error:  {ex}")


def threaded_add_youtube(id_list, yt_music, play_list_id):
    num_threads = 20
    chunk_size = max(1, len(id_list) // num_threads)
    chunks = list(divide_list_into_chunks(id_list, chunk_size))

    threads = []
    for chunk in chunks:
        t = Thread(target=add_youtube, args=(chunk, yt_music, play_list_id))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
