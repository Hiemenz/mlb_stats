CREATE TABLE landing_area.team_game_fielding_stats (
  team_game_fielding_stats_sk SERIAL PRIMARY KEY,
  caught_stealing INT,
  stolen_bases INT,
  stolen_base_percentage DECIMAL, -- Use DECIMAL for percentages; NULLable since some values might be missing
  assists INT,
  put_outs INT,
  errors INT,
  chances INT,
  passed_ball INT,
  pickoffs INT,
  game_id INT,
  team_id INT,
  UNIQUE (game_id, team_id) -- Ensure there's only one entry per team per game
);
