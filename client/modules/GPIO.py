WORDS = ["DIM", "OFF", "LIGHT","FAN","ON","FAST","BRIGHT"]

def isValid(text):
    return bool(re.search(r'\bturn on light\b', text, re.IGNORECASE))
