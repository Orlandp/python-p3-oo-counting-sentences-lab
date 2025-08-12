#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value: str = ""):
        self._value = ""
        self.value = value  # use setter for validation

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            # The tests expect this exact message (and no exception)
            print("The value must be a string.")

    # --- methods required by the tests ---

    def is_sentence(self) -> bool:
        return self.value.endswith(".")

    def is_question(self) -> bool:
        return self.value.endswith("?")

    def is_exclamation(self) -> bool:
        return self.value.endswith("!")

    def count_sentences(self) -> int:
        """
        Count sentences separated by ., !, or ?.
        Treat runs like '!!', '??', '...' as one separator.
        Ignore empty chunks from leading/trailing punctuation/whitespace.
        """
        if not self.value.strip():
            return 0

        parts = re.split(r"[.!?]+", self.value)
        sentences = [p.strip() for p in parts if p.strip()]
        return len(sentences)
