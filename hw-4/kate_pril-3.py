class Warrior:
    __ranks_names = ("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                     "Master", "Greatest")
    __level = 1
    __experience = 100
    __rank = __ranks_names[0]
    __achievements = []

    def __init__(self):
        self.__achievements = []

    def _get_rank(self, level):
        return self.__ranks_names[level // 10]

    def _update_warrior(self):
        while self.__experience >= (self.__level + 1) * 100 and self.__level < 100:
            self.__level += 1
            self.__rank = self._get_rank(self.__level)

        if self.__level == 100:
            self.__experience = 10000

    def training(self, info):
        if info[2] <= self.__level:
            if self.__experience + info[1] <= 10000:
                self.__experience += info[1]
            else:
                self.__experience = 10000
            self._update_warrior()
            self.__achievements.append(info[0])
            return info[0]
        else:
            return "Not strong enough"

    def battle(self, enemy_level):
        a = self.__experience > 10000
        if enemy_level < 1 or enemy_level > 100:
            return "Invalid level"
        elif enemy_level <= self.__level:
            if self.__level - enemy_level >= 2:
                return "Easy fight"
            else:
                if self.__level - enemy_level == 1:
                    if not a:
                        self.__experience += 5
                else:
                    if not a:
                        self.__experience += 10
                self._update_warrior()
                return "A good fight"
        else:
            diff = enemy_level - self.__level
            if self.__ranks_names.index(self.__rank) < self.__ranks_names.index(
                    self._get_rank(enemy_level)) and diff >= 5:
                return "You've been defeated"
            else:
                if not a:
                    self.__experience += 20 * diff * diff
                self._update_warrior()
                return "An intense fight"

    @property
    def level(self):
        return self.__level

    @property
    def experience(self):
        return self.__experience

    @property
    def rank(self):
        return self.__rank

    @property
    def achievements(self):
        return self.__achievements
