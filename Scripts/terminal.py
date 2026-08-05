import subprocess

def run_command(
        command:str,
        working_dir:str = None
    ) -> bool:

    print(f"[INFO] Executing: {command}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=False,
        cwd=working_dir
    )
    
    if result.stdout.strip():
        print(result.stdout.strip())

    if result.stderr.strip():
        print(result.stderr.strip())

    if result.returncode != 0:
        print(f"[ERROR] Command failed: {command}")
        return False
    
    return True

def run_commands(
        commands:list,
        working_dir:str = None
    ) -> bool:
    
    okay = True

    for command in commands:
        okay &= run_command(command, working_dir)

    return okay
