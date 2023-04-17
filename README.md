# MovieGPT-lang-summarization
LLM Summarization for MovieGPT

## TODO

### 1. LLM summarization interface

Implement an interface to collect LLM summaries using

1. WIP: GPT3

  - ~~notebook example~~
  
  - ~~[Chains in langchain](https://docs.langchain.com/docs/components/chains/index_related_chains) circumvent 4k token limit.~~

### 2. PG:Playground at small scale

- Visualization tool? for insecting 10-100s summaries.

- Get ETA for 12k videos?

## Inbox

### Scope 1: Better/Cheaper? summarization pipelines

1. ChatGPT

  - Pro: Prompt engineering in the browser.
  Over there, the results retained the "<>".
  
    BTW, Retaining the <> is irrelevant if they are not accurate.
    Isn't it easier to desinging a matching module from summary to raw than come up with such prompt?
    By doing so, we could finetune GPT3 😉

2. [HuggingFace (e.g., T5)](https://huggingface.co/docs/transformers/tasks/summarization), other tools [suggested by PIs](assets/ai-as-pi.md)

3. Look into any of the public project of [GPT3 project/plugin universe]().
  For examples, [arxiv summarize]().
