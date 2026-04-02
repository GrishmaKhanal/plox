import sys
from pathlib import Path


def run_file(path: str) -> None:
    source = Path(path).read_text(encoding='utf-8')
    run(source)

def run_prompt() -> None:
    try:
        while True:
            line = input("> ")
            if line == 'exit()':
                break
            run(line)
    except EOFError:
        print(f"Exited!")
    except KeyboardInterrupt:
        print()
        print("KEYBOARD INTERRUPT")
        run_prompt()

def run(source: str) -> None:
    # placeholder
    print(source)

def main() -> None:
    args = sys.argv[1:]
    if len(args) > 1:
        print("Usage: plox [script]")
        # 64 -> command line usage error
        sys.exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_prompt()

if __name__ == "__main__":
    main()
