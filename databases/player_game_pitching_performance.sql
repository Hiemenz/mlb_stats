CREATE TABLE landing_area.player_game_pitching_performance (
  player_game_pitching_performance_sk SERIAL PRIMARY KEY,
  game_id INT,
  team_id INT,
  player_id int,
  summary VARCHAR(255),
  games_played INT,
  games_started INT,
  fly_outs INT,
  ground_outs INT,
  air_outs INT,
  runs INT,
  doubles INT,
  triples INT,
  home_runs INT,
  strike_outs INT,
  base_on_balls INT,
  intentional_walks INT,
  hits INT,
  hit_by_pitch INT,
  at_bats INT,
  caught_stealing INT,
  stolen_bases INT,
  stolen_base_percentage DECIMAL, -- Use DECIMAL for percentages; NULLable since some values might be missing
  number_of_pitches INT,
  innings_pitched DECIMAL,
  wins INT,
  losses INT,
  saves INT,
  save_opportunities INT,
  holds INT,
  blown_saves INT,
  earned_runs INT,
  batters_faced INT,
  outs INT,
  games_pitched INT,
  complete_games INT,
  shutouts INT,
  pitches_thrown DECIMAL,
  balls INT,
  strikes INT,
  strike_percentage DECIMAL,
  hit_batsmen INT,
  balks INT,
  wild_pitches INT,
  pickoffs INT,
  rbi INT,
  games_finished INT,
  runs_scored_per_9 DECIMAL,
  home_runs_per_9 DECIMAL,
  inherited_runners INT,
  inherited_runners_scored INT,
  catchers_interference INT,
  sac_bunts INT,
  sac_flies INT,
  passed_ball INT,
  UNIQUE (game_id, team_id, player_id) -- Ensuring each team's entry is unique per game
);
