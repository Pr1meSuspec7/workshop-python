
def colortext(text, color=None):
    '''Ex: print(colortext('some string', 'cyan'))'''
    COLORS = {'grey': 30, 'red': 31, 'green': 32, 'yellow': 33,
          'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}
    RESET = '\033[0m'
    ascii_color = '\033[1;%dm%s'
    if color is not None:
        # Modulo (%) operator works in this way:
        # COLORS[color] replaces %d and text replaces %s
        text = ascii_color % (COLORS[color], text)
    text += RESET
    return text


#####################################################################


if __name__ == "__main__":

    rosso = '\033[1;31m'
    blu = '\033[1;34m'
    verde = '\033[1;32m'
    verde = '\033[1;33m'
    reset = '\033[0m'

    print("")
    print('\033[1;31mTesto colorato manualmente di rosso\033[0m')
    print('\033[1;34mTesto colorato manualmente di blu\033[0m')
    print('\033[1;32mTesto colorato manualmente di verde\033[0m')
    print("")
    print(colortext("Testo colorato di rosso con la funziona colortext", "red"))
    print(colortext("Testo colorato di blu con la funziona colortext", "blue"))
    print(colortext("Testo colorato di verde con la funziona colortext", "green"))
    print("")
