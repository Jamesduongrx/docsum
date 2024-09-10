import os
import re
import time


max_chunk_input = 30000
#rate limit 30,000 tokens maxed
def split_document_into_chunks(text,chunk_size=max_chunk_input):
    paragraph = re.split(r'[.!?] +',text)
    chunks = []
    current_chunk = ""


    for sentence in paragraph:
        sentence_size = len(sentence)


        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence
        else:

            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def summarize(text, client):
    '''
    We need to call the split_document_into_chunks on text.
    Then for each paragraph in the output list,
    call the LLM code below to summarize it.
    Put the summary into a new list.
    Concatenate that new list into one smaller document.
    Recall the LLM code below on the new smaller document.
    '''
    chunks = split_document_into_chunks(text)
    summarized_chunks = []


    # Summarize each chunk
    for chunk in chunks:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'system',
                    'content': 'Summarize the input text below.  Limit the summary to 1 paragraph and use a 1st grade reading level.',
                },
                {
                    "role": "user",
                    "content": chunk,
                }
            ],
            model="llama3-8b-8192",
        )
        summary = chat_completion.choices[0].message.content
        summarized_chunks.append(summary)


    combined_summary = ' '.join(summarized_chunks)


    return combined_summary
 


 


if __name__ == '__main__':

    import doctest 
    import os
    from groq import Groq


    # parse command line args
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    client = Groq(
        # This is the default and can be omitted
        api_key=os.environ.get("GROQ_API_KEY"),
    )

#find out why utf-32 doesn't work. "BOM"
# need to encode it for file to access new characters from mx.txt
    with open(args.filename, encoding='utf-8') as f:
        text = f.read()




    final_summary = summarize(text, client)



    print(final_summary)