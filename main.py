# main.py
# AetherEngine: Primary Execution Entry Point

from core.kernel import boot_system

def main():
    operator, mode = boot_system()
    print("-" * 50)
    print(f"Session Active: {operator} operating in {mode.upper()} environment.")
    print("Awaiting Day 2 Data Pipeline instructions...")
    print("-" * 50)

if __name__ == "__main__":
    main()
