class Tile:
    def __init__(self):
        self.bomb = False
        self.label = None
        self.visible = False
        self.flagged = False
        self.clicked = 0
        self.pressed = 0
        self.is_active = True
        self.visible_time = 0
        self.open_time =0
        self.visible_tiles_around = 0
        self.flaggeds = 0
        self.can_be_clicked = True
        self.false_flagged = False