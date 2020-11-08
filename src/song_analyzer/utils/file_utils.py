import csv
import os

from song_analyzer.config import CSV_COLUMNS
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences, get_song_length_stats


def print_file(file_path):
    """
    print the file's contents
    :param file_path: path to the file
    """
    with open(file_path, 'r') as opened_file:
        print(opened_file.read())


def create_dir_if_missing(dir_path: str):
    """
    Create directory path if doesn't exist
    :param dir_path: path to directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_lyrics_lines_from_song_file(path) -> list:
    """
    Get the lyrics from the song's file
    :return: the song's lyrics as lines
    """
    with open(path, 'r') as lyrics_file:
        return lyrics_file.readlines()


def create_gen_stats_csv(csv_path: str):
    """
    Create a CSV file with the general stats field names
    :param csv_path: path to CSV file
    """
    with open(csv_path, 'w', newline='', encoding='utf-8') as general_stats_file:
        writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
        writer.writeheader()


def update_pos_stats_file(file_path: str, song_obj):
    """
    Update POS statisitics file with new POS entities data
    if it's missing, it will be created
    :param file_path: path to the post statistics file
    :param song_obj: Song object
    :return:
    """
    with open(file_path, 'a') as pos_file:
        pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
        pos_file.write('\n-- {} --\n'.format(song_obj.metadata['name']))
        pos_file.write('\n[ NOUNS ]\n')
        [pos_file.write(noun + '\n') for noun in set(pos_entities['nouns'])]
        pos_file.write('\n[ ADJECTIVES ]\n')
        [pos_file.write(adjective + '\n') for adjective in set(pos_entities['adjectives'])]
        pos_file.write('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(pos_entities['nouns']),
                                                                          len(pos_entities['adjectives']),
                                                                          pos_entities['noun_to_adjective_ratio']))


def update_gen_stats_file(file_path: str, song_obj):
    """
    Update general statistics file with word/sentence length stats
    :param file_path: path to the post statistics file
    :param song_obj: Song object
    """
    with open(file_path, 'a', newline='', encoding='utf-8') as general_stats_file:
        len_stats = get_song_length_stats(song_obj.sentences)
        writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
        writer.writerow(len_stats)
