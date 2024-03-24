

CREATE TABLE landing_area.mlb_game_summary (
  mlb_game_summary_sk SERIAL PRIMARY KEY, -- Surrogate key
  game_id INT,
  game_date DATE,
  game_type CHAR(1),
  game_status VARCHAR(50),
  home_team_id INT,
  home_team_name VARCHAR(255),
  home_team_score INT,
  away_team_id INT,
  away_team_name VARCHAR(255),
  away_team_score INT,
  venue_id INT,
  venue_name VARCHAR(255),
  UNIQUE (game_id, home_team_id, away_team_id, game_date) -- Composite key as a unique constraint
);


