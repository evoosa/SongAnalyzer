from song_analyzer.song_parts.song import Song
import argparse


def get_argument_parser(): # FIXME - add typesssss
    """ Create the argument parser for the scripts """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--song_path',
                        type=str,
                        help="song's path")
    return parser


def count_words_with_pos_tags(song_obj, pos_tags: list) -> int: # TODO - try to get rid of it????????
    """
    Count the number of words in the song with one of the given POS tags
    :param song_obj: Song object
    :param pos_tags: POS tags to search songs with
    :return: number of words with POS tags
    """
    count = 0
    for sentence in song_obj.sentences:
        for word in sentence.words:
            if word.pos in pos_tags:
                count += 1
    return count


def get_words_with_pos_tags(song_obj, pos_tags: list) -> set: # FIXME to set????????????
    """
    Get words with on of the given POS tags
    :param song_obj: Song object
    :param pos_tags: POS tags to search songs with
    :return:
    """
    words = []
    for sentence in song_obj.sentences:
        for word in sentence.words:
            if word.pos in pos_tags:
                words.append(word.data)
    return set(words)


def get_sentence_length_stats(song_obj) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the sentences in the song
    :return: sentences statistics
    """
    sentences_lengths = [len(sentence.words) for sentence in song_obj.sentences]
    max_len = max(sentences_lengths)
    min_len = min(sentences_lengths)
    average_len = sum(sentences_lengths) / len(sentences_lengths)
    return dict(sentence_max_len=max_len, sentence_min_len=min_len, sentence_average_len=average_len)


def get_word_length_stats(song_obj) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the words in the song
    :return: words statistics
    """
    words_lengths = []
    for sentence in song_obj.sentences:
        for word in sentence.words:
            words_lengths.append(len(word.data))
    max_len = max(words_lengths)
    min_len = min(words_lengths)
    average_len = sum(words_lengths) / len(words_lengths)
    return dict(word_max_len=max_len, word_min_len=min_len, word_average_len=average_len)

    # FIXME - should i set the nouns and adjectives, remove duplicates? should they be unique?
    # FIXME - should i leagel? (sentences/words avg, and noun/adjs ratio)
