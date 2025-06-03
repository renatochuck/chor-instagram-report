import time
import random
import sys
import re
from colorama import Fore, Style, init
import os

init(autoreset=True)

# === Hacker Black Hat Face Banner ===
def print_blackhat_face():
    face = r"""
              ▄███████████▄
           ▄███▀▀▀       ▀▀▀███▄
        ▄██▀                 ▀██▄
      ▄█▀     ▄▄▄▄▄▄▄▄▄▄▄     ▀█▄
     █▀     ███████████████     ▀█
    █      █████████████████     █
   █      █████▀▀▀▀▀▀▀▀█████▌     █
  █▌     ▐███▀          ▀███▌     ▐█
  █▌     ███   ▄▄▄▄▄▄    ███▌     ▐█
  █      ███  ████████   ███      █
  █      ▀██▄  ▀▀▀▀▀▀   ▄██▀      █
   █       ▀██▄▄▄▄▄▄▄▄▄██▀       █
    ▀█▄                   ▄▄   ▄█▀
      ▀█▄▄              ▄▄█▀ ▄█▀
         ▀▀███▄▄▄▄▄▄▄▄███▀▀
              ▀▀▀▀▀▀▀▀
        ☠ chor-instagram-report ☠
"""
    print(Fore.RED + face + Style.RESET_ALL)

# === CHOR Banner (only shown once) ===
def print_chor_banner():
    banner = r"""
   ██████  ██   ██  ██████  ██████  ██████  
  ██      ██   ██ ██      ██    ██ ██   ██ 
  ██      ███████ ██      ██    ██ ██████  
  ██      ██   ██ ██      ██    ██ ██   ██ 
   ██████ ██   ██  ██████  ██████  ██   ██ 
                                            
 ██████   █████  ██████   ██████  ██████  
██      ██   ██ ██   ██ ██    ██ ██   ██ 
██      ███████ ██████  ██    ██ ██████  
██      ██   ██ ██   ██ ██    ██ ██   ██ 
 ██████ ██   ██ ██   ██  ██████  ██   ██ 
"""
    print(Fore.GREEN + banner + Style.RESET_ALL)

# === Clear CHOR banner only ===
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# === Fake data generators ===
def fake_ip():
    return "{}.{}.{}.{}".format(
        random.randint(1, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def fake_location():
    return random.choice([
        "New York, USA", "Mumbai, India", "Berlin, Germany", "Tokyo, Japan",
        "Cape Town, South Africa", "Sydney, Australia", "Toronto, Canada",
        "Moscow, Russia", "São Paulo, Brazil", "London, UK"
    ])

def fake_status():
    return random.choice(["Active", "Suspicious", "Flagged", "Disabled", "Under Review"])

def fake_report_type():
    return random.choice([
        "Spam/Bot", "Impersonation", "Hate Speech", "Fake Account",
        "Harassment", "Scam", "Copyright Violation"
    ])

def fake_account_age():
    return f"{random.randint(1, 10)} year(s)"

def fake_follower_count():
    return f"{random.randint(100, 1000000)} followers"

def fake_device():
    return random.choice(["iPhone 14", "Samsung Galaxy S22", "Google Pixel", "Desktop", "MacBook Pro", "Linux Terminal"])

# === Print the progress bar ===
def print_progress_bar(current, total, bar_length=40):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(Fore.CYAN + f"[{bar}]  Reporting Account... [{current}/{total}]" + Style.RESET_ALL)

# === Print details for each fake report ===
def print_report_details(username):
    print(Fore.YELLOW + f"   > Target Username: @{username}")
    print(Fore.CYAN + f"   > IP Found: {fake_ip()}")
    print(Fore.GREEN + f"   > Location: {fake_location()}")
    print(Fore.MAGENTA + f"   > Account Status: {fake_status()}")
    print(Fore.RED + f"   > Report Type: {fake_report_type()}")
    print(Fore.BLUE + f"   > Device Used: {fake_device()}")
    print(Fore.WHITE + f"   > Account Age: {fake_account_age()}")
    print(Fore.LIGHTCYAN_EX + f"   > Follower Count: {fake_follower_count()}")
    print()

# === Extract username from input (username or URL) ===
def extract_username(input_str):
    input_str = input_str.strip()
    pattern = r"(?:https?://)?(?:www\.)?instagram\.com/([a-zA-Z0-9_.]+)/?"
    match = re.match(pattern, input_str)
    if match:
        return match.group(1)
    if re.match(r'^[a-zA-Z0-9_.]+$', input_str):
        return input_str
    return None

# === Simulate reporting of a single username multiple times ===
def simulate_reports(username, total_reports=10, delay=1.5):
    print("\nInitializing CHOR Instagram Account Reporting Tool...\n")
    print("Connecting to Instagram servers...")
    time.sleep(1.2)
    print("Bypassing API authentication...")
    time.sleep(1.2)
    print("Spoofing IP address and encrypting traffic...\n")
    time.sleep(1.5)

    for i in range(1, total_reports + 1):
        print_progress_bar(i, total_reports)
        print_report_details(username)
        time.sleep(delay)

    print(Fore.GREEN + "[✓] All reports submitted successfully!" + Style.RESET_ALL)
    print(Fore.RED + "[!] Instagram account flagged and under review..." + Style.RESET_ALL)
    print(Fore.YELLOW + "[!] THis is for ethical hacking education only." + Style.RESET_ALL)
    time.sleep(1)
    print_blackhat_face()

# === Simulate reporting multiple accounts ===
def simulate_multiple_accounts(usernames, total_reports_per_user=5, delay=1):
    print("\nStarting multi-account report...\n")
    for idx, username in enumerate(usernames, 1):
        print(Fore.MAGENTA + f"Reporting account {idx}/{len(usernames)}: @{username}" + Style.RESET_ALL)
        simulate_reports(username, total_reports=total_reports_per_user, delay=delay)

# === Simulate mass report ===
def simulate_mass_report(usernames, total_reports_per_user=3, delay=0.5):
    print("\nStarting MASS REPORT mode...\n")
    for idx, username in enumerate(usernames, 1):
        print(Fore.MAGENTA + f"[{idx}/{len(usernames)}] Mass reporting @{username}" + Style.RESET_ALL)
        for i in range(1, total_reports_per_user + 1):
            print_progress_bar(i, total_reports_per_user)
            print_report_details(username)
            time.sleep(delay)
    print(Fore.GREEN + "[✓] Mass report completed!" + Style.RESET_ALL)
    print_blackhat_face()

# === Load usernames from file ===
def load_usernames_from_file(filename):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except Exception as e:
        print(Fore.RED + f"Error loading file: {e}" + Style.RESET_ALL)
        return []

# === Main Menu ===
def main_menu():
    clear_screen()
    print_chor_banner()

    while True:
        print(Fore.WHITE + """
Choose an option:
1. Report a single Instagram username
2. Report using Instagram profile link
3. Report multiple accounts (enter usernames)
4. Mass report from usernames file
5. Exit
""" + Style.RESET_ALL)
        choice = input("Enter your choice [1-5]: ").strip()

        if choice == '1':
            username = input("Enter Instagram username to report: ").strip()
            username = extract_username(username)
            if username:
                simulate_reports(username)
            else:
                print(Fore.RED + "Invalid username." + Style.RESET_ALL)

        elif choice == '2':
            link = input("Enter Instagram profile link to report: ").strip()
            username = extract_username(link)
            if username:
                simulate_reports(username)
            else:
                print(Fore.RED + "Invalid Instagram URL." + Style.RESET_ALL)

        elif choice == '3':
            print("Enter usernames one by one. Type 'done' to finish.")
            usernames = []
            while True:
                u = input(f"Username {len(usernames)+1}: ").strip()
                if u.lower() == 'done':
                    break
                uname = extract_username(u)
                if uname:
                    usernames.append(uname)
                else:
                    print(Fore.RED + "Invalid username, try again." + Style.RESET_ALL)
            if usernames:
                simulate_multiple_accounts(usernames)
            else:
                print(Fore.RED + "No valid usernames entered." + Style.RESET_ALL)

        elif choice == '4':
            filename = input("Enter the filename containing usernames (one per line): ").strip()
            usernames = load_usernames_from_file(filename)
            if usernames:
                simulate_mass_report(usernames)
            else:
                print(Fore.RED + "No usernames loaded from file." + Style.RESET_ALL)

        elif choice == '5':
            print(Fore.CYAN + "Exiting CHOR Report Simulator. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number from 1 to 5." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
