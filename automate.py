from pathlib import Path

class_list = []

def class_names():
    print("Enter *2 to finish")
    while True:
        c = input("Class: ")
        if c == "": break
        class_list.append(c)


def class_folders(r_dir):
    for i in range(len(class_list) - 1, -1, -1):
        class_list[i] = r_dir + "/" + class_list[i]
        cf = Path(class_list[i])
        cf.mkdir()


def week_folders():
    weeks = int(input("How many weeks? "))
    for c in class_list:
        for i in range(weeks - 1, -1, -1):
            wf = Path(c + "/Week " + str(i + 1))
            wf.mkdir()


if __name__ == "__main__":
    root_dir = input("\nRoot Directory: ")
    root_dir = str(Path.home()) + "/" + root_dir
    Path(root_dir).mkdir()
    class_names()
    class_folders(root_dir)
    week_folders()
    print("File system updated...good luck this semester!\n")