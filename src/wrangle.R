library(jsonlite)
library(dplyr)

replay_info_js <- fromJSON("C:/Users/axshi/Documents/CFNScrape/CFNScrape/bin/Debug/net6.0/replay_list_all.json")

replay_data_flat <- replay_info_js %>%
  select(replay_id,
         battle_version,
         player1_info,
         player2_info,
         replay_battle_type_name) %>%
  flatten() 


reduced_df <- replay_data_flat %>% select(
  replay_id,
  battle_version,
  battle_type = replay_battle_type_name,
  p1_name = player1_info.player.fighter_id, 
  p1_platform = player1_info.player.platform_name, 
  p1_id = player1_info.player.short_id, 
  p1_home_id = player1_info.home_id,
  
  p1_round_results = player1_info.round_results, 
  p1_character = player1_info.character_name,
  p1_input = player1_info.battle_input_type,
  p1_lp = player1_info.league_point, 
  p1_mr = player1_info.master_rating,
  p1_title = player1_info.title_data.title_data_val, 
  p1_circle_id = player1_info.main_circle.circle_id,
  p1_circle_name = player1_info.main_circle.circle_name,
  
  p2_name = player2_info.player.fighter_id, 
  p2_platform = player2_info.player.platform_name, 
  p2_id = player2_info.player.short_id, 
  p2_home_id = player2_info.home_id,
  
  p2_round_results = player2_info.round_results, 
  p2_character = player2_info.character_name,
  p2_input = player2_info.battle_input_type,
  p2_lp = player2_info.league_point, 
  p2_mr = player2_info.master_rating,
  m2_title = player2_info.title_data.title_data_val, 
  p2_circle_id = player2_info.main_circle.circle_id,
  p2_circle_name = player2_info.main_circle.circle_name
  )