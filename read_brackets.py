import pandas as pd
import numpy as np
import os
from BracketEntry import BracketEntry

def read_brackets(save_picks=True):
    brackets = os.listdir('brackets')
    entries = {}

    # Initialize entries
    for n, bracket in enumerate(brackets):
        entries[str(n+1)] = BracketEntry(bracket)

    # Extract picks
    all_picks = {}
    for entry_num, entry in entries.items():
        BracketEntry.read_brackets(entry)
        all_picks[str(entry.entrant_name) + ' - ' + str(entry_num)] = entry.picks

    picks_df = pd.DataFrame(all_picks).T
    save_dir = "summary/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if save_picks == True:
        picks_df.to_csv(save_dir + "picks_2022.csv")
        print(f"picks saved in folder: {save_dir}")

    return entries


if __name__ == "__main__":
    read_brackets()