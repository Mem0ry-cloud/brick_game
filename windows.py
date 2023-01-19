class Window:
    pass


class MainMenuWindow(Window):
    pass


class CampaignMenuWindow(Window):
    pass


class LevelsMenuWindow(Window):
    pass


class MainGameWindow(Window):
    pass


class CreateMapWindow(Window):
    pass


class WindowMaster:
    def __init__(self):
        pass

    def start_MainMenuWindow(self):
        pass

    def start_CreateMapWindow(self, map=None):
        pass

    def start_MainGameWindow(self, map=None):
        pass

    def start_LevelsMenuWindow(self):
        pass

    def start_CampaignMenuWindow(self, unlocked_level=1):
        pass