# MovieGPT-lang-summarization

LLM Summarization for MovieGPT

## TODO

### 1. LLM summarization interface

_Milestone: Implement class to collect LLM summaries_

1. Finish [summarize.py](./src/summarize.py) module.

  1. Write dummy unit test in "__main__" using dialog with `1EuwzHn9JEM.csv`

1. Play with prompts:

    - "-/engaging"

    - "movie summary/plot/trailer", "movie plot summary"

    - steer the length: "with 300 words"

1. Augment dummy unit test with dialogs with less than `4000 chars / 4` chars.

_Questions_

1. Do we need a if-else to handle dialogs <= 4k token limit?

    For those langchain stuff is enough, reducing API calls 😉

~~1. How to circumvent 4k token limit?~~

    [langchain map_reduce or refine](https://python.langchain.com/en/latest/index.html).

### 2. PG:Playground at small scale

_Milestone: Get ETA & ETP for 12k videos._

1. Run [data wandering notebook](./notebooks/02_data-wandering.ipynb) over ~30 videos with 10 bins. Get ETA & ETP for 12k videos.

  1. Record summaries onto JSON.

1. Dispatch bulk summarization for 100 & 1k videos

### 3. PG:Playground visualization

_Milestone: Visualization tool to map sentence in summaries onto raw dialogs._

> Can be done concurrently with [T2](#2-pgplayground-at-small-scale)

1. Build visualization tool

1. Play with a small subset of the data (e.g., 10, 100 videos) to get a sense of LLM summarization hyper-params.

## Inbox

1. [HuggingFace (e.g., T5)](https://huggingface.co/docs/transformers/tasks/summarization).

  _Added: 2023-04-?_

  - [LangChain with HF-T5](https://python.langchain.com/en/latest/modules/models/llms/integrations/huggingface_hub.html)

    _Added: 2023-04-18_

1. [LangChain and LlamaCpp](https://python.langchain.com/en/latest/modules/models/llms/integrations/llamacpp.html)

  _Added: 2023-04-18_

1. Try other tools [suggested by PIs](assets/ai-as-pi.md)

  _Added: 2023-04-?_

1. Check ChatGPT

  _Added: 2023-04-?_

1. Look into any of the public project of [GPT3 project/plugin universe](). For examples, [arxiv summarize]().

  _Added: 2023-04-?_
