from package.cli import main_cli
import threading
import time as Time
import typer

def testRun():
  while True:
    Time.sleep(1)
    print("testRun")


if __name__ == "__main__":
  # typer.run(main_cli)
  thread = threading.Thread(target=testRun, args=())
  thread.start()

