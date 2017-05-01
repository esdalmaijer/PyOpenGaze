from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.eyetracker import EyeTracker
import pygaze.libtime as timer

disp = Display()
scr = Screen()

scr.draw_text("Preparing experiment...", fontsize=20)
disp.fill(scr)
disp.show()

tracker = EyeTracker(disp)
tracker.calibrate()

tracker.start_recording()
t0 = timer.get_time()
while timer.get_time() - t0 < 5000:
	gazepos = tracker.sample()
	scr.clear()
	scr.draw_fixation(fixtype='dot', pos=gazepos)
	disp.fill(scr)
	disp.show()

tracker.stop_recording()
tracker.close()

disp.close()
