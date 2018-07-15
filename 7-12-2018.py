! /usr/bin/env python3
print('Content-type: text/html\n')
import cgi

html = """
<!doctype html>
<html>
<head><meta charset ="utf-8"><title>MADLIBS</title></head>
<body>
<h1> I211 Madlibs!</h1>
<form action=madlibs.cgi  method="post">
	Enter the requested piece of informaton: 
	<p><input type="text" name="drink" placeholder="drink">
	<p><input type="text" name="facial expression" placeholder="facial expression">
	<p><input type="text" name="adj1" placeholder="adjective">
	<p><input type="text" name="thing" placeholder="thing">
	<p><input type="text" name="body part" placeholder="body part">
	<p><input type="text" name="piece of furniture" placeholder="piece of furniture">
	<p><input type="text" name="objects" placeholder="objects">
	<p><input type="text" name="rank" placeholder="rank">
	<p><input type="text" name="verb" placeholder="verb">
	<p><input type="text" name="nickname" placeholder="nickname">
	<p><input type="text" name="place" placeholder="place">
	<p><input type="text" name="adj2" placeholder="adjective">
	<p><input type="text" name="exclamation" placeholder="exclamation" >
	<p><input type="radio" name="Jordan" value="Jordan" checked> Jordan
	<input type="radio" name="Yuning" value="Yuning" checked > Yuning
	<input type="radio" name="Khayla" value="Khayla" checked > Khayla
	<p><button type="submit">Submit</button>
	<button type="reset">Reset</button>
</form> 
</body>
</html>"""

print(form.getfirst()
