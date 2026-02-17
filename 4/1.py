# import re

sentence = input("type sentence:")
symbols = sentence.count("")
words = sentence.split()
wordscount = len(words)
print(f"result: symbols - {symbols}, wordscount = {wordscount}, vowels count {len(re.findall("[eyuioa]", sentence.lower()))}")

