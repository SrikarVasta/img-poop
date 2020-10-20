import os
import tinify

tinify.key = ""
path = "./menu"

files = os.listdir(path)
all_files = []
done = []
for r, d, files in os.walk(path):
    for f in files:
        if f.endswith(".jpg"):
            all_files.append(1)
for r, d, files in os.walk(path):
    for f in files:
        if f.endswith(".jpg"):
            print("processing (", len(done)+1, "/", len(all_files), ")...")
            source = tinify.from_file(os.path.join(r, f))
            print(f)
            source.to_file(os.path.join(r, "optimalized-" + f))
            print("finished:", f)
            print("replacing:", os.path.join(r, f))
            if os.path.exists(os.path.join(r, "optimalized-" + f)):
                if os.path.exists(os.path.join(r,f)):
                    os.remove(os.path.join(r, f))
                    os.rename(os.path.join(r, "optimalized-" + f), os.path.join(r, f))
                    print("replaced:", os.path.join(r, f),
                        " with ",  os.path.join(r, "optimalized-" + f))
                    done.append(1)
