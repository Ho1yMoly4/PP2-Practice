import os
os.mkdir("test")


import os
os.makedirs("a/b/c")
#or
os.makedirs("a/b/c", exist_ok=True)


from pathlib import Path
Path("test").mkdir()


import os
print(os.listdir("Folder"))


