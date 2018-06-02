smiles = open("../public/task.txt").read()

out = open("tmp.html", "w")

print('''<meta charset="utf-8" /><style>
body {
    font-size: 8px;
}
</style>
<pre>''', file=out)
print(smiles, file=out)
print("</pre>", file=out)

out.close()
