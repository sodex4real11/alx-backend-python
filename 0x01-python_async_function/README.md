Python - Async; The ALX Project
In this project, asynchronous programming in Python, including asynchronous I/O, tasks, and coroutines were explored. Various asynchronous techniques to handle concurrent tasks and improve the performance of Python applications were implemented.

Project description

0-basic_async_syntax.py

This script demonstrates the basic syntax of asynchronous programming in Python. It defines a function wait_random(max_delay: int = 10) that asynchronously waits for a random delay between 0 and max_delay seconds before returning the delayed result.

1-basic_asyncio.py

This script showcases how to use the asyncio module to run asynchronous functions concurrently. It defines a function wait_n(n: int, max_delay: int = 10) that takes an integer n and an optional maximum delay. It uses the asyncio.gather function to run multiple instances of wait_random() concurrently and returns a list of delayed results.

2-measure_runtime.py

This script measures the execution time of concurrent asynchronous functions. It defines a function measure_time() that calculates the total execution time for running wait_n() with a specified n value.

3-tasks.py

This script demonstrates the use of asyncio Tasks to perform asynchronous operations concurrently. It defines a function task_wait_n(n: int, max_delay: int = 10) that uses asyncio Tasks to run multiple instances of wait_random() concurrently and returns a list of delayed results.

4-tasks.py

This script shows how to handle asynchronous functions using asyncio.as_completed. It defines a function task_wait_n(n: int, max_delay: int = 10) that uses asyncio.as_completed to iterate through completed tasks and return a list of delayed results.

Usage

To run any of the scripts, make sure you have Python 3.7 or higher installed on your system. You can execute the scripts using the following command:

python script_name.py

Replace script_name.py with the name of the script you want to run.
