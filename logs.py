import json


class Logs():
    def __init__(self) -> None:
        self.logs = []
        self.moves = 0

    def log_move(self, player, row, column, game_state):
        move_info = {
            'move_number' : self.moves,
            'player' : player,
            'move' : (row, column),
            'game_state' : game_state
        }
        self.moves += 1
        self.logs.append(move_info)



    def download_logs(self):
        with open('logs.json', 'w') as json_file:
            json.dump(self.logs, json_file, indent = 4)