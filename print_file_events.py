# https://developerweb.net/viewtopic.php?id=6228
# https://pypi.org/project/inotify/
import inotify.adapters
i = inotify.adapters.Inotify()
i.add_watch("/home/du_ds/tmp")
for event in i.event_gen(yield_nones=False):
	(_, type_names, path, filename) = event
	print(event)
