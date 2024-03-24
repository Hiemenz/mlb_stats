import requests
import json
import os
from urllib.parse import urlparse, parse_qs


def to_float(value):
    
    if not value:
        return value
    try:
        return float(value)
    except ValueError:  # The value cannot be converted to a float
        return None

def parse_batting(batting_data, type):
    
    if type == 'team_game_stats':
        batting_dict = {
            'fly_outs': batting_data['flyOuts'],
            'ground_outs': batting_data['groundOuts'],
            'runs': batting_data['runs'],
            'doubles': batting_data['doubles'],
            'triples': batting_data['triples'],
            'home_runs': batting_data['homeRuns'],
            'strike_outs': batting_data['strikeOuts'],
            'base_on_balls': batting_data['baseOnBalls'],
            'intentional_walks': batting_data['intentionalWalks'],
            'hits': batting_data['hits'],
            'hit_by_pitch': batting_data['hitByPitch'],
            'average': to_float(batting_data['avg']),
            'at_bats': batting_data['atBats'],
            'obp': to_float(batting_data['obp']),
            'slg': to_float(batting_data['slg']),
            'ops': to_float(batting_data['ops']),
            'caught_stealing': batting_data['caughtStealing'],
            'stolen_bases': batting_data['stolenBases'],
            'stolen_base_percentage': to_float(batting_data['stolenBasePercentage']),
            'ground_into_double_play': batting_data['groundIntoDoublePlay'],
            'ground_into_triple_play': batting_data['groundIntoTriplePlay'],
            'plate_appearances': batting_data['plateAppearances'],
            'total_bases': batting_data['totalBases'],
            'rbi': batting_data['rbi'],
            'left_on_base': batting_data['leftOnBase'],
            'sac_bunts': batting_data['sacBunts'],
            'sac_flies': batting_data['sacFlies'],
            'catchers_interference': batting_data['catchersInterference'],
            'pickoffs': batting_data['pickoffs'],
            'at_bats_per_home_run':to_float(batting_data['atBatsPerHomeRun'])
        }
        
    elif type == 'player_game_stats':
        batting_dict = {
            'summary': batting_data['summary'],
            'games_played': batting_data['gamesPlayed'],
            'fly_outs': batting_data['flyOuts'],
            'ground_outs': batting_data['groundOuts'],
            'runs': batting_data['runs'],
            'doubles': batting_data['doubles'],
            'triples': batting_data['triples'],
            'home_runs': batting_data['homeRuns'],
            'strike_outs': batting_data['strikeOuts'],
            'base_on_balls': batting_data['baseOnBalls'],
            'intentional_walks': batting_data['intentionalWalks'],
            'hits': batting_data['hits'],
            'hit_by_pitch': batting_data['hitByPitch'],
            'at_bats': batting_data['atBats'],
            'caught_stealing': batting_data['caughtStealing'],
            'stolen_bases': batting_data['stolenBases'],
            'stolen_base_percentage':to_float(batting_data['stolenBasePercentage']),
            'ground_into_double_play': batting_data['groundIntoDoublePlay'],
            'ground_into_triple_play': batting_data['groundIntoTriplePlay'],
            'plate_appearances': batting_data['plateAppearances'],
            'total_bases': batting_data['totalBases'],
            'rbi': batting_data['rbi'],
            'left_on_base': batting_data['leftOnBase'],
            'sac_bunts': batting_data['sacBunts'],
            'sac_flies': batting_data['sacFlies'],
            'catchers_interference': batting_data['catchersInterference'],
            'pickoffs': batting_data['pickoffs'],
            'at_bats_per_home_run': to_float(batting_data['atBatsPerHomeRun']),
        }
        
    elif type == 'player_season_stats':
        batting_dict = {
            'games_played': batting_data.get('gamesPlayed'),
            'fly_outs': batting_data.get('flyOuts', None),
            'ground_outs': batting_data.get('groundOuts'),
            'runs': batting_data.get('runs'),
            'doubles': batting_data.get('doubles'),
            'triples': batting_data.get('triples'),
            'home_runs': batting_data.get('homeRuns'),
            'strike_outs': batting_data.get('strikeOuts'),
            'base_on_balls': batting_data.get('baseOnBalls'),
            'intentional_walks': batting_data.get('intentionalWalks'),
            'hits': batting_data.get('hits'),
            'hit_by_pitch': batting_data.get('hitByPitch'),
            'avg': to_float(batting_data.get('avg', None)),
            'at_bats': batting_data.get('atBats'),
            'obp': to_float(batting_data.get('obp')),
            'slg': to_float(batting_data.get('slg')),
            'ops': to_float(batting_data.get('ops')),
            'caught_stealing': batting_data.get('caughtStealing'),
            'stolen_bases': batting_data.get('stolenBases'),
            'stolen_base_percentage': to_float(batting_data.get('stolenBasePercentage')),
            'ground_into_double_play': batting_data.get('groundIntoDoublePlay'),
            'ground_into_triple_play': batting_data.get('groundIntoTriplePlay'),
            'plate_appearances': batting_data.get('plateAppearances'),
            'total_bases': batting_data.get('totalBases'),
            'rbi': batting_data.get('rbi'),
            'left_on_base': batting_data.get('leftOnBase'),
            'sac_bunts': batting_data.get('sacBunts'),
            'sac_flies': batting_data.get('sacFlies'),
            'babip': to_float(batting_data.get('babip')),
            'catchers_interference': batting_data.get('catchersInterference'),
            'pickoffs': batting_data.get('pickoffs'),
            'at_bats_per_home_run': to_float(batting_data.get('atBatsPerHomeRun')),
            
        }
    
    return batting_dict
    

def parse_pitching(pitching_data, type):
    if type == 'team_game_stats':
        pitching_dict = {
            'ground_outs': pitching_data.get('groundOuts'),
            'fly_outs': pitching_data.get('airOuts'),
            'runs': pitching_data.get('runs'),
            'doubles': pitching_data.get('doubles'),
            'triples': pitching_data.get('triples'),
            'home_runs': pitching_data.get('homeRuns'),
            'strike_outs': pitching_data.get('strikeOuts'),
            'base_on_balls': pitching_data.get('baseOnBalls'),
            'intentional_walks': pitching_data.get('intentionalWalks'),
            'hits': pitching_data.get('hits'),
            'hit_by_pitch': pitching_data.get('hitByPitch'),
            'at_bats': pitching_data.get('atBats'),
            'obp': to_float(pitching_data.get('obp')),
            'caught_stealing': pitching_data['caughtStealing'],
            'stolen_bases': pitching_data['stolenBases'],
            'stolen_base_percentage': to_float(pitching_data['stolenBasePercentage']),
            'number_of_pitches': pitching_data['numberOfPitches'],
            'era': to_float(pitching_data['era']),
            'innings_pitched': to_float(pitching_data['inningsPitched']),
            'save_opportunities': pitching_data['saveOpportunities'],
            'earned_runs': pitching_data['earnedRuns'],
            'whip':to_float( pitching_data['whip']),
            'batters_faced': pitching_data['battersFaced'],
            'outs': pitching_data['outs'],
            'complete_games': pitching_data['completeGames'],
            'shutouts': pitching_data['shutouts'],
            'pitches_thrown': pitching_data.get('pitchesThrown'),
            'balls': pitching_data['balls'],
            'strikes': pitching_data['strikes'],
            'strike_percentage':to_float( pitching_data['strikePercentage']),
            'hit_batsmen': pitching_data['hitBatsmen'],
            'balks': pitching_data['balks'],
            'wild_pitches': pitching_data['wildPitches'],
            'pickoffs': pitching_data['pickoffs'],
            'ground_outs_to_airouts': to_float(pitching_data['groundOutsToAirouts']),
            'rbi': pitching_data['rbi'],
            'pitches_per_inning':to_float( pitching_data['pitchesPerInning']),
            'runs_scored_per_9': to_float(pitching_data['runsScoredPer9']),
            'home_runs_per_9': to_float(pitching_data['homeRunsPer9']),
            'inherited_runners': pitching_data['inheritedRunners'],
            'inherited_runners_scored': pitching_data['inheritedRunnersScored'],
            'catchers_interference': pitching_data['catchersInterference'],
            'sac_bunts': pitching_data['sacBunts'],
            'sac_flies': pitching_data['sacFlies'],
            'passed_ball': pitching_data['passedBall']
        }
        
    elif type == 'player_game_stats':
        
        
        pitching_dict = {
            'summary' : pitching_data.get('summary'),
            'games_played': pitching_data.get('gamesPlayed'),
            'games_started': pitching_data.get('gamesStarted'),
            'fly_outs': pitching_data.get('flyOuts'),
            'ground_outs': pitching_data.get('groundOuts'),
            'air_outs': pitching_data.get('airOuts'),
            'runs': pitching_data.get('runs'),
            'doubles': pitching_data.get('doubles'),
            'triples': pitching_data.get('triples'),
            'home_runs': pitching_data.get('homeRuns'),
            'strike_outs': pitching_data.get('strikeOuts'),
            'base_on_balls': pitching_data.get('baseOnBalls'),
            'intentional_walks': pitching_data.get('intentionalWalks'),
            'hits': pitching_data.get('hits'),
            'hit_by_pitch': pitching_data.get('hitByPitch'),
            'at_bats': pitching_data.get('atBats'),
            'caught_stealing': pitching_data.get('caughtStealing'),
            'stolen_bases': pitching_data.get('stolenBases'),
            'stolen_base_percentage':to_float( pitching_data.get('stolenBasePercentage')),
            'number_of_pitches': pitching_data.get('numberOfPitches'),
            'innings_pitched': to_float(pitching_data.get('inningsPitched')),
            'wins': pitching_data.get('wins'),
            'losses': pitching_data.get('losses'),
            'saves': pitching_data.get('saves'),
            'save_opportunities': pitching_data.get('saveOpportunities'),
            'holds': pitching_data.get('holds'),
            'blown_saves': pitching_data.get('blownSaves'),
            'earned_runs': pitching_data.get('earnedRuns'),
            'batters_faced': pitching_data.get('battersFaced'),
            'outs': pitching_data.get('outs'),
            'games_pitched': pitching_data.get('gamesPitched'),
            'complete_games': pitching_data.get('completeGames'),
            'shutouts': pitching_data.get('shutouts'),
            'pitches_thrown': to_float(pitching_data.get('pitchesThrown')),
            'balls': pitching_data.get('balls'),
            'strikes': pitching_data.get('strikes'),
            'strike_percentage': to_float(pitching_data.get('strikePercentage')),
            'hit_batsmen': pitching_data.get('hitBatsmen'),
            'balks': pitching_data.get('balks'),
            'wild_pitches': pitching_data.get('wildPitches'),
            'pickoffs': pitching_data.get('pickoffs'),
            'rbi': pitching_data.get('rbi'),
            'games_finished': pitching_data.get('gamesFinished'),
            'runs_scored_per_9': to_float(pitching_data.get('runsScoredPer9')),
            'home_runs_per_9': to_float(pitching_data.get('homeRunsPer9')),
            'inherited_runners': pitching_data.get('inheritedRunners'),
            'inherited_runners_scored': pitching_data.get('inheritedRunnersScored'),
            'catchers_interference': pitching_data.get('catchersInterference'),
            'sac_bunts': pitching_data.get('sacBunts'),
            'sac_flies': pitching_data.get('sacFlies'),
            'passed_ball': pitching_data.get('passedBall'),
        }   
        
    elif type == 'player_season_stats':
        pitching_dict = {
           'games_played': pitching_data.get('gamesPlayed'),
           'games_started': pitching_data.get('gamesStarted'),
           'fly_outs': pitching_data.get('flyOuts'),
           'ground_outs': pitching_data.get('groundOuts'),
           'air_outs': pitching_data.get('airOuts'),
           'runs': pitching_data.get('runs'),
           'doubles': pitching_data.get('doubles'),
           'triples': pitching_data.get('triples'),
           'home_runs': pitching_data.get('homeRuns'),
           'strike_outs': pitching_data.get('strikeOuts'),
           'base_on_balls': pitching_data.get('baseOnBalls'),
           'intentional_walks': pitching_data.get('intentionalWalks'),
           'hits': pitching_data.get('hits'),
           'hit_by_pitch': pitching_data.get('hitByPitch'),
           'at_bats': pitching_data.get('atBats'),
           'obp': to_float(pitching_data.get('obp')),
           'caught_stealing': pitching_data.get('caughtStealing'),
           'stolen_bases': pitching_data.get('stolenBases'),
           'stolen_base_percentage': to_float(pitching_data.get('stolenBasePercentage')),
           'number_of_pitches': pitching_data.get('numberOfPitches'),
           'era': to_float(pitching_data.get('era')),
           'innings_pitched': to_float(pitching_data.get('inningsPitched')),
           'wins': pitching_data.get('wins'),
           'losses': pitching_data.get('losses'),
           'saves': pitching_data.get('saves'),
           'save_opportunities': pitching_data.get('saveOpportunities'),
           'holds': pitching_data.get('holds'),
           'blown_saves': pitching_data.get('blownSaves'),
           'earned_runs': pitching_data.get('earnedRuns'),
           'whip':to_float(pitching_data.get('whip')),
           'batters_faced': pitching_data.get('battersFaced'),
           'outs': pitching_data.get('outs'),
           'games_pitched': pitching_data.get('gamesPitched'),
           'complete_games': pitching_data.get('completeGames'),
           'shutouts': pitching_data.get('shutouts'),
           'pitches_thrown': pitching_data.get('pitchesThrown'),
           'balls': pitching_data.get('balls'),
           'strikes': pitching_data.get('strikes'),
           'strike_percentage':to_float( pitching_data.get('strikePercentage')),
           'hit_batsmen': pitching_data.get('hitBatsmen'),
           'balks': pitching_data.get('balks'),
           'wild_pitches': pitching_data.get('wildPitches'),
           'pickoffs': pitching_data.get('pickoffs'),
           'ground_outs_to_airouts': to_float(pitching_data.get('groundOutsToAirouts')),
           'rbi': pitching_data.get('rbi'),
           'win_percentage': to_float(pitching_data.get('winPercentage')),
           'pitches_per_inning':to_float( pitching_data.get('pitchesPerInning')),
           'games_finished': pitching_data.get('gamesFinished'),
           'strikeout_walk_ratio': to_float(pitching_data.get('strikeoutWalkRatio')),
           'strikeouts_per_9_inn': to_float(pitching_data.get('strikeoutsPer9Inn')),
           'walks_per_9_inn':to_float( pitching_data.get('walksPer9Inn')),
           'hits_per_9_inn': to_float(pitching_data.get('hitsPer9Inn')),
           'runs_scored_per_9': to_float(pitching_data.get('runsScoredPer9')),
           'home_runs_per_9': to_float(pitching_data.get('homeRunsPer9')),
           'inherited_runners': pitching_data.get('inheritedRunners'),
           'inherited_runners_scored': pitching_data.get('inheritedRunnersScored'),
           'catchers_interference': pitching_data.get('catchersInterference'),
           'sac_bunts': pitching_data.get('sacBunts'),
           'sac_flies': pitching_data.get('sacFlies'),
           'passed_ball': pitching_data.get('passedBall'),
        }
    
    return pitching_dict

def parse_fielding(fielding_data, type):
    if type == 'team_game_stats':
        fielding_dict = {
            'caught_stealing': fielding_data['caughtStealing'],
            'stolen_bases': fielding_data['stolenBases'],
            'stolen_base_percentage': to_float(fielding_data['stolenBasePercentage']),
            'assists': fielding_data['assists'],
            'put_outs': fielding_data['putOuts'],
            'errors': fielding_data['errors'],
            'chances': fielding_data['chances'],
            'passed_ball': fielding_data['passedBall'],
            'pickoffs': fielding_data['pickoffs']
        }
        
    elif type == 'player_game_stats':
        fielding_dict = {
            'caught_stealing': fielding_data['caughtStealing'],
            'stolen_bases': fielding_data['stolenBases'],
            'stolen_base_percentage': to_float(fielding_data['stolenBasePercentage']),
            'assists': fielding_data['assists'],
            'put_outs': fielding_data['putOuts'],
            'errors': fielding_data['errors'],
            'chances': fielding_data['chances'],
            'fielding': fielding_data['fielding'],
            'passed_ball': fielding_data['passedBall'],
            'pickoffs': fielding_data['pickoffs'],
            
        }
        
    elif type == 'player_season_stats':
        fielding_dict = {
            'caught_stealing': fielding_data.get('caughtStealing'),
            'stolen_bases': fielding_data.get('stolenBases'),
            'stolen_base_percentage': to_float(fielding_data.get('stolenBasePercentage')),
            'assists': fielding_data.get('assists'),
            'put_outs': fielding_data.get('putOuts'),
            'errors': fielding_data.get('errors'),
            'chances': fielding_data.get('chances'),
            'fielding': fielding_data.get('fielding'),
            'passed_ball': fielding_data.get('passedBall'),
            'pickoffs': fielding_data.get('pickoffs'),
        }
    
    return fielding_dict





def fetch_and_handle_data(url_endpoint):
    # Parse the URL to determine the folder
    parsed_url = urlparse(url_endpoint)
    file_name = parsed_url.path.split('/')[-1]  # Assuming the last part of the path is the endpoint
    
    endpoint = file_name.split('/')[0]
    # Construct the folder path dynamically based on the endpoint
    folder_path = f'data/{endpoint}/'
    
    # Determine the filename, for example, based on the start_date
    filename = (url_endpoint.split('/api/')[-1]).replace('/', '_') + '.json'
    
    file_path = os.path.join(folder_path, filename)
    
    
    if os.path.exists(file_path):
        # File exists, read the data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
            
    else:
    # if True:
        # File doesn't exist, fetch the data from the URL
        response = requests.get(url_endpoint)
        print(f'getting: {url_endpoint}')
        if response.status_code == 200:
            save_off_results(response, folder_path, filename)
            data = response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None        
            
    # Return or process the data as needed
    return data


def save_off_results(response, folder, filename):
    # Ensure the directory exists
    os.makedirs(folder, exist_ok=True)
    # Save the JSON response
    with open(os.path.join(folder, filename), 'w') as file:
        json.dump(response.json(), file)