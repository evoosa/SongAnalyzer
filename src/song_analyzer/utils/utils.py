from song_analyzer.song_parts.song import Song
from song_analyzer.utils.song_stats_utils import get_sentence_length_stats, get_word_length_stats


def get_song_pos_entities(lyrics_path: str):
    song_obj = Song(lyrics_path)
    return {
        'nouns': song_obj.nouns,
        'adjectives': song_obj.adjectives,
        'noun_to_adjective_ratio': song_obj.noun_to_adj_ratio
    }

def get_song_length_stats(lyrics_path: str):
    song_obj = Song(lyrics_path)
    sentence_stats = get_sentence_length_stats(song_obj)
    words_stats = get_word_length_stats(song_obj)
    return {
        'sentence_stats': sentence_stats,
        'word_stats': words_stats
    }


