CREATE TABLE landing_area.play_by_play (
    play_by_play_sk SERIAL PRIMARY KEY,
    game_id INT,
    at_bat_index INT,
    sequence_index INT,
    pitch_number INT,
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    is_pitch BOOLEAN,
    play_type VARCHAR(255),
    batter_player_id INT,
    batter_player_full_name VARCHAR(255),
    pitcher_player_id INT,
    pitcher_player_full_name VARCHAR(255),
    pitch_description TEXT,
    pitch_code VARCHAR(10),
    details_description TEXT,
    details_code VARCHAR(10),
    details_event TEXT,
    details_eventType VARCHAR(255),
    is_scoring_play BOOLEAN,
    is_in_play BOOLEAN,
    is_strike BOOLEAN,
    is_ball BOOLEAN,
    is_out BOOLEAN,
    has_review BOOLEAN,
    from_catcher BOOLEAN,
    disengagement_num INT,
    pitch_type_code VARCHAR(10),
    pitch_type_description VARCHAR(255),
    pitch_type_confidence FLOAT,
    count_balls INT,
    count_strikes INT,
    count_outs INT,
    pre_count_balls INT,
    pre_count_strikes INT,
    pre_count_outs INT,
    start_speed FLOAT,
    end_speed FLOAT,
    strike_zone_top FLOAT,
    strike_zone_bottom FLOAT,
    strike_zone_width FLOAT,
    strike_zone_depth FLOAT,
    pitch_coordinates_aY FLOAT,
    pitch_coordinates_aZ FLOAT,
    pitch_coordinates_pfxX FLOAT,
    pitch_coordinates_pfxZ FLOAT,
    pitch_coordinates_pX FLOAT,
    pitch_coordinates_pZ FLOAT,
    pitch_coordinates_vX0 FLOAT,
    pitch_coordinates_vY0 FLOAT,
    pitch_coordinates_vZ0 FLOAT,
    pitch_coordinates_x FLOAT,
    pitch_coordinates_y FLOAT,
    pitch_coordinates_x0 FLOAT,
    pitch_coordinates_y0 FLOAT,
    pitch_coordinates_z0 FLOAT,
    pitch_coordinates_aX FLOAT,
    pitch_breaks_break_angle FLOAT,
    pitch_breaks_break_length FLOAT,
    pitch_breaks_break_Y FLOAT,
    pitch_breaks_break_vertical FLOAT,
    pitch_breaks_break_vertical_induced FLOAT,
    pitch_breaks_break_horizontal FLOAT,
    pitch_zone INT,
    pitch_plate_time FLOAT,
    pitch_extension FLOAT
);
