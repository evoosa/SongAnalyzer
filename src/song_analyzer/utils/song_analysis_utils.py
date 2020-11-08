from song_analyzer.song_parts.song import Song
from textblob import TextBlob


def get_pos_entities_from_sentences(sentences: list) -> dict:
    """
    Get POS entities data for a given song
    :param sentences: song's sentences
    :return: POS entities for the song
    """
    nouns = get_words_with_pos_tags(sentences, ['NN', 'NNS', 'NNP', 'NNPS'])
    adjectives = get_words_with_pos_tags(sentences, ['JJ', 'JJR', 'JJS'])
    noun_to_adj_ratio = len(nouns) / len(adjectives)
    return dict(
        nouns=nouns,
        adjectives=adjectives,
        noun_to_adjective_ratio=noun_to_adj_ratio
    )


def get_song_length_stats(sentences: list) -> dict[str, int]:
    """
    Get statistics about the min/max/average length of the sentences and words in the song
    :param sentences: list of sentences
    :return: length stats for the song
    """
    """
    ::
    :return: sentences statistics
    """
    sentences_lengths = [len(sentence.words) for sentence in sentences]
    sen_max_len = max(sentences_lengths)
    sen_min_len = min(sentences_lengths)
    sen_average_len = sum(sentences_lengths) / len(sentences_lengths)

    words_lengths = []
    for sentence in sentences:
        for word in sentence.words:
            words_lengths.append(len(word))
    word_max_len = max(words_lengths)
    word_min_len = min(words_lengths)
    word_average_len = sum(words_lengths) / len(words_lengths)
    return dict(sentence_max_len=sen_max_len,
                sentence_min_len=sen_min_len,
                sentence_average_len=sen_average_len,
                word_max_len=word_max_len,
                word_min_len=word_min_len,
                word_average_len=word_average_len)


def get_word_pos(word: str) -> str:
    """
    get the word's part of speech
    currently, there is no support for short words, such as "we'll" or "you've"
    :return: the word's POS, or an empty string if it's a shortened word
    """
    if "'" not in word:
        return TextBlob(word).tags[0][1]
    else:
        return ''


def get_words_with_pos_tags(sentences, pos_tags: list) -> list:
    """
    Get words with on of the given POS tags
    :param sentences: song's sentences
    :param pos_tags: POS tags to search songs with
    :return:
    """
    words = []
    for sentence in sentences:
        for word in sentence.words:
            word_pos = get_word_pos(word)
            if word_pos in pos_tags:
                words.append(word)
    return words
