from colorama import init, Fore, Style
from .calculator import Calculator
from .observers import LoggingObserver, AutoSaveObserver
from .persistence import save_history, load_history

def main():
    init(autoreset=True)
    calc = Calculator()
    log_obs = LoggingObserver()
    auto_obs = AutoSaveObserver(); auto_obs.history_provider = calc.items
    calc.register(log_obs); calc.register(auto_obs)

    print("Enhanced Calculator. Type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            cmd = input("> ").strip()
            if not cmd: continue
            if cmd == "exit": print("bye!"); break
            if cmd == "help":
                print("commands: add subtract multiply divide power root modulus int_divide percent abs_diff")
                print("history | clear | undo | redo | save | load | help | exit")
                continue
            if cmd == "history":
                for c in calc.items():
                    print(f"{c.timestamp} {c.operation}({c.a},{c.b}) = {c.result}")
                continue
            if cmd == "clear": calc.clear(); print("history cleared"); continue
            if cmd == "undo": print("undid:", calc.undo()); continue
            if cmd == "redo": print("redid:", calc.redo()); continue
            if cmd == "save": save_history(calc.items()); print("saved"); continue
            if cmd == "load":
                items = load_history(); calc.clear()
                for c in items: calc.history.push(c)
                print(f"loaded {len(items)}")
                continue

            parts = cmd.split()
            op, a, b = parts[0], float(parts[1]), float(parts[2])
            c = calc.perform(op,a,b)
            print(Fore.GREEN + str(c.result))
        except Exception as e:
            print(Fore.RED + f"error: {e}")

if __name__ == "__main__":
    main()  # pragma: no cover
