import requests
from database import batch_generic_insert_mlb

import datetime

from parse_helper import parse_batting, parse_pitching, parse_fielding, fetch_and_handle_data
import json
import time
import csv
import os


game_summary_list = []
game_summaries_list = []

inning_list = []
game_total_list = []

team_game_batting_stats_list = []
team_game_pitching_stats_list = []
team_game_fielding_stats_list = []
game_player_info_list = []

player_game_batting_performance_list = []
player_game_pitching_performance_list = []
player_game_fielding_performance_list = []

player_season_stats_batting_list = [] 
player_season_stats_pitching_list = []
player_season_stats_fielding_list = []

    
play_outcome_list = []
play_by_play_list = []



# batch_generic_insert_mlb('landing_area.mlb_game_summary', game_summary_list)
# batch_generic_insert_mlb('landing_area.game_summaries', game_summaries_list)

# batch_generic_insert_mlb('landing_area.game_team_totals', game_total_list)
# batch_generic_insert_mlb('landing_area.game_inning', inning_list)

# batch_generic_insert_mlb('landing_area.team_game_batting_stats', team_game_batting_stats_list)
# batch_generic_insert_mlb('landing_area.team_game_pitching_stats', team_game_pitching_stats_list)
# batch_generic_insert_mlb('landing_area.team_game_fielding_stats', team_game_fielding_stats_list)
# batch_generic_insert_mlb('landing_area.game_player_info', game_player_info_list)

# batch_generic_insert_mlb('landing_area.player_game_batting_performance', player_game_batting_performance_list)
# batch_generic_insert_mlb('landing_area.player_game_pitching_performance', player_game_pitching_performance_list)
# batch_generic_insert_mlb('landing_area.player_game_fielding_performance', player_game_fielding_performance_list)

# batch_generic_insert_mlb('landing_area.game_day_player_season_stats_batting_performance', player_season_stats_batting_list)
# batch_generic_insert_mlb('landing_area.game_day_player_season_stats_pitching_performance', player_season_stats_pitching_list)
# batch_generic_insert_mlb('landing_area.game_day_player_season_stats_fielding_performance', player_season_stats_fielding_list)


def get_game_summary_data(start_date, end_date, insert_into_database=True):    
    global game_summary_list
    url_endpoint = f'https://statsapi.mlb.com/api/v1/schedule?startDate={start_date}&endDate={end_date}&sportId=1'

    data = fetch_and_handle_data(url_endpoint)

    if data:
        game_id_list = []
        game_summary_list = []
        if not data['dates']:
            return []
        
        for game in data['dates'][0]['games']:
            
            game_summary_data = {
                'game_id' : game['gamePk'],
                'game_date' : data['dates'][0]['date'],
                'game_type' : game.get('gameType', ''),
                'game_status' : game['status']['detailedState'],
                'home_team_id' : game['teams']['home']['team']['id'],
                'home_team_name' : game['teams']['home']['team'].get('name'),
                'home_team_score' : game['teams']["home"]["score"] if 'score' in game['teams']["home"] else None,
                'away_team_id' : game['teams']['away']['team']['id'],
                'away_team_name' : game['teams']['away']['team'].get('name'),
                'away_team_score' : game['teams']["away"]["score"] if 'score' in game['teams']["away"] else None,
                'venue_id' : game['venue']['id'] if 'venue' in game else None,
                'venue_name' : game['venue']['name'] if 'venue' in game else ''
                
                
                
            }
            game_id_list.append(game['gamePk'])
            game_summary_list.append(game_summary_data)
            
        # if insert_into_database:    
        #     batch_generic_insert_mlb('landing_area.mlb_game_summary', game_summary_list)
        return game_id_list
    
    # this should be live feed
def get_game_summaries(game_id, insert_into_database=True):    
                
    global game_summaries_list
    url_endpoint = f'https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live'
    
    data = fetch_and_handle_data(url_endpoint)
    if data:
        
        
        game_summaries_dict = {
            'game_id': data.get('gameData',{}).get('game',{}).get('pk'),
            'game_type': data.get('gameData',{}).get('game',{}).get('type'),
            'game_double_header': data.get('gameData',{}).get('game',{}).get('doubleHeader'),
            'game_identifier': data.get('gameData',{}).get('game',{}).get('id'),
            'game_day_type': data.get('gameData',{}).get('game',{}).get('gamedayType'),
            'game_tiebreaker': data.get('gameData',{}).get('game',{}).get('tiebreaker'),
            'game_number': data.get('gameData',{}).get('game',{}).get('gameNumber'),
            'game_calendar_event_id': data.get('gameData',{}).get('game',{}).get('calendarEventID'),
            'game_season': data.get('gameData',{}).get('game',{}).get('season'),
            'date_time': data.get('gameData',{}).get('datetime',{}).get('dateTime'),
            'original_date': data.get('gameData',{}).get('datetime',{}).get('originalDate'),
            'official_date': data.get('gameData',{}).get('datetime',{}).get('officialDate'),
            'day_night': data.get('gameData',{}).get('datetime',{}).get('dayNight'),
            'time_str': data.get('gameData',{}).get('datetime',{}).get('time'),
            'ampm': data.get('gameData',{}).get('datetime',{}).get('ampm'),
            'coded_game_state': data.get('gameData',{}).get('status',{}).get('codedGameState'),
            'status_code': data.get('gameData',{}).get('status',{}).get('statusCode'),
            'away_team_name': data.get('gameData',{}).get('teams',{}).get('away').get('name'),
            'away_team_id': data.get('gameData',{}).get('teams',{}).get('away').get('id'),
            'away_team_abbreviation': data.get('gameData',{}).get('teams',{}).get('away').get('abbreviation'),
            'away_team_games_played': data.get('gameData',{}).get('teams',{}).get('away').get('record').get('gamesPlayed'),
            'away_team_record_wins': data.get('gameData',{}).get('teams',{}).get('away').get('wins'),
            'away_team_record_losses': data.get('gameData',{}).get('teams',{}).get('away').get('losses'),
            'home_team_name': data.get('gameData',{}).get('teams',{}).get('home').get('name'),
            'home_team_id': data.get('gameData',{}).get('teams',{}).get('home').get('id'),
            'home_team_abbreviation': data.get('gameData',{}).get('teams',{}).get('home').get('abbreviation'),
            'home_team_games_played': data.get('gameData',{}).get('teams',{}).get('home').get('record').get('gamesPlayed'),
            'home_team_record_wins': data.get('gameData',{}).get('teams',{}).get('home').get('wins'),
            'home_team_record_losses': data.get('gameData',{}).get('teams',{}).get('home').get('losses'),
            'venue_id': data.get('gameData',{}).get('venue',{}).get('id'),
            'venue_name': data.get('gameData',{}).get('venue',{}).get('name'),
            'venue_link': data.get('gameData',{}).get('venue',{}).get('link'),
            'venue_capacity': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('capacity'),
            'venue_turf_type': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('turfType'),
            'venue_roof_type': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('roofType'),
            'venue_left_line': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('leftLine'),
            'venue_left_center': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('leftCenter'),
            'venue_center': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('center'),
            'venue_right_center': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('rightCenter'),
            'venue_right_line': data.get('gameData',{}).get('venue',{}).get('fieldInfo', {}).get('rightLine'),
            'weather_condition': data.get('gameData',{}).get('weather',{}).get('condition'),
            'weather_temp': data.get('gameData',{}).get('weather',{}).get('temp'),
            'weather_wind': data.get('gameData',{}).get('weather',{}).get('wind'),
            'game_attendance': data.get('gameData',{}).get('gameInfo',{}).get('attendance'),
            'game_first_pitch': data.get('gameData',{}).get('gameInfo',{}).get('firstPitch'),
            'game_duration_minutes': data.get('gameData',{}).get('gameInfo',{}).get('gameDurationMinutes'),
        }

        game_summaries_list.append(game_summaries_dict)
        
    # if insert_into_database:        

    #     batch_generic_insert_mlb('landing_area.game_summaries', game_summaries_list)


def parse_linescore(gamePk, insert_into_database=True):

    global inning_list
    global game_total_list
    url_endpoint = f'https://statsapi.mlb.com/api/v1/game/{gamePk}/linescore'
   
    
    data = fetch_and_handle_data(url_endpoint)

    
    for inning in data['innings']:
        inning_dict = {
            'game_id': gamePk,
            'inning_num' : inning['num'],
            'home_team_runs': inning['home'].get('runs'),
            'home_team_hits': inning['home']['hits'],
            'home_team_errors': inning['home']['errors'],
            'home_team_left_on_base': inning['home']['leftOnBase'],
            'away_team_runs':inning['away'].get('runs'),
            'away_team_hits':inning['away']['hits'],
            'away_team_errors':inning['away']['errors'],
            'away_team_left_on_base':inning['away']['leftOnBase']
        }
        inning_list.append(inning_dict)  

    # if insert_into_database:   
    #     batch_generic_insert_mlb('landing_area.game_inning', inning_list)
    
    game_team_totals = {
        'game_id': gamePk,
        'home_team_total_runs' : data['teams']['home'].get('runs'),
        'home_team_total_hits' : data['teams']['home'].get('hits'),
        'home_team_total_errors' : data['teams']['home'].get('errors'),
        'home_team_total_left_on_base' : data['teams']['home'].get('leftOnBase'),
        'away_team_total_runs' : data['teams']['away'].get('runs'),
        'away_team_total_hits' : data['teams']['away'].get('hits'),
        'away_team_total_errors' : data['teams']['away'].get('errors'),
        'away_team_total_left_on_base' : data['teams']['away'].get('leftOnBase'),
    }
    game_total_list.append(game_team_totals)
    # if insert_into_database:   
    #     batch_generic_insert_mlb('landing_area.game_team_totals', game_total_list)
    
    
def parse_box_score(gamePk, insert_into_database=True):
    

    global team_game_batting_stats_list
    global team_game_pitching_stats_list
    global team_game_fielding_stats_list
    global game_player_info_list
    global player_game_batting_performance_list
    global player_game_pitching_performance_list
    global player_game_fielding_performance_list
    global player_season_stats_batting_list
    global player_season_stats_pitching_list
    global player_season_stats_fielding_list
    url_endpoint = f'https://statsapi.mlb.com/api/v1/game/{gamePk}/boxscore'

    data = fetch_and_handle_data(url_endpoint)

    
    side = ['home', 'away']
    
    

    for team in side:
        # todo put in yaml magic string
        team_game_batting_stats = parse_batting(data['teams'][team]['teamStats']['batting'], 'team_game_stats')
        
        team_game_batting_stats['game_id'] = gamePk
        team_id = data['teams'][team]['team']['id']
        team_game_batting_stats['team_id'] = team_id
        
        team_game_batting_stats_list.append(team_game_batting_stats)
        
        team_game_pitching_stats =  parse_pitching(data['teams'][team]['teamStats']['pitching'], 'team_game_stats')
        team_game_pitching_stats['game_id'] = gamePk
        team_game_pitching_stats['team_id'] = team_id
        
        team_game_pitching_stats_list.append(team_game_pitching_stats)

        
        team_game_field_stats = parse_fielding(data['teams'][team]['teamStats']['fielding'], 'team_game_stats')
        team_game_field_stats['game_id'] = gamePk
        team_game_field_stats['team_id'] = team_id
        
        team_game_fielding_stats_list.append(team_game_field_stats)
        

        for player_game_id in data['teams'][team]['players']:
            # print(player)
            
            player_id = data['teams'][team]['players'][player_game_id]['person']['id'],
            
            
            
            jersey_number = data['teams'][team]['players'][player_game_id].get('jerseyNumber')
            jersey_number = None if jersey_number == "" else jersey_number
            
            player_generic = {
                'game_id' : gamePk,
                'team_id': team_id,
                'player_id': player_id,
                'full_name': data['teams'][team]['players'][player_game_id]['person'].get('fullName'),
                'link': data['teams'][team]['players'][player_game_id]['person']['link'],
                'jersey_number': jersey_number,
                'position': data['teams'][team]['players'][player_game_id].get('position',{}).get('code'),
                'status_code': data['teams'][team]['players'][player_game_id]['status']['code'],
                'status_description': data['teams'][team]['players'][player_game_id]['status']['description']
            }
            # todo add to database
            game_player_info_list.append(player_generic)
            
            # current game stats
            current_game_stats = data['teams'][team]['players'][player_game_id]['stats']
            player_season_stats = data['teams'][team]['players'][player_game_id]['seasonStats']
            if current_game_stats['batting']:
                returned_dict = parse_batting(current_game_stats['batting'], 'player_game_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                
                player_game_batting_performance_list.append(returned_dict)

            if current_game_stats['pitching']:
                returned_dict = parse_pitching(current_game_stats['pitching'], 'player_game_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                player_game_pitching_performance_list.append(returned_dict)

            if current_game_stats['fielding']:
                returned_dict = parse_fielding(current_game_stats['fielding'], 'player_game_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                player_game_fielding_performance_list.append(returned_dict)

    # todo remove magic strings
            if player_season_stats['batting']:
                returned_dict = parse_batting(player_season_stats['batting'], 'player_season_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                player_season_stats_batting_list.append(returned_dict)

            if player_season_stats['pitching']:
                returned_dict = parse_pitching(player_season_stats['pitching'], 'player_season_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                player_season_stats_pitching_list.append(returned_dict)

            if player_season_stats['fielding']:
                returned_dict = parse_fielding(player_season_stats['fielding'], 'player_season_stats')
                returned_dict['game_id'] = gamePk
                returned_dict['team_id'] = team_id
                returned_dict['player_id'] = player_id
                player_season_stats_fielding_list.append(returned_dict)
                
    
    # if insert_into_database:
    #     batch_generic_insert_mlb('landing_area.team_game_batting_stats', team_game_batting_stats_list)
    #     batch_generic_insert_mlb('landing_area.team_game_pitching_stats', team_game_pitching_stats_list)
    #     batch_generic_insert_mlb('landing_area.team_game_fielding_stats', team_game_fielding_stats_list)
    #     batch_generic_insert_mlb('landing_area.game_player_info', game_player_info_list)
        
    #     batch_generic_insert_mlb('landing_area.player_game_batting_performance', player_game_batting_performance_list)
    #     batch_generic_insert_mlb('landing_area.player_game_pitching_performance', player_game_pitching_performance_list)
    #     batch_generic_insert_mlb('landing_area.player_game_fielding_performance', player_game_fielding_performance_list)

    #     batch_generic_insert_mlb('landing_area.game_day_player_season_stats_batting_performance', player_season_stats_batting_list)
    #     batch_generic_insert_mlb('landing_area.game_day_player_season_stats_pitching_performance', player_season_stats_pitching_list)
    #     batch_generic_insert_mlb('landing_area.game_day_player_season_stats_fielding_performance', player_season_stats_fielding_list)



def get_live_feed(game_id):
    pass

def get_roster():
    pass

def get_standings(league_id, season):
    url_endpoint = f'https://statsapi.mlb.com/api/v1/standings?leagueId={league_id}&season={season}'
    data = fetch_and_handle_data(url_endpoint)
    
    print(data)
    
    standings_list = []
    
    for item in data['records']:
        for team_record in item['teamRecords']:
            
            for record in team_record.get('records', {}).get('splitRecords'):
                record_type = record.get('type') 
                if record_type == 'lastTen':
                    last_ten_wins = record.get('wins') 
                    last_ten_losses = record.get('losses')
                elif record_type == 'home':                    
                    home_wins = record.get('wins') 
                    home_losses = record.get('losses')
                elif record_type == 'away':                    
                    away_wins = record.get('wins') 
                    away_losses = record.get('losses')
                elif record_type == 'oneRun':                    
                    one_run_wins = record.get('wins') 
                    one_run_losses = record.get('losses')
                elif record_type == 'day':                    
                    day_game_wins = record.get('wins') 
                    day_game_losses = record.get('losses')
                elif record_type == 'night':                    
                    night_game_wins = record.get('wins') 
                    night_game_losses = record.get('losses')
                elif record_type == 'extraInning':                    
                    extra_inning_wins = record.get('wins') 
                    extra_inning_losses = record.get('losses')
            for record in team_record.get('records', {}).get('expectedRecords'):     
                record_type = record.get('type') 
                if record_type == 'xWinLoss':
                    expected_record_wins =  record.get('wins') 
                    expected_record_losses =  record.get('losses') 
            
            team_standing_dict ={
                'season' : season,
                'team_id': team_record.get('team', {}).get('id'),
                'team_name': team_record.get('team', {}).get('name'),
                'league_id': item.get('league', {}).get('id'),
                'league_link': item.get('league', {}).get('link'),
                'division_id': item.get('division', {}).get('id'),
                'division_link': item.get('division', {}).get('link'),
                'team_link': team_record.get('team', {}).get('link'),
                'season': team_record.get('season'),
                'streakType': team_record.get('streak', {}).get('streakType'),
                'streakNumber': team_record.get('streak', {}).get('streakNumber'),
                'streakCode': team_record.get('streak', {}).get('streakCode'),
                'clinchIndicator': team_record.get('clinchIndicator'),
                'divisionRank': team_record.get('divisionRank'),
                'leagueRank': team_record.get('leagueRank'),
                'sportRank': team_record.get('sportRank'),
                'gamesPlayed': team_record.get('gamesPlayed'),
                'gamesBack': team_record.get('gamesBack'),
                'wildCardGamesBack': team_record.get('wildCardGamesBack'),
                'leagueGamesBack': team_record.get('leagueGamesBack'),
                'springLeagueGamesBack': team_record.get('springLeagueGamesBack'),
                'sportGamesBack': team_record.get('sportGamesBack'),
                'divisionGamesBack': team_record.get('divisionGamesBack'),
                'conferenceGamesBack': team_record.get('conferenceGamesBack'),
                'wins': team_record.get('leagueRecord', {}).get('wins'),
                'losses': team_record.get('leagueRecord', {}).get('losses'),
                'ties': team_record.get('leagueRecord', {}).get('ties'),
                'pct': team_record.get('leagueRecord', {}).get('pct'),
                'lastUpdated': team_record.get('lastUpdated'),
                'runsAllowed': team_record.get('runsAllowed'),
                'runsScored': team_record.get('runsScored'),
                'divisionChamp': team_record.get('divisionChamp'),
                'divisionLeader': team_record.get('divisionLeader'),
                'hasWildcard': team_record.get('hasWildcard'),
                'clinched': team_record.get('clinched'),
                'eliminationNumber': team_record.get('eliminationNumber'),
                'eliminationNumberSport': team_record.get('eliminationNumberSport'),
                'eliminationNumberLeague': team_record.get('eliminationNumberLeague'),
                'eliminationNumberDivision': team_record.get('eliminationNumberDivision'),
                'eliminationNumberConference': team_record.get('eliminationNumberConference'),
                'wildCardEliminationNumber': team_record.get('wildCardEliminationNumber'),
                'magicNumber': team_record.get('magicNumber'),
                'wins': team_record.get('wins'),
                'losses': team_record.get('losses'),
                'runDifferential': team_record.get('runDifferential'),
                'winningPercentage': team_record.get('winningPercentage'),
                'last_ten_wins': last_ten_wins,
                'last_ten_losses': last_ten_losses,
                'home_wins': home_wins,
                'home_losses': home_losses,
                'away_wins': away_wins,
                'away_losses': away_losses,
                'one_run_wins': one_run_wins,
                'one_run_losses': one_run_losses,
                'day_game_wins': day_game_wins,
                'day_game_losses': day_game_losses,
                'night_game_wins': night_game_wins,
                'night_game_losses': night_game_losses,
                'extra_inning_wins': extra_inning_wins,
                'extra_inning_losses': extra_inning_losses,
                'expected_record_wins': expected_record_wins,
                'expected_record_losses': expected_record_losses,
            }
            
            standings_list.append(team_standing_dict)
            
    print(standings_list)
    write_or_append_to_csv('csv/standings.csv', standings_list)

     

def get_teams():
    
    response = requests.get(f'https://statsapi.mlb.com/api/v1/teams')
    data = response.json()
    
    teams_lists = []
    for team in data['teams']:
        teams_dict = {
           'team_id': team['id'],
           'team_full_name': team['name'],
           'team_link': team['link'],
           'team_season': team['season'],
           'venue_id': team['venue']['id'],
            'venue_name': team['venue']['name'],
            'venue_link': team['venue']['link'],
            'team_code': team['teamCode'],
            'file_code': team.get('fileCode'),
            'abbreviation': team['abbreviation'],
            'team_name': team['teamName'],
            'first_year_of_play': team.get('firstYearOfPlay'),
            'league_id': team['league'].get('id'),
            'league_name':team['league'].get('name'),
            'league_link': team['league'].get('link'),
            'division_id': team.get('division', {}).get('id'),
            'division_name': team.get('division', {}).get('name'),
            'division_link': team.get('division', {}).get('link'),
            'sport_id': team['sport']['id'],
            'sport_name': team['sport']['name'],
            'sport_link': team['sport']['link'],
            'short_name': team['shortName'],
            'parent_org_name': team.get('parentOrgName'),
            'parent_org_id': team.get('parentOrgId'),
            'franchise_name': team.get('franchiseName'),
            'club_name': team.get('clubName'),
            'active': team['active'],
            }
           
        teams_lists.append(teams_dict)
    generic_insert_mlb('landing_area.teams', teams_lists)


def get_transactions():
    pass

def get_team_affiliates():
    pass

def get_game_play_by_play_outcomes(gamePk):
    url_endpoint = f'https://statsapi.mlb.com/api/v1/game/{gamePk}/winProbability'
    data = fetch_and_handle_data(url_endpoint)
    
    global play_outcome_list
    global play_by_play_list
    
    for item in data:
        play_outcome_dict = {
            'game_id': gamePk,
            'at_bat_index': item.get('about', {}).get('atBatIndex'),
            'result_type': item.get('result', {}).get('type'),
            'result_event': item.get('result', {}).get('event'),
            'event_type': item.get('result', {}).get('eventType'),
            'batter_player_id': item.get('matchup', {}).get('batter',{}).get('id'),
            'batter_player_full_name': item.get('matchup', {}).get('batter',{}).get('fullName'),
            'batSide': item.get('matchup', {}).get('batSide',{}).get('code'),
            'pitcher_player_id': item.get('matchup', {}).get('pitcher',{}).get('id'),
            'pitcher_player_full_name': item.get('matchup', {}).get('pitcher',{}).get('fullName'),
            'pitch_hand': item.get('matchup', {}).get('pitchHand',{}).get('code'),
            'splits_batter': item.get('matchup', {}).get('splits',{}).get('batter'),
            'splits_pitcher': item.get('matchup', {}).get('splits',{}).get('pitcher'),
            'splits_men_on_base': item.get('matchup', {}).get('splits',{}).get('menOnBase'),
            'result_description': item.get('result', {}).get('description'),
            'rbi': item.get('result', {}).get('rbi'),
            'away_score': item.get('result', {}).get('awayScore'),
            'home_score': item.get('result', {}).get('homeScore'),
            'is_out': item.get('result', {}).get('isOut'),
            'balls': item.get('count', {}).get('balls'),
            'strikes': item.get('count', {}).get('strikes'),
            'outs': item.get('count', {}).get('outs'),
            'half_inning': item.get('about', {}).get('halfInning'),
            'is_top_inning': item.get('about', {}).get('isTopInning'),
            'inning': item.get('about', {}).get('inning'),
            'start_time': item.get('about', {}).get('startTime'),
            'end_time': item.get('about', {}).get('endTime'),
            'is_complete': item.get('about', {}).get('isComplete'),
            'is_scoring_play': item.get('about', {}).get('isScoringPlay'),
            'has_review': item.get('about', {}).get('hasReview'),
            'has_out': item.get('about', {}).get('hasOut'),
            'captivating_index': item.get('about', {}).get('captivatingIndex'),
            'home_team_win_probability': item.get('homeTeamWinProbability'),
            'away_team_win_probability': item.get('awayTeamWinProbability'),
            'home_team_win_probability_added': item.get('homeTeamWinProbabilityAdded'),
        }
        
        for pitch in item.get('playEvents', {}):
            play_by_play_dict = {
                'game_id': gamePk,
                'at_bat_index': item.get('about', {}).get('atBatIndex'),
                'sequence_index': pitch.get('index'),
                'pitch_number': pitch.get('pitchNumber'),
                'start_time': pitch.get('startTime'),
                'end_time': pitch.get('endTime'),
                'is_pitch': pitch.get('isPitch'),
                'is_pitch': pitch.get('isSubstitution'),
                'play_type': pitch.get('type'),
                'batter_player_id': item.get('matchup', {}).get('batter',{}).get('id'),
                'batter_player_full_name': item.get('matchup', {}).get('batter',{}).get('fullName'),
                'pitcher_player_id': item.get('matchup', {}).get('pitcher',{}).get('id'),
                'pitcher_player_full_name': item.get('matchup', {}).get('pitcher',{}).get('fullName'),
                'pitch_description': pitch.get('details', {}).get('call', {}).get('description'),
                'pitch_code': pitch.get('details', {}).get('call', {}).get('code'),
                'details_description': pitch.get('details', {}).get('description'),
                'details_code': pitch.get('details', {}).get('code'),
                'details_event': pitch.get('details', {}).get('event'),
                'details_eventType': pitch.get('details', {}).get('eventType'),
                'is_scoring_play': pitch.get('details', {}).get('isScoringPlay'),
                'is_in_play': pitch.get('details', {}).get('isInPlay'),
                'is_strike': pitch.get('details', {}).get('isStrike'),
                'is_ball': pitch.get('details', {}).get('isBall'),
                'is_out': pitch.get('details', {}).get('isOut'),
                'has_review': pitch.get('details', {}).get('hasReview'),
                'from_catcher': pitch.get('details', {}).get('fromCatcher'),
                'disengagement_num': pitch.get('details', {}).get('disengagementNum'),
                'pitch_type_code': pitch.get('details', {}).get('type', {}).get('code'),
                'pitch_type_description': pitch.get('details', {}).get('type', {}).get('description'),
                'pitch_type_confidence': pitch.get('pitchData', {}).get('typeConfidence'),
                'count_balls': pitch.get('count', {}).get('balls',),
                'count_strikes': pitch.get('count', {}).get('strikes'),
                'count_outs': pitch.get('count', {}).get('outs'),
                'pre_count_balls': pitch.get('preCount', {}).get('balls',),
                'pre_count_strikes': pitch.get('preCount', {}).get('strikes'),
                'pre_count_outs': pitch.get('preCount', {}).get('outs'),
                'start_speed': pitch.get('pitchData', {}).get('startSpeed'),
                'end_speed': pitch.get('pitchData', {}).get('endSpeed'),
                'strike_zone_top': pitch.get('pitchData', {}).get('strikeZoneTop'),
                'strike_zone_bottom': pitch.get('pitchData', {}).get('strikeZoneBottom'),
                'strike_zone_width': pitch.get('pitchData', {}).get('strikeZoneWidth'),
                'strike_zone_depth': pitch.get('pitchData', {}).get('strikeZoneDepth'),
                'pitch_coordinates_aY': pitch.get('pitchData', {}).get('coordinates', {}).get('aY'),                
                'pitch_coordinates_aZ': pitch.get('pitchData', {}).get('coordinates', {}).get('aZ'),
                'pitch_coordinates_pfxX': pitch.get('pitchData', {}).get('coordinates', {}).get('pfxX'),
                'pitch_coordinates_pfxZ': pitch.get('pitchData', {}).get('coordinates', {}).get('pfxZ'),
                'pitch_coordinates_pX': pitch.get('pitchData', {}).get('coordinates', {}).get('pX'),
                'pitch_coordinates_pZ': pitch.get('pitchData', {}).get('coordinates', {}).get('pZ'),
                'pitch_coordinates_vX0': pitch.get('pitchData', {}).get('coordinates', {}).get('vX0'),
                'pitch_coordinates_vY0': pitch.get('pitchData', {}).get('coordinates', {}).get('vY0'),
                'pitch_coordinates_vZ0': pitch.get('pitchData', {}).get('coordinates', {}).get('vZ0'),
                'pitch_coordinates_x': pitch.get('pitchData', {}).get('coordinates', {}).get('x'),
                'pitch_coordinates_y': pitch.get('pitchData', {}).get('coordinates', {}).get('y'),
                'pitch_coordinates_x0': pitch.get('pitchData', {}).get('coordinates', {}).get('x0'),
                'pitch_coordinates_y0': pitch.get('pitchData', {}).get('coordinates', {}).get('y0'),
                'pitch_coordinates_z0': pitch.get('pitchData', {}).get('coordinates', {}).get('z0'),
                'pitch_coordinates_aX': pitch.get('pitchData', {}).get('coordinates', {}).get('aX'),
                'pitch_breaks_break_angle': pitch.get('pitchData', {}).get('breaks', {}).get('breakAngle'),
                'pitch_breaks_break_length': pitch.get('pitchData', {}).get('breaks', {}).get('breakLength'),
                'pitch_breaks_break_Y': pitch.get('pitchData', {}).get('breaks', {}).get('breakY'),
                'pitch_breaks_break_vertical': pitch.get('pitchData', {}).get('breaks', {}).get('breakVertical'),
                'pitch_breaks_break_vertical_induced': pitch.get('pitchData', {}).get('breaks', {}).get('breakVerticalInduced'),
                'pitch_breaks_break_horizontal': pitch.get('pitchData', {}).get('breaks', {}).get('breakHorizontal'),
                'pitch_zone': pitch.get('pitchData', {}).get('zone'),
                'pitch_plate_time': pitch.get('pitchData', {}).get('plateTime'),
                'pitch_extension': pitch.get('pitchData', {}).get('extension'),
            }
            
            play_by_play_list.append(play_by_play_dict)
        play_outcome_list.append(play_outcome_dict)

    # write_or_append_to_csv('csv/play_outcome.csv', play_outcome_list)
    # write_or_append_to_csv('csv/play_by_play.csv', play_by_play_list)

    
    pass 

def get_game_contextMetrics():
    pass


def get_game_changes():
    pass

def get_game_timestamps():
    pass

def get_game_diff():
    pass

def get_game_pace():
    pass 


def write_or_append_to_csv(file_path, dict_data_list):
    # Check if the file exists
    path_parts = file_path.split('/')
    directory_path = '/'.join(path_parts[:-1])
    
    os.makedirs(directory_path, exist_ok=True)
    file_exists = os.path.exists(file_path)
    
    # Open the file in append mode if it exists, or write mode if it doesn't
    mode = 'a' if file_exists else 'w'
    
    with open(file_path, mode, newline='') as csvfile:
        # Create a DictWriter object, fieldnames are taken from the keys of the provided dictionary
        writer = csv.DictWriter(csvfile, fieldnames=dict_data_list[0].keys())
        
        # If the file is new, write the header first
        if not file_exists:
            writer.writeheader()
        
        # Write the dictionary data as a row in the CSV file
        writer.writerows(dict_data_list)



def orchestrate():
    global game_summary_list
    global game_summaries_list
    global inning_list
    global game_total_list
    global team_game_batting_stats_list
    global team_game_pitching_stats_list
    global team_game_fielding_stats_list
    global game_player_info_list
    global player_game_batting_performance_list
    global player_game_pitching_performance_list
    global player_game_fielding_performance_list
    global player_season_stats_batting_list
    global player_season_stats_pitching_list
    global player_season_stats_fielding_list
    global play_outcome_list
    global play_by_play_list
    
    

    # start_date = datetime.date(2022,5,19)
    
    start_date = datetime.date(2024, 3, 23)

    end_date = datetime.date(2015, 1, 1)
    current_date = start_date
    
    while current_date >= end_date:
        print(current_date)
        
        games_found = get_game_summary_data(current_date,current_date, False)
        
        for attempt in range(10): 
            try:
                for game in games_found:
                    
                    get_game_summaries(game)
                    parse_linescore(game)
                    
                    parse_box_score(game)
                    try: 
                        get_game_play_by_play_outcomes(game)
                    except: 
                        continue
                batch_generic_insert_mlb('landing_area.mlb_game_summary', game_summary_list)
                batch_generic_insert_mlb('landing_area.game_summaries', game_summaries_list)
                batch_generic_insert_mlb('landing_area.game_team_totals', game_total_list)
                batch_generic_insert_mlb('landing_area.game_inning', inning_list)
                batch_generic_insert_mlb('landing_area.team_game_batting_stats', team_game_batting_stats_list)
                batch_generic_insert_mlb('landing_area.team_game_pitching_stats', team_game_pitching_stats_list)
                batch_generic_insert_mlb('landing_area.team_game_fielding_stats', team_game_fielding_stats_list)
                batch_generic_insert_mlb('landing_area.game_player_info', game_player_info_list)
                batch_generic_insert_mlb('landing_area.player_game_batting_performance', player_game_batting_performance_list)
                batch_generic_insert_mlb('landing_area.player_game_pitching_performance', player_game_pitching_performance_list)
                batch_generic_insert_mlb('landing_area.player_game_fielding_performance', player_game_fielding_performance_list)
                batch_generic_insert_mlb('landing_area.game_day_player_season_stats_batting_performance', player_season_stats_batting_list)
                batch_generic_insert_mlb('landing_area.game_day_player_season_stats_pitching_performance', player_season_stats_pitching_list)
                batch_generic_insert_mlb('landing_area.game_day_player_season_stats_fielding_performance', player_season_stats_fielding_list)
                batch_generic_insert_mlb('landing_area.play_outcome', play_outcome_list)
                batch_generic_insert_mlb('landing_area.play_by_play', play_by_play_list)



                write_or_append_to_csv('csv/mlb_game_summary.csv', game_summary_list)
                write_or_append_to_csv('csv/game_summaries.csv', game_summaries_list)
                write_or_append_to_csv('csv/game_team_totals.csv', game_total_list)
                write_or_append_to_csv('csv/game_inning.csv', inning_list)
                write_or_append_to_csv('csv/team_game_batting_stats.csv', team_game_batting_stats_list)
                write_or_append_to_csv('csv/team_game_pitching_stats.csv', team_game_pitching_stats_list)
                write_or_append_to_csv('csv/team_game_fielding_stats.csv', team_game_fielding_stats_list)
                write_or_append_to_csv('csv/game_player_info.csv', game_player_info_list)
                write_or_append_to_csv('csv/player_game_batting_performance.csv', player_game_batting_performance_list)
                write_or_append_to_csv('csv/player_game_pitching_performance.csv', player_game_pitching_performance_list)
                write_or_append_to_csv('csv/player_game_fielding_performance.csv', player_game_fielding_performance_list)
                write_or_append_to_csv('csv/game_day_player_season_stats_batting_performance.csv', player_season_stats_batting_list)
                write_or_append_to_csv('csv/game_day_player_season_stats_pitching_performance.csv', player_season_stats_pitching_list)
                write_or_append_to_csv('csv/game_day_player_season_stats_fielding_performance.csv', player_season_stats_fielding_list)
                write_or_append_to_csv('csv/play_outcome.csv', play_outcome_list)
                write_or_append_to_csv('csv/play_by_play.csv', play_by_play_list)

                break
            except Exception as e:
                # This block will execute if there's an exception in the try block
                print(f"An error occurred: {e}")
                print('error occured for ' + str(current_date))
                time.sleep(60)
                
                
        
        
        game_summary_list = []
        game_summaries_list = []
        inning_list = []
        game_total_list = []
        team_game_batting_stats_list = []
        team_game_pitching_stats_list = []
        team_game_fielding_stats_list = []
        game_player_info_list = []
        player_game_batting_performance_list = []
        player_game_pitching_performance_list = []
        player_game_fielding_performance_list = []
        player_season_stats_batting_list = []
        player_season_stats_pitching_list = []
        player_season_stats_fielding_list = []
        
        play_outcome_list = []
        play_by_play_list = []
        
        current_date += datetime.timedelta(days=-1)
    
# get_teams()
orchestrate()
# get_standings(103, 2023)

# get_game_winProbability(748112)

# parse_box_score(717804)
