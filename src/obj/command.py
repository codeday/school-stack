from __future__ import annotations

from src.obj.modifier import Modifier


class Command:
    valid_commands = ["schools", "info", "quit"]

    def __init__(self, command: str):
        self.command = command
        self.split_command = command.split(" ")
        self.modifiers = [s for s in self.split_command if "--" in s]

    def is_valid(self) -> bool:
        pass

    @staticmethod
    def create_command(command_query: str) -> Command:
        pass

    def execute(self):
        pass
