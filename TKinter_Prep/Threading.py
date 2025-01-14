import threading

class MyClass:
    def __init__(self):
        self.condition = threading.Condition()
        self.data_from_script = None
        self.data_for_script = None

    def run_method(self):
        for i in range(3):
            with self.condition:
                print("Method: Waiting for input from script...")
                self.condition.wait()  # Wait for the script to provide data
                print(f"Method: Received input - {self.data_from_script}")

                # Process and provide data back to the script
                self.data_for_script = f"Processed {self.data_from_script}"
                print(f"Method: Sending output - {self.data_for_script}")
                self.condition.notify()  # Notify the script to continue

def script_function(obj):
    for i in range(3):
        with obj.condition:
            print(f"Script: Sending input - Input {i}")
            obj.data_from_script = f"Input {i}"
            obj.condition.notify()  # Notify the method to proceed
            obj.condition.wait()  # Wait for the method to send data back
            print(f"Script: Received output - {obj.data_for_script}")

# Create an instance of MyClass
obj = MyClass()

# Create threads for the method and the script
method_thread = threading.Thread(target=obj.run_method)
script_thread = threading.Thread(target=script_function, args=(obj,))

# Start the threads
method_thread.start()
script_thread.start()

# Wait for both threads to finish
method_thread.join()
script_thread.join()