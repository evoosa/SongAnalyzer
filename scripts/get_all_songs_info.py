import os
from song_analyzer.config import BASE_DIR, LYRICS_DIR, SCRIPT_OUTPUTS_DIR
from song_analyzer.song_parts.song import Song
from song_analyzer.song_parts.artist import Artist

if __name__ == '__main__':  # TODO - verbosity!!
    lyrics_dir = os.path.join(BASE_DIR, LYRICS_DIR)
    output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR)

    print('\n[ Getting all songs info.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]
    song_objects = [Song(lyrics) for lyrics in lyrics_files]

    artist_objects = {}
    for song_obj in song_objects:
        # Get Artist object
        artist_name = song_obj.metadata['artist']
        artist_output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR, artist_name)

        if not os.path.exists(artist_output_dir):
            os.makedirs(artist_output_dir)

        if artist_name not in artist_objects.keys():
            artist_objects[artist_name] = Artist(artist_name)

        artist_objects[artist_name].songs.append(song_obj)

        # Get POS entities for song

