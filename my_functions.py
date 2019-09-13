class MyFunctions:

    def __init__():
        pass

    def _get_all_map_locations(game_state):
        '''Return a list of all legal positions on the map.'''
        legal_positions = []
        map_size = game_state.ARENA_SIZE
        is_even = (map_size % 2 == 0)
        mid_map = (map_size - 1 - is_even)/2
        for x in range(map_size):
            low_y = mid_map - x
            if (x > mid_map):
                low_y = x - mid_map - is_even
            high_y = map_size - low_y
            for y in range(low_y, high_y):
                legal_positions.append([x, y])
        return legal_positions

    def get_my_defenders(game_state):
        '''Return a list of positions.'''
        pass

    def get_enemy_defenders(game_state):
        '''Return a list of positions.'''
        pass

    def rate_my_attack_positions(game_state):
        '''For each attack position, return a list of how many defenders are in range at each step.'''
        pass

    def rate_enemy_attack_positions(game_state):
        '''For each attack position, return a list of how many defenders are in range at each step.'''
        pass

    def get_game_state_with_additional_blockers(game_state, blockers):
        '''Return the game state we would have if we added blockers at a given list of locations.'''
        pass
