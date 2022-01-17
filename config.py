####
# REMINDERS
####
# Each reminder has the following keys:
#   reminder: The message displayed in the notification
#   period: The period on seconds to display the reminder
REMINDERS = [
    {
        "message": "Hello world!",
        "period": 5
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
PREMIODORO_OUT = './var/premiodoro'

####
# IDLE
####
# Should use Idle system?
IDLE_USE = True

# Idles count
# The total seconds your mouse must be in the same position to count your state as idle
IDLE_MAXCOUNT = 120
