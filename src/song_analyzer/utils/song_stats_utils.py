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
