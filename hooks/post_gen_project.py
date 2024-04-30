#!/usr/bin/env python

import subprocess
import sys


def execute_cmd(cmd: list[str]) -> int:
    print(f">> {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
    return result.returncode


def main() -> int:
    cmd = ["git", "init"]
    if (rc := execute_cmd(cmd)) != 0:
        return rc

    cmd = ["git", "remote", "add", "origin", "{{ cookiecutter.repo_url_ssh }}"]
    if (rc := execute_cmd(cmd)) != 0:
        return rc

    cmd = ["git", "add", "."]
    if (rc := execute_cmd(cmd)) != 0:
        return rc

    cmd = ["git", "commit", "-m", "feat: initialize project"]
    if (rc := execute_cmd(cmd)) != 0:
        return rc

    return 0


if __name__ == "__main__":
    exit(main())
