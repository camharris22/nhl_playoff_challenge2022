import pandas as pd
import numpy as np
import os
import read_brackets as rb
from BracketEntry import BracketEntry

def get_points(save_points=True):
    entries = rb.read_brackets(save_picks=False)

    # Results by round (manually input)
    results = {
        'rd1': [
            'CGY',
            'EDM',
            'COL',
            'MIN',
            'FLA',
            'TOR',
            'CAR',
            'PIT'
        ],
        'rd2': [
            'EDM',
            'COL',
            'FLA',
            'PIT'
        ],
        'rd3': [
            'COL',
            'FLA'
        ],
        'rd4': [
            'FLA'
        ]
    }

    # Extract picks
    all_points = {}
    for entry_num, entry in entries.items():
        BracketEntry.calc_points(entry, results)
        all_points[str(entry.entrant_name) + ' ' + str(entry_num)] = entry.points

    points_df = pd.DataFrame(all_points)
    save_dir = "summary/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if save_points == True:
        points_df.to_csv(save_dir + "results_2022.csv")
        print(f"points saved in folder: {save_dir}")

    return


if __name__ == "__main__":
    get_points()