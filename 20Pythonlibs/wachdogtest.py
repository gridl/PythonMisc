from watchdog.observers import Observer
from watchdog.events import (PatternMatchingEventHandler, FileModifiedEvent, FileCreatedEvent)

observer = Observer() # create an observer instance

class Handler(PatternMatchingEventHandler):
    def on_created(self, event: FileCreatedEvent): #subclass one of the handler classes and override the mthods for events you want to process
        print('FIle created: ', event.src_path)

    def on_modified(self, event: FileModifiedEvent):
        print('File modified: %s [%s]' % (event.src_path,event.event_type))

observer.schedule(event_handler=Handler('*'), path='.') #schedule the event handler and tell watchdog what it should be watching. (*) = ALl files, (.) current directory
observer.daemon = False
observer.start()

try:
    observer.join() # watchdog runs in a separate thread
except KeyboardInterrupt:
    print('Stopped')
    observer.stop()
    observer.join()

