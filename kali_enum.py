
# A program in python that can: 
#     Enumerate all the running processes.
#     List all the running threads within process boundary.
#     Enumerate all the loaded modules within the processes.
#     Is able to show all the executable pages within the processes.
#     Gives us a capability to read the memory.

# Research from:
# https://stackoverflow.com/questions/2703640/process-list-on-linux-via-python
# https://psutil.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/5553917/how-to-list-all-dlls-loaded-by-a-process-with-python
# https://stackoverflow.com/questions/52521963/reading-data-from-process-memory-with-python
# https://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

import psutil
import re


def display_processes():
    '''Enumerates over all running processes and prints them'''
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print("Process info:", process.info)


def display_process_threads(pid):
    '''Lists the running threads within process pid'''
    process = psutil.Process(pid)
    print("Process thread:", process.threads())


def display_modules(pid):
    '''Enumerates over all loaded modules for pid and prints them'''
    process = psutil.Process(pid)
    for dll in process.memory_maps():
        print("Process module:", dll.path)


def display_executable_pages(pid):
    '''Shows all the executable pages within process pid'''
    process = psutil.Process(pid)
    dll = process.memory_maps(grouped=False)
    for index in range(len(dll)):
        if 'x' in dll[index][1]:  # check for executable rights
            print("Process executable:", dll[index])


def display_memory_addresses(pid):
    '''Dumps the memory data from pid into the .dump file'''
    pid = str(pid)

    # open our files by pocess id
    maps_file = open("/proc/" + str(pid) + "/maps", 'r')
    mem_file = open("/proc/" + str(pid) + "/mem", 'rb', 0)

    for line in maps_file.readlines():  # for each mapped region
        # this regex validates hex
        m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
        if m.group(3) == 'r':  # if this is a readable region
            try:
                start = int(m.group(1), 16)
                end = int(m.group(2), 16)
                mem_file.seek(start)  # seek to region start
                chunk = mem_file.read(end - start)  # read region contents
                print(chunk)
            except OSError:
                pass
    maps_file.close()
    mem_file.close()


if __name__ == '__main__':
    while True:
        print("Enter 1 to see processes")
        print("Enter 2 to see process threads")
        print("Enter 3 to see process modules")
        print("Enter 4 to see process executables")
        print("Enter 5 to see process memory (requires hightened privileges")
        user_choice = input("Enter a number: ")
        if user_choice == '1':
            display_processes()
        elif user_choice == '2':
            pid = int(input("Enter a pid:"))
            display_process_threads(pid)
        elif user_choice == '3':
            pid = int(input("Enter a pid:"))
            display_modules(pid)
        elif user_choice == '4':
            pid = int(input("Enter a pid:"))
            display_executable_pages(pid)
        elif user_choice == '5':
            pid = int(input("Enter a pid:"))
            display_memory_addresses(pid)
        else:
            print("Not a valid option, exiting")
            break

