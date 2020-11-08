# SongAnalyzer
* The SongAnalyzer package provides you scripts for analyzing song lyrics

# Important Directories
    - The lyrics are located in the 'lyrics' directory.
    - The scripts are located in the 'scripts' directory.
    - The scripts output to a directory called 'song_analyzer/script_outputs' - They'll create it if it's missing

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
    - python 3.7.9
    - Linux environment
    - run: python3 -m textblob.download_corpora

# Installation
    - pip3 install song_analyzer/src/
    OR
    - python3 setup.py install

# Usage
    ./get_song_length_stats.py <lyrics_file_path>
    ./get_song_pos_entities.py <lyrics_file_path>
    ./generate_noun_adj_ratio_hist.py
    ./get_all_songs_info.py

# What i wish i had the time to address
    - logging
    - runtime optimization - multiprocess instead of a linear run
    - memory and IO optimization
    - learning about ways to optimize the bucket count of histograms
    - handling shortened words, such as you've, we'll