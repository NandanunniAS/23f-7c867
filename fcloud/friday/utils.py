from math import radians, cos, sin, asin, sqrt, log


def common_msgs(cmd: str):
    if "ok" in cmd and "bye" not in cmd:
        return "Okay !"
    return None


def calculator(cmd: str):
    ops = ["+", "-", "/", "*", "**"]
    ops.extend(["sin", "cos", "tan", "log", "sqrt"])
    exp = cmd.replace(" ", "")
    exp = exp.replace("^", "**")
    try:
        val = f"{cmd} = {round(eval(exp), 5)}"
        return val
    except (SyntaxError, NameError):
        return None


def get_distance_btw(d1, d2) -> str: 
    # deg -> rad
    d1[1] = radians(d1[1])
    d2[1] = radians(d2[1])
    d1[0] = radians(d1[0])
    d2[0] = radians(d2[0])

    # Haversine formula  
    dlon = d2[1] - d1[1]
    dlat = d2[0] - d1[0]
    c = 2 * asin(sqrt(sin(dlat / 2)**2 + cos(d1[0]) * cos(d2[0]) * sin(dlon / 2)**2))

    # radius of earth = 6371 km or 3956 miles
    d = c * 6371 * 1000

    if d > 1000:
        distance = str(d / 1000) + " km"
    else:
        distance = str(d) + " m"
    return distance
