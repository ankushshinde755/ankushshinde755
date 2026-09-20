#!/usr/bin/env python3
import sys
import time

CYAN = "\033[38;2;56;189;248m"
PURPLE = "\033[38;2;192;132;252m"
GREEN = "\033[38;2;74;222;128m"
BOLD = "\033[1m"
RESET = "\033[0m"

def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    print(f"\n{CYAN}{BOLD}┌─────────────────────────────────────────────────────────────┐{RESET}")
    print(f"{CYAN}{BOLD}│  ANKUSH SHINDE • Cloud Application Engineer @ Acquia        │{RESET}")
    print(f"{CYAN}{BOLD}└─────────────────────────────────────────────────────────────┘{RESET}\n")

def main():
    print_banner()
    
    typewriter(f"{PURPLE}{BOLD}=== OPERATIONAL PROFILE ==={RESET}")
    typewriter(f"{CYAN}• Role:{RESET} Cloud Application Engineer at {PURPLE}Acquia{RESET}")
    typewriter(f"{CYAN}• Focus:{RESET} DevOps, SRE, Cloud Infrastructure & Automation")
    typewriter(f"{CYAN}• Stack:{RESET} AWS, Docker, Kubernetes, Terraform, Python, Bash\n")

    typewriter(f"{PURPLE}{BOLD}=== CONNECT & LINKS ==={RESET}")
    print(f"  • {CYAN}LinkedIn:{RESET}  https://www.linkedin.com/in/ankush-shinde-58a67a14b/")
    print(f"  • {CYAN}GitHub:{RESET}    https://github.com/ankushshinde755")
    print(f"  • {CYAN}Portfolio:{RESET} https://ankushshinde755.github.io/\n")

    print(f"{GREEN}{BOLD}✓ Systems Online.{RESET}\n")

if __name__ == "__main__":
    main()
