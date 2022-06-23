from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in [pl.name for pl in self.players]:
            return f"Player {player_name} is not in the guild."

        for pl in self.players:
            if pl.name == player_name:
                self.players.remove(pl)
                pl.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        guild_info_result = f"Guild: {self.name}\n"
        for pl in self.players:
            guild_info_result += pl.player_info() + "\n"
        return guild_info_result.strip()
