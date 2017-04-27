import os
import time

from opengaze import OpenGazeTracker

# Construct the path to the log file.
dirname = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(dirname, '%s.tsv' % (time.strftime("%Y-%m-%d_%H-%M-%S")))

# Open the connection to the tracker.
tracker = OpenGazeTracker(logfile=fname, debug=False)

# Calibrate the tracker.
tracker.calibrate()

# Start recording data.
tracker.start_recording()
tracker.log("START=%d" % (round(time.time()*1000)))

# Collect data for a bit.
for i in range(5):
	tracker.log("STEP %d: %d" % (i+1, round(time.time()*1000)))
	time.sleep(1.0)

# Stop recording.
tracker.log("STOP=%d" % (round(time.time()*1000)))
tracker.stop_recording()

# Close the connection.
tracker.close()
