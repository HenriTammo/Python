f = open("näidis.html", "w")
code = """<html>
<head></head>
<body><p>"""
sisestus = "tegemist on muutuva stringiga"
code2 = """</p></body>
</html>"""

f.write(code)
f.write(str(sisestus))
f.write(code2)
f.close