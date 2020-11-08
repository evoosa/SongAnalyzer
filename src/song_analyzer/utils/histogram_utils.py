import pandas as pd
import matplotlib.pyplot as plt


def generate_histogram_plot_file(ratios: list, output_path: str):
    """
    Create a file containing a histogram plot for a given list of noun/adjective ratios
    :param ratios: list of integers representing noun/adjective ratios
    :param output_path: path to output the PNG to
    """
    pandas_series = pd.Series(ratios)
    fig, ax = plt.subplots()
    ax.hist(x=pandas_series, bins='auto', color='#0504aa', alpha=0.6, rwidth=0.8)

    plt.title('noun/adjective ratio for {} song lyrics'.format(len(ratios)))
    plt.xlabel('noun/adjective ratio')
    plt.ylabel('number of songs')
    plt.grid(axis='y', alpha=0.6)
    plt.savefig(output_path)
