# MovieGPT-lang-summarization

LLM Summarization for MovieGPT

## TODO

### 1. LLM summarization interface

Implement an interface to collect LLM summaries using

1. Play with a dialog with `1EuwzHn9JEM.csv`

  1. Update notebook to use gpt-3.5-turbo

  1. Play with prompts:

      - "-/engaging"

      - "movie summary/plot/trailer", "movie plot summary"

      - steer the length: "with 300 words"

_Questions_

1. How to circumvent 4k token limit?

    [langchain](https://python.langchain.com/en/latest/index.html).

### 2. PG:Playground at small scale

_Scope: Get ETA & ETP for 12k videos._

1. Play with a small subset of the data (e.g., 100 videos) to get a sense of the interface.

1. Dispatch bulk summarization jobs to LLM.

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
