from song_analyzer.utils.histogram_utils import get_histogram_plot_file
from config import OUTPUT_DIR_PATH
import os
from datetime import datetime


class Artist:
    """ a Class representing a musical artist """

    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def get_noun_to_adj_ratio_hist_plot(self):
        """  Create a histogram plot PNG file for the artist's noun/ =adjective ratios """
        artist_output_dir = os.path.join(OUTPUT_DIR_PATH, self.name)
        output_file_path = os.path.join(artist_output_dir,
                                        "hist_plot-{}.png".format(datetime.now().strftime("%d-%m-%Y-%H:%M")))
        if not os.path.exists(artist_output_dir):
            os.makedirs(artist_output_dir)

        noun_to_adj_ratios = [song_obj.noun_to_adj_ratio for song_obj in self.songs]
        get_histogram_plot_file(noun_to_adj_ratios, output_file_path)
