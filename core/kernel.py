# core/kernel.py
# AetherEngine: Core System Initialization Module
# Day 1: Foundational Variables, Data Capture, and Environment Diagnostics

SYSTEM_NAME = "AetherEngine"
VERSION = "0.1.0-alpha"
AUTHOR = "Muhammad Nahid"

def boot_system():
    print("=" * 50)
    print(f"System Booting: {SYSTEM_NAME} [v{VERSION}]")
    print(f"Lead Architect: {AUTHOR}")
    print("=" * 50)

    operator_id = input("Enter Operator ID (Your Name): ")
    environment_mode = input("Select Mode (Dev / Production / Research): ")

    print("\n[System] Initializing Core Memory Space...")
    print(f"[System] Welcome, Operator {operator_id}.")
    print(f"[System] AetherEngine locked in '{environment_mode.upper()}' mode.")
    print("[System] Core engine status: ONLINE & LISTENING.\n")

    return operator_id, environment_mode
