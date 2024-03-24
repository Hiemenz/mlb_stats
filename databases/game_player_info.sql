CREATE TABLE landing_area.game_player_info (
  game_player_info_sk SERIAL PRIMARY KEY,
  game_id INT,
  team_id INT,
  player_id INT,
  full_name VARCHAR(255),
  link VARCHAR(255),
  jersey_number INT, 
  position CHAR(2), -- Assuming position codes are short, e.g., "P" for Pitcher; adjust size as needed
  status_code VARCHAR(50),
  status_description VARCHAR(255),
  UNIQUE (game_id, team_id, player_id) -- Ensuring each player's entry is unique per game and team
);
