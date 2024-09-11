# docsum![](https://github.com/Jamesduongrx/docsum/actions/workflows/test.yml/badge.svg)
Docsum.py is a script that reads a text file and uses Groq API to generate a summary for the user. 

# Getting Started
Install Groq, and generate a free Groq API key,https://console.groq.com/keys. Create an .env file through the terminal and add the generated key:
```
GROQ_API_KEY=your_api_key_here
```
The following example summarizes the declaration of independence.

```
$ python3 docsum.py docs/declaration.txt
A long time ago, some people in America decided they wanted to be free. They were tired of being ruled by a king from a faraway land. The king was being mean and taking away their rights. The people wrote a special paper to say they were free and independent. They said they didn't want to be ruled by the king anymore. They promised to work together and take care of each other to make sure they stayed safe and happy. This paper is called the Declaration of Independence. It's like a big declaration that says, "We are free and we're going to make our own decisions!"
```
