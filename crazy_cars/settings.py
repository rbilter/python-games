from pathlib import Path


class GameSettings():
    def __init__(self, assets):
        self.__settings_file = Path(assets + '/settings.txt')
        self.__high_score = 0
        self.__load_high_score()

    def get_high_score(self):
        return self.__high_score

    def set_high_score(self, score):
        changed = False
        if self.__high_score < score:
            self.__high_score = score

            with open(self.__settings_file, 'w') as f:
                f.write(str(self.__high_score))
            f.close()

            changed = True
        return changed

    def __load_high_score(self):
        self.__settings_file.touch(exist_ok=True)
        with open(self.__settings_file) as f:
            hs = f.readline()
            if len(hs) > 0:
                self.__high_score = int(hs)
        f.close()
