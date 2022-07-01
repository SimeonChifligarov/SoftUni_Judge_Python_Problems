# You will receive 3 lines of input. On the first line you will receive a title of an article.
# On the next line you will receive the content of that article. On the next n lines until you receive
# "end of comments" you will get the comments about the article.

title = input()
content = input()
comments_as_list = []
comments = input()

while not comments == "end of comments":
    comments_as_list.append(comments)
    comments = input()

print("<h1>")
print(f"    {title}")
print("</h1>")
print("<article>")
print(f"    {content}")
print("</article>")
for comm in comments_as_list:
    print("<div>")
    print(f"    {comm}")
    print("</div>")
