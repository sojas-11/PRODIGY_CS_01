import string
import os
from collections import Counter
def caesar_encrypt(text, shift):
    result = ""
    shift = shift % 26  
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_pos = (ord(ch) - base + shift) % 26
            result += chr(base + new_pos)
        else:
            result += ch
    
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_crack(ciphertext):
    print("\n" + "="*60)
    print("BRUTE FORCE ATTACK - All 26 Possibilities:")
    print("="*60)
    
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
        print(f"Shift {shift:2d}: {decrypted}")
    
    return results
def frequency_analysis(text):
    clean_text = ''.join(ch.upper() for ch in text if ch.isalpha())   
    if not clean_text:
        print("No alphabetic characters found!")
        return    
    freq = Counter(clean_text)
    total = len(clean_text)
    print("\n" + "="*60)
    print("FREQUENCY ANALYSIS:")
    print("="*60)
    print(f"Total letters: {total}\n")
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_freq:
        percentage = (count / total) * 100
        bar = "█" * int(percentage / 2)
        print(f"{letter}: {count:3d} ({percentage:5.1f}%) {bar}")
    print("\nEnglish letter frequency (E is most common at ~12.7%)")

def save_to_file(filename, text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print(f"✓ Saved to {filename}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")

def load_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found!")
        return None
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return None


def advanced_statistics(text):
    print("\n" + "="*60)
    print("TEXT STATISTICS:")
    print("="*60)
    
    total_chars = len(text)
    alphabetic = sum(1 for ch in text if ch.isalpha())
    numeric = sum(1 for ch in text if ch.isdigit())
    spaces = text.count(' ')
    special = total_chars - alphabetic - numeric - spaces
    
    print(f"Total characters: {total_chars}")
    print(f"Alphabetic: {alphabetic}")
    print(f"Numeric: {numeric}")
    print(f"Spaces: {spaces}")
    print(f"Special characters: {special}")


def main_menu():
    """Main menu system"""
    print("\n" + "="*60)
    print("ADVANCED CAESAR CIPHER TOOL")
    print("="*60)
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("3. Brute force attack (try all shifts)")
    print("4. Frequency analysis")
    print("5. Load from file")
    print("6. Save to file")
    print("7. Text statistics")
    print("8. Exit")
    print("="*60)
    
    choice = input("Select option (1-8): ").strip()
    return choice


def main():
    message = ""
    shift = 0
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            message = input("\nEnter message to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if not (1 <= shift <= 25):
                    print("Shift must be between 1-25")
                    continue
                encrypted = caesar_encrypt(message, shift)
                print(f"\n✓ Encrypted: {encrypted}")
                message = encrypted
            except ValueError:
                print("Invalid shift value!")
        
        elif choice == "2":
            message = input("\nEnter message to decrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if not (1 <= shift <= 25):
                    print("Shift must be between 1-25")
                    continue
                decrypted = caesar_decrypt(message, shift)
                print(f"\n✓ Decrypted: {decrypted}")
                message = decrypted
            except ValueError:
                print("✗ Invalid shift value!")
        
        elif choice == "3":
            message = input("\nEnter encrypted message to crack: ")
            brute_force_crack(message)
            print("\nWhich shift looks correct? (Enter to continue)")
            input()
        
        elif choice == "4":
            text = input("\nEnter text for analysis: ")
            frequency_analysis(text)
        
        elif choice == "5":
            filename = input("\nEnter filename to load: ")
            loaded = load_from_file(filename)
            if loaded:
                message = loaded
                print(f"Loaded: {message[:50]}..." if len(message) > 50 else f"Loaded: {message}")
        
        elif choice == "6":
            if message:
                filename = input("\nEnter filename to save: ")
                save_to_file(filename, message)
            else:
                print("✗ No message to save!")
        
        elif choice == "7":
            text = input("\nEnter text for statistics: ")
            advanced_statistics(text)
        
        elif choice == "8":
            print("\n Goodbye!")
            break
        
        else:
            print("✗ Invalid option! Choose 1-8")

if __name__ == "__main__":
    main()






















