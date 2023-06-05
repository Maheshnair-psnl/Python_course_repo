import threading
import time

class TextEditor:
    def __init__(self):
        self.text = ""
        self.lock = threading.Lock()
        self.timer_thread = threading.Thread(target=self.check_input_timeout, daemon=True)

    def start(self):
        self.timer_thread.start()
        self.listen_for_input()

    def listen_for_input(self):
        while True:
            user_input = input()
            with self.lock:
                self.text += user_input
                self.timer_thread = threading.Thread(target=self.check_input_timeout, daemon=True)
                self.timer_thread.start()

    def check_input_timeout(self):
        time.sleep(5)
        with self.lock:
            if not self.timer_thread.is_alive():
                # The user has already started typing again, so we don't need to delete the text
                return

            self.text = ""
            print("Input timeout. Text cleared.")

if __name__ == "__main__":
    editor = TextEditor()
    editor.start()
