#!/usr/bin/python
from datetime import datetime
# Print current time once
now = datetime.now()
current = now.strftime("%H:%M:%S")
print("This message was sent:", current)
