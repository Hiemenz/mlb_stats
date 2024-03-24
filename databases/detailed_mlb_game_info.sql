CREATE TABLE landing_area.detailed_mlb_game_info (
  detailed_mlb_game_info_sk SERIAL PRIMARY KEY, -- Surrogate Key
  game_id INT,
  game_date TIMESTAMP WITH TIME ZONE,
  game_type CHAR(1),
  game_status VARCHAR(50),
  home_team_id INT,
  home_team_name VARCHAR(255),
  away_team_id INT,
  away_team_name VARCHAR(255),
  venue_id INT,
  venue_name VARCHAR(255),
  home_team_runs INT,
  away_team_runs INT,
  game_duration INT, -- Assuming duration is in minutes; use appropriate data type
  attendance INT,
  weather_description VARCHAR(255),
  temperature DECIMAL, -- Assuming temperature might need fractional part
  wind_description VARCHAR(255),
  detailed_status VARCHAR(50),
  double_header_flag CHAR(1),
  game_number_of_day INT,
  day_night VARCHAR(10),
  games_in_series INT, -- Assuming this represents total games in the series; adjust if needed
  series_game_number INT,
  series_description VARCHAR(255),
  UNIQUE (game_id, home_team_id, away_team_id) -- Composite unique constraint
);

-- todo
-- rework to use the feed live for this table and anything that i 
-- cannot find in the live feed then put it to the summary table