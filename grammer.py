import language_tool_python
from textblob import TextBlob as tr
#trans=language_tool_python.LanguageTool('en-US')
s=" i lve u"
text=   tr(s)#trans.correct(text)
print(text.correct())
