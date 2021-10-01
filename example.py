import os

model_ext = ('.stl', '.slc', '.png')
files = []
usb_mount = os.listdir("img")
for x in range(len(usb_mount)):
    usb_root = os.path.join("img", usb_mount[x])
    files += [os.path.join(usb_root, file) for file in os.listdir(usb_root) if file.lower().endswith(model_ext)]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

print("Files:", files)
