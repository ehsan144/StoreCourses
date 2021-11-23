from os import system, listdir
from pickle import load, dump
from colored import fg, attr

system("cls")


class StoreCoursesVideo:
    file = "IlIlIlIllIIllIIl"
    data = dict()

    def __init__(self):
        if self.file in listdir():
            with open(self.file, "rb") as f:
                self.data = load(f)

    def get_data(self):
        system("cls")
        print("%s All Courses:\n\n %s" % (fg(1), attr(0)))
        for name in self.data:
            vn, per = self.data.get(name)
            print(f"\t %s{name.upper()}%s => %s{vn}%s : %s{per} %s \n" %
                  (fg(127), attr(0), fg(32), attr(0), fg(178), attr(0)))

    def delete_data(self, name):
        if name != "":
            if name in self.data:
                self.data.pop(name)
                print(f"%s{name}%s Success Deleted!" % (fg(1), attr(0)))
                with open(self.file, "wb") as f:
                    dump(self.data, f)
        self.get_data()

    def insert_data(self, name: str, video_num: int = 0, per: float = 0):
        if name != "":
            self.data.update({name: [video_num, float(per)]})
            with open(self.file, "wb") as f:
                dump(self.data, f)
        self.get_data()


if __name__ == '__main__':
    a = StoreCoursesVideo()
    a.get_data()
    while True:
        select = input("Please Enter your data for %sInsert%s or %sUpdate%s (%s'D'%s => Delete | %s'E'%s => Exit):" %
                       (fg(6), attr(0), fg(1), attr(0), fg(1), attr(0), fg(3), attr(0)))
        if select == "":
            print("%sError%s : data can not be %sNull%s" % (fg(1), attr(0), fg(2), attr(0)))
        elif select.upper() == "E" or select.upper() == "N":
            break
        elif select.upper() == "D":
            key = input("Enter a Course's Name for Delete:")
            a.delete_data(key)
        else:
            data = tuple(select.split(" "))
            if "" not in data and len(data) == 3:
                n, v, s, *other = data
                a.insert_data(n, int(v), float(s))
            else:
                print("%sError%s : Data can not be %sNull%s and Data must have %s 3 arguments %s" %
                      (fg(1), attr(0), fg(3), attr(0), fg(4), attr(0)))
    a.get_data()
