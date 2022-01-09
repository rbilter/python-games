from pathlib import Path


class GameSettings():
    def __init__(self):
        self.settings_file = Path('assets/settings.txt')

    def get_high_score(self):
        high_score = 0
        self.settings_file.touch(exist_ok=True)
        with open(self.settings_file) as f:
            hs = f.readline()
            if len(hs) > 0:
                high_score = int(hs)
        f.close()
        return high_score

    def set_high_score(self, score):
        with open(self.settings_file, 'w') as f:
            f.write(str(score))
        f.close()
