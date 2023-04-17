# ChatGPT as Resarch Principal Investigator

## 2023-04-15

### Junior researcher

suggest text summarization code or apiss

### Principal investigator

There are various text summarization codes and APIs available that you can use to generate summaries of your text. Here are a few popular options:

    Python's NLTK library: NLTK (Natural Language Toolkit) is a popular Python library for natural language processing, including text summarization. You can use NLTK's Summarizer class to generate summaries of your text. Here's an example code snippet:

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

def summarize(text, n):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)
    word_freq = FreqDist(words)

    ranking = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if i not in ranking:
                    ranking[i] = word_freq[word]
                else:
                    ranking[i] += word_freq[word]

    top_sentences = nlargest(n, ranking, key=ranking.get)
    summary = ' '.join([sentences[i] for i in sorted(top_sentences)])
    return summary
```

Here, text is the input text that you want to summarize, and n is the number of sentences you want in the summary. The summarize function uses NLTK to tokenize the text, calculate the frequency distribution of words, and rank the sentences based on the frequency of their words. It then selects the top n sentences with the highest ranking and concatenates them to form the summary.

    GPT-3 API: OpenAI's GPT-3 is a powerful language model that can be used for various NLP tasks, including text summarization. OpenAI provides an API that allows you to use GPT-3 to generate summaries of your text. Here's an example code snippet using the OpenAI API:

```python
import openai
openai.api_key = "YOUR_API_KEY"

def summarize(text):
    prompt = f"Please summarize the following text:\n{text}"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=60,
      n=1,
      stop=None,
      temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary
```

Here, text is the input text that you want to summarize. The summarize function uses the GPT-3 API to generate a summary of the input text. The max_tokens parameter controls the maximum number of tokens in the generated summary, and the temperature parameter controls the creativity of the generated text.

    TextRank algorithm: TextRank is a graph-based algorithm for text summarization that uses PageRank to rank sentences based on their importance in the text. There are various implementations of TextRank available, such as the one in the sumy library for Python. Here's an example code snippet:

```python
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize(text, n):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    sentences = summarizer(parser.document, n)
    summary = ' '.join(str(sentence) for sentence in sentences)
    return summary
```

Here, text is the input text that you want to summarize, and n is the number of sentences you want in the summary. The summarize function

### Junior researcher

which is it scalable for 12k long movie dialogs?

### Principal investigator

The scalability of text summarization algorithms depends on several factors, such as the size of the input text, the complexity of the algorithm, and the computing resources available.

For 12k long movie dialogs, the scalability of the algorithm will depend on the specific algorithm and implementation used. Some text summarization algorithms may struggle with processing such a large amount of data, while others may be able to handle it efficiently.

In general, some algorithms may require significant computing resources, such as memory and processing power, to process such a large amount of data. Additionally, some algorithms may require additional preprocessing steps, such as cleaning and formatting the input data, to ensure optimal performance.

It is important to consider the specific needs and requirements of the task at hand when selecting a text summarization algorithm. In some cases, it may be necessary to use a distributed computing approach or to optimize the algorithm for the specific use case to ensure scalability.

### Junior researcher

i need a concrete answer rank previous suggestions, the deadline is approaching

### Principal investigator

Certainly, here's my ranking of the previous suggestions, based on the scalability of the algorithms for summarizing a large amount of data such as 12k long movie dialogs:

    GPT-3 API: The GPT-3 API is highly scalable and can handle large amounts of data with ease. It uses state-of-the-art language models and is specifically designed to generate human-like summaries. However, it requires an API key and may come at a cost, depending on the usage.

    TextRank algorithm: TextRank is a graph-based algorithm that is scalable and efficient for summarizing large amounts of text. It uses PageRank to rank sentences based on their importance, which can be effective for generating informative summaries. The sumy library provides a straightforward implementation of the algorithm.

    Python's NLTK library: The NLTK library is a popular natural language processing library for Python, and it includes a simple implementation of a text summarization algorithm. However, the algorithm may not be as efficient as the other options on this list for summarizing large amounts of data, and it may require additional preprocessing steps to ensure optimal performance.

Overall, based on the scalability of the algorithms for processing large amounts of data, I would recommend using the GPT-3 API or the TextRank algorithm, depending on your specific needs and resources. The NLTK library could also be a viable option, but it may require additional preprocessing and optimization steps to ensure optimal performance.
