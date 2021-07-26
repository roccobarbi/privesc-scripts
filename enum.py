import subprocess

executable_dirs = ["/bin", "/usr/bin", "usr/sbin"]


def get_executable_file_list():
    output = []
    for dir in executable_dirs:
        command = ["ls", "-l", dir]
        out = subprocess.Popen(command, stdout=subprocess.PIPE)
        stdout = out.communicate()
        for line in stdout:
            print(str(line))
        output.extend(stdout)
    return output


def get_suid_and_sgid_from_list(list):
    output = []
    for line in list:
        if line[3] == 's' or line[6] == 's':
            output.append(line)
    return output


def print_by_line(list):
    for line in list:
        print(str(line))


def print_divisor_20_double():
    print("====================")


def print_title(title):
    print_divisor_20_double()
    print(str(title))
    print_divisor_20_double()


def main():
    executable_files = get_executable_file_list()
    suid_sgid_executable_files = get_suid_and_sgid_from_list(executable_files)
    print_title("Executable files with suid and guid")
    print_by_line(suid_sgid_executable_files)


if __name__ == "__main__":
    main()