import pandas as pd
from pathlib import Path
import json
import numpy as np

mod_path = Path(__file__).parent
relative_path = '../data/replay_list_all.json'
src_path = (mod_path / relative_path).resolve()

with open(src_path, 'r') as f:
    data = json.load(f)

replay_data = pd.json_normalize(data)

col_renamer = {
    "replay_id" : "replay_id",
    "battle_version" : "version",
    "replay_battle_type_name" : "battle_type",
    "player1_info.player.fighter_id" : "p1_name", 
    "player1_info.player.platform_name" : "p1_platform", 
    "player1_info.player.short_id" : "p1_id", 
    "player1_info.home_id" : "p1_home_id",
    
    "player1_info.round_results":"p1_round_results", 
    "player1_info.character_name" : "p1_character",
    "player1_info.battle_input_type" : "p1_input",
    "player1_info.league_point" : "p1_lp", 
    "player1_info.master_rating" : "p1_mr",
    "player1_info.title_data.title_data_val" : "p1_title", 
    "player1_info.main_circle.circle_id" : "p1_circle_id",
    "player1_info.main_circle.circle_name" : "p1_circle_name",
    
    "player2_info.player.fighter_id" : "p2_name", 
    "player2_info.player.platform_name" : "p2_platform", 
    "player2_info.player.short_id" : "p2_id", 
    "player2_info.home_id" : "p2_home_id",
    
    "player2_info.round_results" : "p2_round_results", 
    "player2_info.character_name" : "p2_character",
    "player2_info.battle_input_type" : "p2_input",
    "player2_info.league_point" : "p2_lp", 
    "player2_info.master_rating" : "p2_mr",
    "player2_info.title_data.title_data_val" : "m2_title", 
    "player2_info.main_circle.circle_id" : "p2_circle_id",
    "player2_info.main_circle.circle_name" : "p2_circle_name"
    }

replay_data_reduced = replay_data.rename(columns = col_renamer)[[*col_renamer.values()]]

def code_win_loss(input_list):
    return [1 if x >= 1 else x for x in input_list]

replay_data_reduced['p1_round_results'] = replay_data_reduced['p1_round_results'].apply(code_win_loss) 
replay_data_reduced['p1_won_first_round'] = replay_data_reduced['p1_round_results'].map(lambda x: True if x[0] == 1 else False)
replay_data_reduced['p2_round_results'] = replay_data_reduced['p2_round_results'].apply(code_win_loss) 
replay_data_reduced['p2_won_first_round'] = replay_data_reduced['p2_round_results'].map(lambda x: True if x[0] == 1 else False)

replay_data_reduced['p1_win'] = np.where(replay_data_reduced['p1_round_results'].apply(sum) >= 2, True, False)
replay_data_reduced['p2_win'] = np.where(replay_data_reduced['p2_round_results'].apply(sum) >= 2, True, False)






print(replay_data_reduced['p1_win'])