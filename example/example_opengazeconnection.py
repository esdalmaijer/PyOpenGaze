import os
import time

from opengaze import OpenGazeConnection

# # # # #
# INITIALISE

# Construct the path to the log file.
dirname = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(dirname, '%s.tsv' % (time.strftime("%Y-%m-%d_%H-%M-%S")))

# Open the connection to the tracker.
tracker = OpenGazeConnection(logfile=fname, debug=False)
time.sleep(1.0)

# Enable the tracker to send ALL the things.
tracker.enable_send_counter(True)
tracker.enable_send_cursor(True)
tracker.enable_send_eye_left(True)
tracker.enable_send_eye_right(True)
tracker.enable_send_pog_best(True)
tracker.enable_send_pog_fix(True)
tracker.enable_send_pog_left(True)
tracker.enable_send_pog_right(True)
tracker.enable_send_pupil_left(True)
tracker.enable_send_pupil_right(True)
tracker.enable_send_time(True)
tracker.enable_send_time_tick(True)
tracker.enable_send_user_data(True)


# # # # #
# CALIBRATION

# Reset the calibration to its default points.
tracker.calibrate_reset()

# Show the calibration screen.
tracker.calibrate_show(True)

# Start the calibration.
tracker.calibrate_start(True)

# Wait for the calibration result.
result = None
while result == None:
	result = tracker.get_calibration_result()
	time.sleep(0.1)

# Hide the calibration window.
tracker.calibrate_show(False)


# # # # #
# DATA COLLECTION

# Start the streaming of data.
tracker.enable_send_data(True)

# Log the start.
tracker.user_data("START=%d" % (round(time.time()*1000)))

# Wait for 1 sample's duration, then reset the user-defined variable.
time.sleep(0.017)
tracker.user_data("0")

# Collect data for five seconds.
time.sleep(5.0)

# Log the end of data collection.
tracker.user_data("STOP=%d" % (round(time.time()*1000)))

# Stop the streaming of data.
tracker.enable_send_data(False)


# # # # #
# CLOSE

# Close the connection.
tracker.close()
