#!/usr/bin/env python3
import sys
import time

# --- ANSI COLOR CODES ---
CYAN = "\033[38;2;56;189;248m"
PURPLE = "\033[38;2;192;132;252m"
GREEN = "\033[38;2;74;222;128m"
BOLD = "\033[1m"
RESET = "\033[0m"
DIM = "\033[2m"

def typewriter(text, delay=0.015):
    """Prints text with a subtle typewriter animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():a
    banner = f"""
{CYAN}{BOLD}┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   ██ font  ANKUSH SHINDE                                    │
│   Cloud Application Engineer @ Acquia                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘{RESET}
"""
    print(banner)

def show_about():
    print(f"\n{PURPLE}{BOLD}=== 👨‍💻 ABOUT ME ==={RESET}")
    typewriter(f"{CYAN}• Role:{RESET} Cloud Application Engineer at {PURPLE}Acquia{RESET}")
    typewriter(f"{CYAN}• Core Focus:{RESET} DevOps, SRE, Cloud Infrastructure & Automation")
    typewriter(f"{CYAN}• Mission:{RESET} Building high-availability, scalable application pipelines")
    typewriter(f"{CYAN}• Location:{RESET} India 🇮🇳\n")

def show_stack():
    print(f"\n{PURPLE}{BOLD}=== ⚡ TECH STACK & TOOLS ==={RESET}")
    print(f"  {CYAN}Cloud & Infrastructure:{RESET} AWS, Docker, Kubernetes, Terraform")
    print(f"  {CYAN}CI/CD & DevOps:{RESET} GitHub Actions, Jenkins, Shell Scripting")
    print(f"  {CYAN}Languages:{RESET} Python, Bash, JavaScript / Node.js")
    print(f"  {CYAN}Monitoring & Ops:{RESET} Prometheus, Grafana, Datadog\n")

def show_projects():
    print(f"\n{PURPLE}{BOLD}=== 🚀 FEATURED PROJECTS ==={RESET}")
    print(f"  1. {CYAN}GitHub Profile & Automation Utilities{RESET}")
    print(f"     https://github.com/ankushshinde755/ankushshinde755")
    print(f"  2. {CYAN}The Gym Web Platform{RESET}")
    print(f"     https://github.com/ankushshinde755/The-Gym\n")

def show_connect():
    print(f"\n{PURPLE}{BOLD}=== 🌐 CONNECT WITH ME ==={RESET}")
    print(f"  • {CYAN}LinkedIn:{RESET}  https://www.linkedin.com/in/ankush-shinde-58a67a14b/")
    print(f"  • {CYAN}GitHub:{RESET}    https://github.com/ankushshinde755")
    print(f"  • {CYAN}Portfolio:{RESET} https://ankushshinde755.github.io/\n")

def main():
    print_banner()
    show_about()
    show_stack()
    show_projects()
    show_connect()

    print(f"{GREEN}{BOLD}✓ Thanks for visiting my interactive CLI profile!{RESET}\n")

if __name__ == "__main__":
    main()
