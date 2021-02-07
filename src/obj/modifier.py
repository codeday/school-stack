from __future__ import annotations


class Modifier:
    valid_modifiers = ("schools", "info")

    def __init__(self, name: str, value):
        self.name = name
        if value == 'True':
            self.value = True
        elif value == 'False':
            self.value = False
        else:
            self.value = value

    @staticmethod
    def create_list_from_input(split_command: list[str]) -> list[Modifier]:
        modifiers_without_dashes = [s.replace('--', '', 2) for s in split_command if "--" in s]
        modifier_objects: list[Modifier] = []
        for modifier_string in modifiers_without_dashes:
            split_at_equal = modifier_string.split("=")
            modifier_objects.append(Modifier(split_at_equal[0], split_at_equal[1]))

        return modifier_objects
