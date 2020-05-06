f = open("muud failid/7tund/näidis.html", "w")
code = """<html>
<head></head>
<body><p>"""
sisestus =["1, 2, 3, 4, 5"]
code2 = """</p></body>
</html>"""

f.write(code)
f.write(str(sisestus))
f.write(code2)
f.close