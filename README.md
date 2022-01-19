# PremioDoro

- [PremioDoro](#premiodoro)
  - [What is](#what-is)
  - [How to Use](#how-to-use)
  - [Configuration](#configuration)
  - [Credits](#credits)

## What is

Premiodoro is a kind of Pomodoro, made with Python that runs in the background, the reminders are customizable using a JSON file.

## How to Use

1. Install the requirements

```bash
$ pip3 install -r requirements.txt
```

2. Configure your reminders in `reminders.json`

```json
[
    {
        "message": "Go take a walk",
        "period": 3600
    },
    {
        "message": "Look something else for 20 seconds",
        "period": 1200
    }
]
```
* Period in seconds
* The message will display in the notification

3. Run the script

```bash
$ python3 .
```

4. Minimize the terminal and go to work!

The script will send you a notification and play a sound when a reminder is triggered.

## Configuration 

Change the variables in `config.py` to change the Premiodoro configuration.

| variable       | what does                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| PREMIODORO_OUT | The output file, currently only output the remaining time to the next reminder in a json format.            |
| IDLE_USE       | If enabled, will use the IdleManager which checks if your mouse is idle, if so will not tick the reminders. |
| IDLE_MAXCOUNT  | The minimum time (in seconds) for your state be counted as idle                                             |

## Credits

| what               | who                                                         |
| ------------------ | ----------------------------------------------------------- |
| Notification sound | [IENBA](https://freesound.org/people/IENBA/sounds/545495/)  |
| Programming        | [Peterson Adami Candido](https://github.com/wetrustinprize) |