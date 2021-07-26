import os

executable_dirs = ["/bin", "/usr/bin", "/usr/sbin"]


def get_executable_file_list():
    output = []
    for dir_name in executable_dirs:
        file_list = os.listdir(dir_name)
        for file_name in file_list:
            file_path = os.path.join(dir_name, file_name)
            output.append(file_path)
    return output


def get_suid_from_list(file_list):
    output = []
    for file_path in file_list:
        if os.stat(file_path).st_mode & 0o4000:
            output.append(file_path)
    return output


def get_sgid_from_list(file_list):
    output = []
    for file_path in file_list:
        if os.stat(file_path).st_mode & 0o2000:
            output.append(file_path)
    return output


def print_by_line(output):
    for line in output:
        print(str(line))


def print_divisor_20_double():
    print("====================")


def print_title(title):
    print_divisor_20_double()
    print(str(title))
    print_divisor_20_double()


def main():
    executable_files = get_executable_file_list()
    suid_executable_files = get_suid_from_list(executable_files)
    print_title("Executable files with suid")
    print_by_line(suid_executable_files)


if __name__ == "__main__":
    main()