tag_start = "<start>"
tag_end = "<end>"
text = "Это тестовая <start>строка для изучения<end> строковых операций"
pos_start = text.find(tag_start)
pos_end = text.find(tag_end)
if (-1 == pos_start) or (-1 == pos_end) or (pos_start > pos_end):
  print("???")
else:
  print(text[pos_start + len(tag_start):pos_end])

