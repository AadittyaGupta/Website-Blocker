import os
import time

# Normalize the website URL by removing "www." prefix if present.
def normalize_website(site):
    if site.startswith("www."):
        return site[4:]  
    return site 

# Block a specific website by adding its entry to the hosts file.
def block_website(site):
    site = normalize_website(site)  
    hosts_path = "/etc/hosts"  
    redirect = "127.0.0.1"  

    # The two entries we want to add: one for 'site' and one for 'www.site'
    entry = f"{redirect} {site}\n"
    entry_www = f"{redirect} www.{site}\n"

    try:
        # Open the hosts file in read-write mode
        with open(hosts_path, 'r+') as file:
            content = file.read()  
            
            # If the site is not already blocked, add it to the file
            if entry.strip() not in content and entry_www.strip() not in content:
                if not content.endswith('\n'):
                    file.write('\n')  
                file.write(entry)  
                file.write(entry_www)  
                print(f"{site} has been blocked.")
            else:
                print(f"{site} is already blocked.")
    except Exception as error:
        print(f"Error: {error}")  

# Block multiple websites from a file (each website in a new line)
def block_sites_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            sites = file.readlines()  
            for site in sites:
                block_website(site.strip())  
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  
    except Exception as error:
        print(f"Error: {error}")  

# Print the list of blocked websites by reading the hosts file
def print_blocked_websites():
    hosts_path = "/etc/hosts"  
    redirect = "127.0.0.1" 
    try:
        with open(hosts_path, 'r') as file:
            content = file.readlines()  
            # Extract the blocked websites (lines that start with '127.0.0.1')
            blocked_sites = [line.split()[1].replace('www.', '') for line in content if line.startswith(redirect)]
            blocked_sites = list(set(blocked_sites)) 

            if blocked_sites:
                print("Blocked websites:")
                for site in blocked_sites:
                    print(site)  
            else:
                print("No websites are currently blocked.")
    except Exception as error:
        print(f"Error: {error}")  

# Unblock a specific website by removing its entry from the hosts file.
def unblock_website(site):
    site = normalize_website(site) 
    hosts_path = "/etc/hosts" 
    redirect = "127.0.0.1"  

    # Entries for the website without 'www.' and with 'www.'
    entry = f"{redirect} {site}\n"
    entry_www = f"{redirect} www.{site}\n"

    try:
        # Open the hosts file in read-write mode
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()  
            file.seek(0)  
            file.truncate()

            # Write back all lines except the ones that block the site
            for line in lines:
                if line.strip() != entry.strip() and line.strip() != entry_www.strip():
                    file.write(line) 
        print(f"{site} has been unblocked.")
    except Exception as error:
        print(f"Error: {error}") 

#  For clearing the terminal screen 
def clear_screen():
    os.system('clear') 

HEADER = """
========================================
      WEBSITE BLOCKER - MAIN MENU
========================================
"""

def main():
    while True:
        clear_screen()  
        print(HEADER) 
        print("Select an option:")
        print("  1. Block a website")
        print("  2. Bulk Block websites with a TXT file")
        print("  3. Print blocked websites")
        print("  4. Unblock a website")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ").strip()  

        if choice == "1":
            site_to_block = input("Enter the website to block (e.g., www.example.com): ").strip()
            block_website(site_to_block)  
            time.sleep(5)  
        elif choice == "2":
            file_path = input("Enter the path to the TXT file: ").strip()
            block_sites_from_file(file_path) 
            time.sleep(5)
        elif choice == "3":
            print_blocked_websites()  
            input("Press Enter to continue...") 
        elif choice == "4":
            site_to_unblock = input("Enter the website to unblock (e.g., www.example.com): ").strip()
            unblock_website(site_to_unblock)  
            time.sleep(5)
        elif choice == "5":
            print("Exiting the program.") 
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")  
            time.sleep(5)

if __name__ == "__main__":
    main()
