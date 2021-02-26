from datetime import datetime
import psutil

def parse_case(cmd: str) -> str:
    return cmd.lower().strip()

def __replace_all__(cmd: str, to_replaces: tuple, replace_with: str) -> str:
    for to_replace in to_replaces:
        if cmd.startswith(to_replace + " "):
            cmd = cmd.replace(to_replace + " ", replace_with + " ")
        if " " + to_replace + " " in cmd:
            cmd = cmd.replace(" " + to_replace + " ", " " + replace_with + " ")
        if cmd.endswith(" " + to_replace):
            cmd = cmd.replace(" " + to_replace, " " + replace_with)
        if cmd == to_replace:
            cmd = cmd.replace(to_replace, replace_with)
    return cmd

def parse_abbr(cmd: str) -> str:
    if "'s " in cmd: cmd = cmd.replace("'s ", " is ")
    if "'r " in cmd: cmd = cmd.replace("'r ", " are ")
    cmd = __replace_all__(cmd, ["ur"], "your")
    cmd = __replace_all__(cmd, ["u"], "you")
    cmd = __replace_all__(cmd, ["r"], "are")
    cmd = __replace_all__(cmd, ["i'm"], "i am")
    cmd = __replace_all__(cmd, ["rn"], "right now")
    cmd = __replace_all__(cmd, ["okay", "ohk", "okke"], "ok")
    cmd = __replace_all__(cmd, ["wat"], "what")
    cmd = __replace_all__(cmd, ["gud"], "good")
    cmd = __replace_all__(cmd, ["bey", "bei"], "bye")
    return cmd.strip()

def parse_typing_errors(cmd: str) -> str:
    cmd = __replace_all__(cmd, ["waether"], "weather")
    cmd = __replace_all__(cmd, ["whats"], "what's")
    return cmd.strip()


def parse_punctuations(cmd: str) -> str:
    puncs = [",", "?"]
    letters = list(cmd)
    for punc in puncs:
        for i in range(len(letters)):
            if letters[i] == punc:
                try:
                    if not letters[i-1] == " ":
                        letters[i-1] += " "
                    if not letters[i+1] == " ":
                        letters[i+1] += " "
                except IndexError:
                    pass
    cmd = "".join(letter for letter in letters)
    return cmd.strip()


def parse_time() -> str:
    today_obj = datetime.now()
    today_str = today_obj.strftime("%d %b %Y, %a, %H:%M:%S")
    return today_str

def parse_battery_data() -> str:
    battery = psutil.sensors_battery()
    data = str(int(battery.percent)) + "%, "
    data += "Plugged in" if battery.power_plugged else "Not plugged in"
    return data

if __name__ == "__main__":
    parse_battery_data()