import pyperclip

## Clipboard Manager Class (manages clipboard operations)

class ClipBoardManager:
    def __init__(self):
        self.history = []
        self.current_value = None 

    def get_clipboard(self):  ## fetches current clipboard 
        value = pyperclip.paste()
        if value != self.current_value:
            self.history.append(value)
            self.current_value = value 
        return value
    
    def clear_clipboard(self): ## clears current clearboard 
        pyperclip.copy('')
        self.current_value = ''
        print("Clipboard cleared.")

    def show_history(self):  ## displays history 
        if self.history:
            for idx, value in enumerate(self.history, start =1): ## index starts at one 
                print (f"{idx}: {value}")

        else:
            print("History N/A")

## main execution logic 

if __name__ == "__main__":
    manager = ClipBoardManager()

    while True:
        print("\nMenu:")
        print("1. Get current clipboard value")
        print("2. Show clipboard history")
        print("3. Clear clipboard")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            current_value = manager.get_clipboard()
            print(f"Current clipboard value: {current_value}")

        elif choice == '2':
            manager.show_history()

        elif choice == '3':
            manager.clear_clipboard()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")