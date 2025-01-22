# Clipboard Manager

## About

The **Clipboard Manager** is a Python-based tool designed to simplify clipboard operations. With this tool, you can:

- View the current clipboard value.
- Browse through a history of previously copied items.
- Clear the clipboard easily.

I created this project to have an easy way to go back and recopy saved items without manually searching through multiple sources. This utility helps save time and keep your clipboard organized.

## Features

- **Get Current Clipboard**: Fetches and displays the current clipboard value.
- **Show Clipboard History**: Displays a list of previously copied items.
- **Clear Clipboard**: Clears the current clipboard contents.

## Requirements

To run the Clipboard Manager, you need the following:

- Python 3.x
- `pyperclip` library (used for clipboard operations)

You can install the required dependency by running:

```bash
pip install pyperclip
```
## How to Run
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/clipboard-manager.git
```
Navigate to the project directory:

```bash
cd clipboard-manager
```
Run the script:


```bash
python clipboard_manager.py
```
The script will display a menu, and you can interact with the clipboard manager by entering your desired choice (1-4).

## Menu Options
The script will present the following menu:

1. Get Current Clipboard Value: Displays the value currently stored in the clipboard.
2. Show Clipboard History: Shows a history of all copied clipboard values since the program started.
3. Clear Clipboard: Clears the current clipboard value.
4. Exit: Exits the program.
Once you select an option, the corresponding action will be performed. You can repeat the process as needed.

## Areas for Improvement
Here are some potential areas for future improvement and development:

- Persistent History: Currently, clipboard history is stored in memory and will be lost when the program is closed. Implementing functionality to save the history to a file (e.g., JSON or text) would be beneficial.
- Search Functionality: Adding the ability to search through clipboard history for specific items could be helpful, especially when dealing with large amounts of data.
- Cross-platform Support: While the script is generally compatible, ensuring it works seamlessly across all operating systems (Windows, macOS, Linux) would improve its usability.
- Graphical User Interface (GUI): Creating a user-friendly GUI for easier interaction with the clipboard manager would be a nice enhancement over the current command-line interface.
- Clipboard Monitoring: Implementing automatic tracking of clipboard changes could remove the need for the user to manually check for updates.

## License
This project is licensed under the MIT License - see the LICENSE file for details.







