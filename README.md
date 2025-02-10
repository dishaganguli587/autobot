# AutoBot

AutoBot is a Python program designed to enhance productivity on Windows systems by providing a quick switch mechanism for background and foreground tasks. It allows users to automate the switching of tasks to maintain focus on the most important applications while keeping other tasks running in the background.

## Features

- Automatically switch between specified foreground and background tasks.
- Boost productivity by ensuring the right application is always in focus.
- Customizable list of foreground and background tasks.
  
## Requirements

- Python 3.x
- `psutil` library

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/autobot.git
cd autobot
```

Install the required Python package:

```bash
pip install psutil
```

## Usage

Edit the `autobot.py` file to specify your preferred foreground and background tasks. Modify the `FOREGROUND_TASKS` and `BACKGROUND_TASKS` lists with the names of the applications you want to manage.

Run the program:

```bash
python autobot.py
```

The program will start managing the specified tasks, bringing them to the foreground or sending them to the background as defined.

## Note

Ensure that the application names in `FOREGROUND_TASKS` and `BACKGROUND_TASKS` match the process names as they appear in the Windows Task Manager.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.