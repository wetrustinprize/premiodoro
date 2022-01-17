# Reminders
# Each reminder has the following keys:
#   reminder: The message displayed in the notification
#   period: The period on seconds to display the reminder
REMINDERS = [
    {
        "message": "Hello world!",
        "period": 3
    },
    {
        "message": "Go take a walk",
        "period": 3600
    },
    {
        "message": "Look something else for 20 seconds",
        "period": 1200
    }
]

# Output file dir
# The file where Premiodoro will output information
# This file can be used in other scripts
# If set to None, there will be no output written
PREMIODORO_OUT = './premiodoro'
