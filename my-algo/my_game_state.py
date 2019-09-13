import gamelib


class MyGameState(gamelib.AdvancedGameState):

    def _get_all_map_locations(self):
        '''Return a list of all legal positions on the map.'''
        return list(self.game_map)

    def _get_defenders(self, player):
        '''Return a list of defenders for a given player.'''
        defenders = []
        for location in self.game_map:
            unit = self.contains_stationary_unit(location)
            if unit and (unit.player_index == player):
                defenders.append(unit)
        return defenders

    def get_all_defenders(self):
        '''Return two lists of positions, one for my defenders and one for the enemy's.'''
        my_defenders = self._get_defenders(0)
        enemy_defenders = self._get_defenders(1)
        return my_defenders, enemy_defenders

    def rate_my_attack_positions(self):
        '''For each attack position, return a list of how many defenders are in range at each step.'''
        pass

    def rate_enemy_attack_positions(self):
        '''For each attack position, return a list of how many defenders are in range at each step.'''
        pass

    def get_game_state_with_additional_blockers(self, blockers):
        '''Return the game state we would have if we added blockers at a given list of locations.'''
        pass
