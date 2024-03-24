CREATE TABLE  landing_area.team_game_pitching_stats (
  team_game_pitching_stats_sk SERIAL PRIMARY KEY,
  game_id INT,
  team_id INT,
  ground_outs INT,
  fly_outs INT,
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
  obp DECIMAL,
  caught_stealing INT,
  stolen_bases INT,
  stolen_base_percentage DECIMAL,
  number_of_pitches INT,
  era DECIMAL,
  innings_pitched DECIMAL,
  save_opportunities INT,
  earned_runs INT,
  whip DECIMAL,
  batters_faced INT,
  outs INT,
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
  ground_outs_to_airouts DECIMAL,
  rbi INT,
  pitches_per_inning DECIMAL,
  runs_scored_per_9 DECIMAL,
  home_runs_per_9 DECIMAL,
  inherited_runners INT,
  inherited_runners_scored INT,
  catchers_interference INT,
  sac_bunts INT,
  sac_flies INT,
  passed_ball INT,
  UNIQUE (game_id, team_id)
);