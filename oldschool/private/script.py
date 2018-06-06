data = open("orig.txt", "r").read()
fout = open("../public/task.txt", "w")

print(data.replace("o", "olo").replace("a", "alo").replace("e", "elo").replace("i", "ilo").replace("u", "ulo").replace("y", "ylo"), file=fout)