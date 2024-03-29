class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai_game):
        """Initialize staticstics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statics that can change during the game"""
        self.ships_left = self.settings.ship_limit 
        self.score = 0
    
    