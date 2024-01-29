# Alarm Clock

This Python program allows users to set alarms with custom messages and choose from a selection of ringtones. The alarms can be set in either 12-hour or 24-hour format.

## Overview

The program utilizes the `datetime`, `time`, `winsound`, and `pyttsx3` libraries to create an alarm clock with the following features:

- Set alarms in either 12-hour or 24-hour format.
- Customizable alarm messages.
- Choose from available ringtones for the alarm.
- Dismiss or snooze options when the alarm goes off.

## Usage

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/shrutiwd/Alarm-Clock.git
    cd Alarm-Clock
    ```

2. Ensure you have Python installed on your system.

3. Run the program:

    ```bash
    python alarm_clock.py
    ```

4. Select the format (12-hour or 24-hour) for entering the alarm time.

5. Enter the alarm time, AM/PM (for 12-hour format), alarm message, and choose a ringtone.

6. The program will display the set alarm time, and the alarm will go off at the specified time.

7. When the alarm goes off, you can choose to dismiss it or snooze for 10 seconds.

## File Structure

- `alarm_clock.py`: The main Python script for setting and triggering alarms.
- `History.txt`: File containing a log of alarm settings and trigger times.
- `ringtones/`: Directory containing available alarm ringtones.
    - `classic.wav`
    - `fast.wav`
    - `heavy.wav`
    - `waves.wav`

## Note

- Make sure the `pyttsx3` library is installed for text-to-speech functionality. Install it using:

    ```bash
    pip install pyttsx3
    ```

- Ensure the `winsound` library is compatible with your operating system.

- Choose a valid ringtone option when prompted.

Feel free to customize the program or add more features according to your preferences.

Happy waking up!
