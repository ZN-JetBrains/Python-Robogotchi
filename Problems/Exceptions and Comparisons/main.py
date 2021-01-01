class WordError(Exception):
    def __str__(self):
        return "Word Error!"


def check_w_letter(word):
    if "w" in word:
        raise WordError
    else:
        return word
