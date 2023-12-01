import random
import time

def create_data_file(file_name):
    with open(file_name, 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

def convert_line_to_int_array(line):
    return list(map(int, line.split()))

def filter_numbers_above_threshold(arr, threshold=40):
    return list(filter(lambda x: x > threshold, arr))

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for line in data:
            line_str = ' '.join(map(str, line))
            file.write(line_str + '\n')

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield convert_line_to_int_array(line)

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@measure_execution_time
def main():
    create_data_file('data.txt')
    with open('data.txt', 'r') as file:
        lines = [convert_line_to_int_array(line) for line in file]
        print("BEFORE")
        for line in lines:
            print(line)
    
    filtered_data = [filter_numbers_above_threshold(line) for line in lines]
    write_to_file('filtered_data.txt', filtered_data)
    
    generator = read_file('filtered_data.txt')
    print("--------------------------------------------------------")
    print("AFTER")
    for line in generator:
        print(line)

main()