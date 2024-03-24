CREATE TABLE landing_area.game_team_totals (
  game_team_totals_sk SERIAL PRIMARY KEY, -- Surrogate Key
  game_id INT UNIQUE, 
  home_team_total_runs INT,
  home_team_total_hits INT,
  home_team_total_errors INT,
  home_team_total_left_on_base INT,
  away_team_total_runs INT,
  away_team_total_hits INT,
  away_team_total_errors INT,
  away_team_total_left_on_base INT
);
