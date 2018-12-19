import re

regex = re.compile("d/(.+)/")
print(regex.findall("https://drive.google.com/file/d/14WlWEWAI-wyEQ3TEBqw13H-GJaPKlOTx/view"))