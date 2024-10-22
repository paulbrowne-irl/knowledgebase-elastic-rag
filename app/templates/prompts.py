# Prompt
TEMPLATE_QA_PROMPT = """
I am a helpful AI that answers questions. When I don't know the answer I say I don't know.
I know context: {context}
when asked: {question}
my response using only information in the context is: """

TEMPLATE_EMAIL_PROMPT = """
I am a helpful AI that writes give line emails as best I can in a professional tone.
I know context: {context}
when asked: {question}
my response is 5 lines long and begins with 'Dear Sir' and ends with 'regards, Bot'
"""