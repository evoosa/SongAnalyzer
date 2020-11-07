import pandas as pd
import matplotlib.pyplot as plt


def get_histogram_plot_file(ratios: list, output_path: str):
    """
    Create a file containing a histogram plot for a given list of noun/adjective ratios
    :param ratios: list of integers representing noun/adjective ratios
    :param output_path: path to output the PNG to
    """
    pandas_series = pd.Series(ratios)
    plt.hist(x=pandas_series, bins='auto', color='#0504aa', alpha=0.6, rwidth=0.8)
    plt.title('noun/adjective ratio for {} song lyrics'.format(len(ratios)))
    plt.xlabel('noun/adjective ratio')
    plt.ylabel('number of songs')
    plt.grid(axis='y', alpha=0.6)
    plt.savefig(output_path)

ratios = [5.333333333333333, 10.285714285714286, 3.8461538461538463, 5.375, 9.333333333333334, 9.416666666666666, 6.05, 6.4375, 8.833333333333334, 14.333333333333334]
get_histogram_plot_file(ratios, 'abc.png')
