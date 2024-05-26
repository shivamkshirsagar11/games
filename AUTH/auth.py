import json
import hashlib
from uuid import uuid4
class Auth:
    players = {}
    current_player=None
    def __init__(self, parent=''):
        self.parent = parent
        try:
            with open(f"{parent}\\players.json", 'r') as jsonfile:
                self.players = json.load(jsonfile)
        except Exception as e:
            print("[auth][loading players] Error:", e)
    
    def __enter__(self):
        return self

    def __exit__(self,exc_type, exc_value, trace):
        with open(f"{self.parent}\\players.json", 'w') as jsonfile:
                json.dump(self.players, jsonfile, indent=4)
                print("Session ended...")

    def add_player(self, player):
        player['password'] = self.get_hash(player['password'])
        _id = str(uuid4())[-5:]
        db_obj = {_id:player}
        self.players.update(db_obj)
        return _id
    
    def get_hash(self, word=''):
        word = word.encode('utf-8')
        hasho = hashlib.sha512(word)
        return hasho.hexdigest()

    def login(self, player):
        player['password'] = self.get_hash(player['password'])
        if player['id'] in self.players and player['password'] == self.players[player['id']]['password']:
            self.current_player = player
            return True
        return False
    
    def delete_player(self):
        if self.current_player['id'] in self.players:
            self.players.pop(self.current_player)
        return True