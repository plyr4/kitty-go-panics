from kittens.tui.handler import result_handler
from kitty.boss import Boss
import sys
import re
import subprocess

def main(args: list[str]) -> str:
    data = sys.stdin.read()
    return data

@result_handler(type_of_input='text')
def handle_result(args: list[str], stdin_data: str, target_window_id: int, boss: Boss) -> None:
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        panic_regex = re.compile(
            r"(?P<function>[^\s()]+\(.*?\))\n\t(?P<file_path>[^\s:]+):(?P<line>\d+)"
        )
        try:
            matches = panic_regex.findall(stdin_data)
        except Exception as e:
            return

        if not matches:
            return

        top_match = matches[0]
        file_path = top_match[1].strip()
        line_number = top_match[2].strip()
        subprocess.run(["/usr/local/bin/code", "--goto", f"{file_path}:{line_number}"], check=True)
