import importlib
import os

def run_tests():

    test_dir = "tests"

    for file in os.listdir(test_dir):

        if file.startswith("test_") and file.endswith(".py"):

            module_name = file[:-3]
            module = importlib.import_module(f"tests.{module_name}")

            if hasattr(module, "run"):
                print(f"Running {module_name}")
                module.run()

if __name__ == "__main__":
    run_tests()
