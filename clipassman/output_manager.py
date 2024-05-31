import shutil


class OutputManager:

    @classmethod
    def print_text(cls, text='', symbol='-'):
        width = cls._get_term_width()
        text = f' {text} ' if text else ''
        print(text.center(width, symbol))

    @classmethod
    def _get_term_width(cls):
        return shutil.get_terminal_size()[0]
