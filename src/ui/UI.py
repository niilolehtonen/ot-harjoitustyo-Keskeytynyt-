from logging import root
from ui.generator_view import GeneratorView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_GeneratorView()

    def _show_GeneratorView(self):
        self._current_view = GeneratorView(
            self._root
        )

        self._current_view.pack()

