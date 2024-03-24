CREATE TABLE landing_area.game_inning (
  game_inning_sk SERIAL PRIMARY KEY, -- Surrogate Key
  game_id INT,
  inning_num INT,
  home_team_runs INT,
  home_team_hits INT,
  home_team_errors INT,
  home_team_left_on_base INT,
  away_team_runs INT,
  away_team_hits INT,
  away_team_errors INT,
  away_team_left_on_base INT,
  UNIQUE (game_id, inning_num) -- Composite unique constraint
);
