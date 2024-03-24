CREATE TABLE landing_area.team_game_batting_stats (
  team_game_batting_stats_sk SERIAL PRIMARY KEY, -- Surrogate Key
  game_id INT,
  team_id INT,
  fly_outs INT,
  ground_outs INT,
  runs INT,
  doubles INT,
  triples INT,
  home_runs INT,
  strike_outs INT,
  base_on_balls INT,
  intentional_walks INT,
  hits INT,
  hit_by_pitch INT,
  average DECIMAL, -- Stored as numeric for calculations, derived from hits/at_bats
  at_bats INT,
  obp DECIMAL, -- On-base percentage
  slg DECIMAL, -- Slugging percentage
  ops DECIMAL, -- On-base plus slugging
  caught_stealing INT,
  stolen_bases INT,
  stolen_base_percentage DECIMAL, -- Stored as numeric, derived from stolen_bases / (stolen_bases + caught_stealing)
  ground_into_double_play INT,
  ground_into_triple_play INT,
  plate_appearances INT,
  total_bases INT,
  rbi INT, -- Runs batted in
  left_on_base INT,
  sac_bunts INT, -- Sacrifice bunts
  sac_flies INT, -- Sacrifice flies
  catchers_interference INT,
  pickoffs INT,
  at_bats_per_home_run DECIMAL, -- Stored as numeric, derived from at_bats / home_runs
  UNIQUE (game_id, team_id) -- Composite unique constraint to ensure one entry per team per game
);
