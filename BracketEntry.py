import pandas as pd

class BracketEntry():
    """Class to manage bracket entries and calculate points"""
    def __init__(self, bracket_name):
        self.bracket_name = bracket_name
        self.picks = {}
        self.points = {}
            
    def read_brackets(self):
        """Read playoff bracket entries and save results as dict"""
        directory = "brackets/" + self.bracket_name
        df = pd.read_excel(directory, sheet_name='teams')
        self.entrant_name = df['entrant_name'].dropna().item()
        # if self.entrant_name in self.picks.keys():
        #     self.entrant_name = self.entrant_name + ' 2'

        self.picks = {
            'rd1_selections' : df['rd1_selections'].dropna().to_list(),
            'rd2_selections' : df['rd2_selections'].dropna().to_list(),
            'rd3_selections' : df['rd3_selections'].dropna().to_list(),
            'rd4_selections' : df['rd4_selections'].dropna().to_list(),
            'tie_breaker' : df['tie_breaker'].dropna().to_list()
        }
        return self.picks
        
    def calc_points(self, results):
        """Calculate pool points based on latest playoff results"""
        points_by_round = {
            'rd1': 2,
            'rd2': 4,
            'rd3': 8,
            'rd4': 17
        }
        for rd in results.keys():
            round_picks = self.picks[rd+'_selections']
            round_result = results[rd]
            round_points = len(set(round_picks) & set(round_result))*points_by_round[rd]
            self.points[rd+'_points'] = round_points
        return self.points