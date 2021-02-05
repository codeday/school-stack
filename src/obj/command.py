from __future__ import annotations

from src.obj.modifier import Modifier


class Command:
    valid_commands = ["schools", "info", "quit"]

    def __init__(self, command: str, modifiers: dict[Modifier]):
        self.command = command
        self.modifiers = modifiers

    @staticmethod
    def is_valid(command_query: str) -> bool:
        pass

    @staticmethod
    def create_command(command_query: str) -> Command:
        pass
