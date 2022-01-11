from os import pipe, system, listdir
from pickle import NONE, load, dump
from colored import fg, attr

system("cls")


class StoreCoursesVideo:
    file = ""
    data = dict()
    def __init__(self,dFileName : str = "IlIlIlIllIIllIIl"):
        if dFileName != "":
            self.file = dFileName
        if self.file in listdir():
            with open(self.file, "rb") as f:
                self.data = load(f)

    def get_data(self):
        system("cls")
        print("%s All Courses:\n\n %s" % (fg(1), attr(0)))
        for index,name in enumerate(self.data):
            vn, per = self.data.get(name)
            print(f"\t %s[{index}]%s %s{name}%s => %s{vn}%s : %s{per} %s \n" %
                  (fg(14), attr(0),fg(127), attr(0), fg(32), attr(0), fg(178), attr(0)))

    def delete_data(self, name):
        if name != "":
            if(name.isnumeric()):
                kname = NONE
                for i,n in enumerate(self.data):
                    if i == int(name):
                        kname = n
                        break
                if kname != NONE and kname in self.data:
                    self.data.pop(kname)
            else:
                if name in self.data:
                    self.data.pop(name)
                    print(f"%s{name}%s Success Deleted!" % (fg(1), attr(0)))
            with open(self.file, "wb") as f:
                dump(self.data, f)
        self.get_data()

    def insert_data(self, name: str, video_num: int = 0, per: float = 0):
        if name != "":
            if(name.isnumeric()):
                print(name)
                kname = NONE
                for i,n in enumerate(self.data):
                    if i == int(name):
                        kname = n
                        break
                if kname != NONE:
                    self.data.update({kname: [video_num, float(per)]})
            else:
                self.data.update({name: [video_num, float(per)]})
            with open(self.file, "wb") as f:
                dump(self.data, f)
        self.get_data()


if __name__ == '__main__':
    store = StoreCoursesVideo()
    store.get_data()
    while True:
        select = input("Please Enter your data for %sInsert%s or %sUpdate%s (%s'D'%s => Delete | %s'E'%s => Exit):" %
                       (fg(6), attr(0), fg(1), attr(0), fg(1), attr(0), fg(3), attr(0)))
        if select == "":
            print("%sError%s : data can not be %sNull%s" % (fg(1), attr(0), fg(2), attr(0)))
        elif select.upper() == "E" or select.upper() == "N":
            break
        elif select.upper() == "D":
            key = input("\nEnter a Course's Name Or [Index] for Delete:")
            store.delete_data(key)
        else:
            data = tuple(select.split(" "))
            print(len(data))
            if ""  in data and len(data) > 3:
                print("%sError%s : Data can not be %sNull%s and Data must have %s Name & VideoNumber & CurentPersent %s" %
                      (fg(1), attr(0), fg(3), attr(0), fg(4), attr(0)))
            else:
                
                if len(data) == 2:
                    n, v = data
                    
                    store.insert_data(n, int(v))
                elif len(data) >= 3:
                    n,v,s,*other = data
                    store.insert_data(n, int(v), float(s)) 
                
    store.get_data()
