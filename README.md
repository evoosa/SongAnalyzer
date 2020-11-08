# SongAnalyzer
* The SongAnalyzer package provides you scripts for analyzing song lyrics

# Important Directories
    - The lyrics are located in the 'lyrics' directory.
    - The scripts are located in the 'scripts' directory.

# Scripts
    * get_song_length_stats.py <lyrics_file_path>
        - generates stats of the word and sentence length for a given song.

    * get_song_pos_entities.py <lyrics_file_path>
        - generates Part Of Speech data for a given song (nouns, adjectives, noun/adjective ratio).

    * generate_noun_adj_ratio_hist.py
        - generates a histogram PNG file, from the noun/adjective ratios of all the songs in the lyrics directory.

    * get_all_songs_info.py
        fo each artist, generates:
        - a histogram of the noun/adjective ratio of it's songs.
        - a CSV file containing stats of the word and sentence length for each song.
        - a TXT file containing Part Of Speech data for each song (nouns, adjectives, noun/adjective ratio).

# Requirements
    - python 3.9
    - Windows or Linux environment

# Installation
    - cd to src/
    - pip3.9 install -e ./
    OR
    - python3.9 setup.py install

# Usage
    - python3.9 get_song_length_stats.py <lyrics_file_path>