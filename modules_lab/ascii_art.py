from pyfiglet import figlet_format


def text_art(text: str):
    ascii_art = figlet_format(text)
    return ascii_art


print(text_art('Python 3.8'))