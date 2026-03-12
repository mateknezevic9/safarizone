import re
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
orig = len(html)
html = re.sub(r'src="data:image/[^;]+;base64,[^"]{20,}"', 'src=""', html)
html = re.sub(r'<div[^>]*class="[^"]*card[^"]*"[^>]*>(?:(?!<\/div>)[\s\S])*?[Cc]harizard(?:(?!<\/div>)[\s\S])*?<\/div>', '', html)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Done: {orig} -> {len(html)}")