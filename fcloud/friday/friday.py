import random

from .dictionary import questions, default_ans, greet, ty_replies, emoji, time_greet
from . import scrapers
from . import utils
from . import parsers

class Friday:

    __cmd__ = str()
    __reply__ = str()

    @classmethod
    def listen(self, cmd: str) -> None:
        self.__cmd__ = cmd
        self.__read__(self.__cmd__)
        self.__reply__ = self.__think__(self.__cmd__)

    @classmethod
    def reply(self) -> str:
        return self.__reply__[0].upper() + self.__reply__[1:]

    @classmethod
    def __read__(self, cmd: str) -> None:
        self.__cmd__ = parsers.parse_case(self.__cmd__)
        self.__cmd__ = parsers.parse_punctuations(self.__cmd__)
        self.__cmd__ = parsers.parse_typing_errors(self.__cmd__)
        self.__cmd__ = parsers.parse_abbr(self.__cmd__)

    @classmethod
    def __think__(self, cmd: str) -> str:
        ret = utils.calculator(self.__cmd__)
        if ret is not None:
            return ret
        if cmd.startswith("say "):
            return cmd.replace("say ", "")
        if "thank" in cmd:
            return f"{ty_replies[random.randint(0, len(ty_replies) - 1)]}, Sir {emoji.smile_with_teeth}"
        if all([i in cmd for i in ["what", "time"]]):
            return parsers.parse_time()
        if all([i in cmd for i in ["what", "battery"]]):
            return parsers.parse_battery_data()
        if all([i in cmd for i in ["what", "weather"]]):
            return scrapers.get_weather_data()
        if all([i in cmd for i in ["what", "github"]]):
            return scrapers.get_github_data()
        if any([
                all([i in cmd for i in ["cricket", "matches"]]),
                all([i in cmd for i in ["cricket", "match"]]),
                all([i in cmd for i in ["when", "india", "match"]])
            ]):
            return scrapers.get_cricket_data()
        if any([cmd.startswith(i) for i in questions]):
            return scrapers.get_wiki_data(cmd)
        if any([i in cmd for i in time_greet]):
            smilies = [emoji.excited_smile, emoji.happy_smile]
            for item in time_greet:
                if item in cmd:
                    return item.capitalize() + f" {smilies[random.randint(0, len(smilies) - 1)]} !"
        if any([i in cmd for i in greet]):
            smilies = [emoji.excited_smile, emoji.happy_smile]
            return greet[random.randint(0, len(greet) - 1)] + f" {smilies[random.randint(0, len(smilies) - 1)]} !"
        ret = utils.common_msgs(self.__cmd__)
        if ret is not None:
            return ret
        if "bye" in cmd:
            return f"Bye, See you soon. {emoji.happy_smile}"
        return default_ans[random.randint(0, len(default_ans) - 1)]



if __name__ == "__main__":
    Friday.listen("what's the time")
    print(Friday.reply())
