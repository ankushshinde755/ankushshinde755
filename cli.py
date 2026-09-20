#!/usr/bin/env python3
import sys
import time

# ANSI Color Codes for Glassmorphism Cyber Palette
CYAN = "\033[38;2;56;189;248m"
PURPLE = "\033[38;2;192;132;252m"
GREEN = "\033[38;2;57;255;20m"
YELLOW = "\033[38;2;251;191;36m"
WHITE = "\033[1;37m"
GRAY = "\033[38;2;148;163;184m"
RESET = "\033[0m"

BANNER = f"""
{CYAN}┌────────────────────────────────────────────────────────────────────────┐
│  {WHITE}ANKUSH SHINDE{RESET} {GRAY}— Cloud Application Engineer @ Acquia{CYAN}                 │
│  {PURPLE}DevOps • Cloud Infrastructure • SRE • Big Data Platforms{CYAN}             │
└────────────────────────────────────────────────────────────────────────┘{RESET}
"""

INFO = f"""
{CYAN}⚡ OPERATIONAL PROFILE{RESET}
  {WHITE}Name:{RESET}       Ankush Shinde
  {WHITE}Current Role:{RESET} Cloud Application Engineer at {PURPLE}Acquia{RESET} (May 2021 – Present)
  {WHITE}Domain:{RESET}       Cloud Operations, Infrastructure as Code (IaC), Multi-Tenant SRE
  {WHITE}LinkedIn:{RESET}     {CYAN}https://www.linkedin.com/in/ankush-shinde-58a67a14b/{RESET}
  {WHITE}Portfolio:{RESET}    {CYAN}https://ankushshinde755.github.io/{RESET}

{PURPLE}💼 CAREER EXPERIENCE{RESET}
  {WHITE}1. Cloud Application Engineer{RESET} | {PURPLE}Acquia{RESET} {GRAY}(May 2021 – Present){RESET}
     • Managing enterprise cloud application environments, deployment infrastructure, and high availability.
     • Provisioning cloud resources via Terraform (IaC) across AWS multi-tenant environments.
     • Acting as technical frontline for enterprise incidents, platform stability, and SLA uptime.

  {WHITE}2. Customer Service Associate{RESET} | {CYAN}Amazon{RESET} {GRAY}(Sept 2020 – March 2021){RESET}
     • Resolved complex customer technical support inquiries across Prime, Shopping, and Fire TV platforms.

{GREEN}📜 CERTIFICATIONS & CREDENTIALS{RESET}
  {CYAN}AWS (Amazon Web Services):{RESET}
    • AWS Cloud Practitioner Essentials
    • Amazon S3 Glacier Certified
    • Advanced Testing Practices via AWS DevOps
    • DevOps on AWS & AWS Command Line Interface (CLI) Basics
    • Cloud Security Essentials & Generative AI for Executives

  {PURPLE}GCP, Azure & Acquia:{RESET}
    • GCP Transformer Models, BERT & LLM Introduction (Google Cloud)
    • Microsoft Certified: Cloud Computing & Azure AI
    • Acquia Talent Ambassador & Interviewer Certified

{YELLOW}🎓 EDUCATION{RESET}
  • {WHITE}Master of Computer Applications (MCA){RESET} — Sinhgad Institute of Management (SIOM), Pune (2017 – 2020)
  • {WHITE}Bachelor of Science (B.Sc. ECS){RESET} — Sahakar Maharshi College, Solapur University

{CYAN}🛠️ TECHNICAL STACK{RESET}
  • {WHITE}Cloud & IaC:{RESET}     AWS, GCP, Linux, Terraform, Docker, Teleport
  • {WHITE}Big Data:{RESET}        Snowflake, Apache Spark, Apache Hive, Cloudera, Oozie, AgilOne CDP
  • {WHITE}Observability:{RESET}   Splunk, Sumo Logic, LogicMonitor, Service Cloud
  • {WHITE}Languages:{RESET}       Python, Bash / Shell Scripting
"""

def print_help():
    print(f"""
{WHITE}Usage:{RESET} python3 cli.py [option]

{CYAN}Options:{RESET}
  {GREEN}--all, -a{RESET}         Display complete portfolio information
  {GREEN}--exp, -e{RESET}         Display work experience (Acquia, Amazon)
  {GREEN}--certs, -c{RESET}       Display AWS, GCP & Microsoft certifications
  {GREEN}--skills, -s{RESET}      Display technical stack
  {GREEN}--help, -h{RESET}        Show this help menu
""")

def main():
    print(BANNER)
    
    args = [arg.lower() for arg in sys.argv[1:]]
    
    if "--help" in args or "-h" in args:
        print_help()
        return

    if "--certs" in args or "-c" in args:
        print(f"{GREEN}📜 CERTIFICATIONS & CREDENTIALS{RESET}\n" + INFO.split("📜 CERTIFICATIONS & CREDENTIALS")[1].split("🎓 EDUCATION")[0])
        return

    if "--exp" in args or "-e" in args:
        print(f"{PURPLE}💼 CAREER EXPERIENCE{RESET}\n" + INFO.split("💼 CAREER EXPERIENCE")[1].split("📜 CERTIFICATIONS & CREDENTIALS")[0])
        return

    # Default output if no args or --all
    print(INFO)

if __name__ == "__main__":
    main()
