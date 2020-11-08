import matplotlib.pyplot as plt
import pandas as pd

from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences


def generate_histogram_plot_file(ratios: list, output_path: str):
    """
    Create a file containing a histogram plot for a given list of noun/adjective ratios
    :param ratios: list of noun/adjective ratios
    :param output_path: path of the output histogram PNG file
    """
    pandas_series = pd.Series(ratios)
    fig, ax = plt.subplots()
    ax.hist(x=pandas_series, bins='auto', color='#0504aa', alpha=0.6, rwidth=0.8)

    plt.title('noun/adjective ratio for {} song lyrics'.format(len(ratios)))
    plt.xlabel('noun/adjective ratio')
    plt.ylabel('number of songs')
    plt.grid(axis='y', alpha=0.6)
    plt.savefig(output_path)

def gen_hist_plot_from_songs(output_path: str, songs):
    """
    Generate a histogram of noun/adjective ratios for a list of songs
    :param output_path: path of the histogram plot file
    :param songs: Song objects
    """
    noun_to_adj_ratios = []
    for song_obj in songs:
        song_pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
        noun_to_adj_ratios.append(song_pos_entities['noun_to_adjective_ratio'])
    generate_histogram_plot_file(noun_to_adj_ratios, output_path)