import re

with open("./2022/filesystem.txt", 'r') as d:
    lines = d.readlines()

class FileSystem:
    CD_REGEX = re.compile(r"^\$ cd (.+)$")
    LS_REGEX = re.compile(r"^\$ ls$")
    DIR_REGEX = re.compile(r"^dir (.+)$")
    FILE_REGEX = re.compile(r"^(\d+) (.+)$")
    def __init__(self, lines):
        self.lines = lines
        self.directories = []
    
    def get_dir(self, name, parent):
        for d in self.directories:
            if d.name == name and d.parent == parent:
                return d
    
    def build_tree(self):
        current_dir = None
        ls_flag = False
        for l in self.lines:
            l = l.strip()
            # print(l, "->", current_dir)
            cd = re.match(self.CD_REGEX, l)
            ls = re.match(self.LS_REGEX, l)
            if cd:
                ls_flag = False
                if cd.groups()[0] == "..":
                    current_dir = current_dir.parent
                else:
                    # print(re.match(self.CD_REGEX, l).groups())
                    d = self.get_dir(cd.groups()[0], current_dir)
                    if not d:
                        d = Directory(cd.groups()[0], current_dir)
                        if current_dir:
                            current_dir.children.append(d)
                        self.directories.append(d)
                    current_dir = d
            elif ls:
                ls_flag = True
            elif ls_flag:
                dir_ = re.match(self.DIR_REGEX, l)
                file_ = re.match(self.FILE_REGEX, l)
                if dir_:
                    d = self.get_dir(dir_.groups()[0], current_dir)
                    if not d:
                        d = Directory(dir_.groups()[0], current_dir)
                        current_dir.children.append(d)
                        self.directories.append(d)
                elif file_:
                    current_dir.files.append(File(file_.groups()[1], file_.groups()[0], current_dir))
                else:
                    print("Unkonwn line", l, "in ls flag")
            else:
                print("Unkonwn line", l)

class File:
    def __init__(self, name, size, directory) -> None:
        self.name = name
        self.size = int(size)
        self.directory = directory

    def __repr__(self) -> str:
        return f"{self.name} ({self.size}) in {self.directory.name}"

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def __repr__(self) -> str:
        return f"{self.name}"

    def get_size(self) -> int:
        s = 0
        for f in self.files:
            s += f.size
        for c in self.children:
            s += c.get_size()

        return s

fs = FileSystem(lines)
fs.build_tree()
ans = []
for d in fs.directories:
    if d.get_size() <= 100000:
        print(d, d.get_size())
        ans.append(d)
    
print()
print(sum(a.get_size() for a in ans)) # 1453349

print()
# part 2
total = 70000000
required = 30000000
root = None
for i in fs.directories:
    if i.name == '/' and i.parent == None:
        root = i

# print(total - root.get_size())
to_be_deleted = required - (total - root.get_size())
print(to_be_deleted)

candidates = [a for a in fs.directories if a.get_size() >= to_be_deleted]
by_sizes = sorted(candidates, key=lambda x: x.get_size())
# print(sizes[-1].get_size())
print(by_sizes[0].get_size())