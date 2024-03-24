import requests 

import json


gamePk = str(413696)
# response = requests.get(f'https://statsapi.mlb.com/api/v1.1/{gamePk}/3456/feed/live') live feed of data 

# https://statsapi.mlb.com/api/v1/schedule?date=2024-02-27&sportId=1 to get the 



# response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/boxscore')

# response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?date=2015-04-10&sportId=1')
# Apr 11, 2015

# response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/linescore')

# startDate = '2023-05-01'
# endDate ='2023-05-29'
# response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?startDate={startDate}&endDate={endDate}&sportId=1')


# response = requests.get(f'https://statsapi.mlb.com/api/v1/game/718348/linescore')


# data = response.json()



# for day in data['dates']:
    
#     for game in day['games']:
#         print(game['link'])
        
#         print(game['teams']['away']['team']['name'])
#         print(game['teams']['away']['score'])
        
#         print(game['teams']['home']['team']['name'])
#         print(game['teams']['home']['score'])
        
        
    
#     for 
#     print()


# json_string = json.dumps(data, indent=4)


# with open('output2.json', 'w') as f:
#     json.dump(data, f, indent=4)
    
    
    
# find all the games that occured on that day
def find_games(start_date, end_date, today=False):
    if today:
        response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?sportId=1')
        # save_off_results(response)
        
        games_found = []
        data = response.json()
        
        games = data['dates'][0]['games']
        for game_info in games:
            game_pk = game_info['gamePk']
            game_guid = game_info['gameGuid']
            link = game_info['link']
            game_type = game_info['gameType']
            season = game_info['season']
            game_date = game_info['gameDate']
            official_date = game_info['officialDate']

            # Accessing team information
            away_team_name = game_info['teams']['away']['team']['name']
            # away_team_record = game_info['teams']['away']['leagueRecord']
            away_wins = game_info['teams']['away']['leagueRecord']['wins']
            away_losses = game_info['teams']['away']['leagueRecord']['losses']
            away_pct = game_info['teams']['away']['leagueRecord']['pct']
            away_team_score = game_info['teams']['away']['score']
            away_team_is_winner = game_info['teams']['away'].get('isWinner', False)

            home_team_name = game_info['teams']['home']['team']['name']
            # home_team_record = game_info['teams']['home']['leagueRecord']
            home_wins = game_info['teams']['home']['leagueRecord']['wins']
            home_losses = game_info['teams']['home']['leagueRecord']['losses']
            away_pct = game_info['teams']['home']['leagueRecord']['pct']
            home_team_score = game_info['teams']['home']['score']
            home_team_is_winner = game_info['teams']['home'].get('isWinner', False)

            # Accessing game state
            abstract_game_state = game_info['status']['abstractGameState']
            coded_game_state = game_info['status']['codedGameState']
            detailed_state = game_info['status']['detailedState']
            status_code = game_info['status']['statusCode']

        # Printing the extracted information
        print(f"Game PK: {game_pk}, Game GUID: {game_guid}")
        print(f"Link: {link}, Game Type: {game_type}, Season: {season}")
        print(f"Game Date: {game_date}, Official Date: {official_date}")
        print(f"Away Team: {away_team_name}, Record: {away_wins}-{away_losses}, Score: {away_team_score}, Winner: {away_team_is_winner}")
        print(f"Home Team: {home_team_name}, Record: {home_wins}-{home_losses}, Score: {home_team_score}, Winner: {home_team_is_winner}")
        print(f"Game State: {abstract_game_state}, {coded_game_state}, {detailed_state}, {status_code}")
    else:
        response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?startDate={start_date}&endDate={end_date}&sportId=1')



def get_line_score(game_pk, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/linescore')
    save_off_results(response, output)

def get_schedule(output , start_date='2023-05-03', end_date='2023-05-03'):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?startDate={start_date}&endDate={end_date}&sportId=1')
    save_off_results(response, output)

def get_standings(league_id, output, season=2024):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/standings?leagueId={league_id}&season={season}')
   
    save_off_results(response, output)
    
# def get_plays(game_pk):
#     pass

def get_box_score(gamePk, output):
    
    response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/boxscore')
    save_off_results(response, output)

def get_team_stats(teamId, season, group, output):
    # statGroups [{"displayName":"hitting"},{"displayName":"pitching"},{"displayName":"fielding"},{"displayName":"catching"},{"displayName":"running"},{"displayName":"game"},{"displayName":"team"},{"displayName":"streak"}]
    response = requests.get(f'https://statsapi.mlb.com/api/v1/teams/{teamId}/stats?season={season}&group={group}')

    save_off_results(response, output)

def get_live_feed(gamepk, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1.1/game/718348/feed/live')
    save_off_results(response, output)
    
def get_roster(team_id, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster')
    save_off_results(response, output)
     
def get_player(player_id, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/people/{player_id}')
    save_off_results(response, output)

def get_teams(output):
    #   "sport": {  "id": 1,
    response = requests.get(f'https://statsapi.mlb.com/api/v1/teams')
    save_off_results(response, output)
    
    
def get_play_by_play(gamePk, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/playByPlay')
    save_off_results(response, output)



def get_transactions(teamId, output):
    #   "sport": {  "id": 1,
    response = requests.get(f'https://statsapi.mlb.com/api/v1/transactions?teamId={teamId}')
    save_off_results(response, output)


def get_win_probability(gamePk, output):
    response = requests.get(f'https://statsapi.mlb.com/api/v1/game/{gamePk}/winProbability')
    save_off_results(response, output)



    
def save_off_results(response, output):
    data = response.json()

    with open( output + '.json', 'w') as f:
        json.dump(data, f, indent=4)
        
        
def cordinate():
    game_ids = find_games('123', '123', today=True)
    for game_id in game_ids:
        get_box_score(game_id, f'data/{game_id}.json')
        

# leagueId="103,104",
#     division="all",
#     include_wildcard=True,
#     season=None,
#     standingsTypes=None,
#     date=None,


# get_line_score('748133', 'get_line_score')
# get_schedule('get_schedule')
# get_standings('103','get_standings', '2023')
# get_box_score('748133','get_box_score')
# get_team_stats('141', '2023', 'hitting', 'get_team_stats')
# get_live_feed('748112', 'get_live_feed')
get_win_probability('748112', 'get_win_probability')
# get_roster('134','get_roster')
# get_player('656582', 'get_player')

# get_teams('get_teams')
# get_transactions('134', 'get_transactions')
# get_play_by_play('748112','get_play_by_play')

