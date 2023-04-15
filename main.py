import pandas as pd
import datetime
from notifications import send_push_notification

# Get the current date
today = datetime.datetime.now().date()

# Load the Excel file using pandas
df = pd.read_excel('workouts.xlsx')

# Convert the date column to datetime format with dayfirst=True
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Filter the dataframe to get the row with the current date
current_workout = df[df['Date'].dt.date == today]['Workout'].values

# Check if a workout exists for the current date
if len(current_workout) > 0:
    message = f"Good morning Caroline. Today is {today.strftime('%-d %B')}, and your workout is: {current_workout[0]}."
    title = f"Your workout for {today.strftime('%-d %B')}"

    send_push_notification(message, title)

else:
    quit()
