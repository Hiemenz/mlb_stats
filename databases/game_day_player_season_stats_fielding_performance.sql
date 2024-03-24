CREATE TABLE landing_area.game_day_player_season_stats_fielding_performance (
  game_day_player_season_stats_fielding_performance_sk SERIAL PRIMARY KEY,
  game_id INT,
  team_id INT,
  player_id INT,
  caught_stealing INT,
  stolen_bases INT,
  stolen_base_percentage DECIMAL, -- Use DECIMAL for percentages; NULLable since some values might be missing
  assists INT,
  put_outs INT,
  errors INT,
  chances INT,
  fielding DECIMAL, -- Assuming fielding percentage; use DECIMAL to accommodate fractional values
  passed_ball INT,
  pickoffs INT,
  UNIQUE (game_id, team_id, player_id) -- Ensuring each player's entry is unique per game and team
);
