""" ex_4_0.py """
from typing import List

def get_data_file_path(filename: str) -> str:
  """Stub to mimic src module function"""
  return filename

FILENAME = get_data_file_path('messages.log')  

def get_shutdown_events(logfile: str) -> List[str]:
  """Return list of shutdown event log lines from file"""
  shutdown_events = []
  
  with open(logfile) as f:
    for line in f:
      words = line.split()  
      if words[4] == "initiated.":
        shutdown_events.append(line[:-2])

  return shutdown_events

if __name__ == "__main__":
  
  events = get_shutdown_events(FILENAME)
  
  print(f"{get_shutdown_events(FILENAME)=}")
  
  for event in events:
    print(event)
