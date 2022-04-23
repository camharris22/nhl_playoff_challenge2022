# 2022 NHL Playoffs Bracket Challenge

Automatically read bracket entries and calculate pool results

# Usage
Have contestents complete the playoff bracket template in the [`reference` folder](https://github.com/camharris22/nhl_playoff_challenge2022/blob/main/reference/bracket_2022_template.xlsx) and save completed brackets in the `brackets` f older. 

Run `read_brackets.py` to read the picks of contestants and save picks in CSV file.

After each round of playoffs, update the `results` dict in `get_points.py` and rerun `get_points.py` to calculate updated points and save CSV.

