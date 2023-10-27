from ytmusicapi import YTMusic
from threading import Thread
from queue import Queue


def search_tracks_youtube(tracks_chunk, queue):
    yt_music = YTMusic()
    for track in tracks_chunk:
        try:
            search_results = yt_music.search(query=track, filter='songs')
            if search_results:
                queue.put(search_results[0])
                print(f"OK {search_results[0]['title']}")
            else:
                print(f'Not Found {track}')
        except Exception as e:
            print(f"Error during searching for track {track}: {e}")


def divide_list_into_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def threaded_search(tracks, num_threads=4):
    chunk_size = max(1, len(tracks) // num_threads)
    chunks = list(divide_list_into_chunks(tracks, chunk_size))

    threads = []
    queue = Queue()
    for chunk in chunks:
        t = Thread(target=search_tracks_youtube, args=(chunk, queue))
        threads.append(t)
        t.start()
    print("step 1")

    for t in threads:
        t.join()
    print("step 2")

    results = []
    while not queue.empty():
        results.append(queue.get())
    print("step 3")

    return results
