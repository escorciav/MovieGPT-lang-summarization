"Summarization biz"
import sys
from pathlib import Path
from typing import Any

root_dir = Path.cwd().parent
sys.path.append(str(root_dir))
import config

from langchain import OpenAI, PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter


PROMPT_TEMPLATE = """Write a concise summary of the following:


{text}


CONCISE YET ENGAGING:"""
PROMPT = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"])


class Summarization:
    """Holds all the boilerplate associate with summarizing a possibly long
    document

    Attributes:
        chain: langchain:Chain scheme used for dealing with long docs.

    Usage:
        summary = Summarization()(text)
    """
    def __init__(self, model_name: str = 'gpt-3.5-turbo', chain: str = "stuff",
            text_splitter: CharacterTextSplitter = None, interim_out: bool =False,
            model_kwargs: dict = None, chain_kwargs: dict = None,
            splitter_kwargs: dict = None) -> None:
        """Setup Summarization class

        Args:
            model_name: valid llm langchain model name.
            text_splitter: type of text splitter.
        """
        model_kwargs = {} if model_kwargs is None else model_kwargs
        splitter_kwargs = {} if splitter_kwargs is None else splitter_kwargs
        self.interim_out = interim_out
        if text_splitter is None:
            self.splitter = CharacterTextSplitter(**splitter_kwargs)
        chain_kwargs = self._chain_kwargs(chain) if chain_kwargs is None else chain_kwargs

        self.llm = OpenAI(model_name=model_name, **model_kwargs)
        self.chain = load_summarize_chain(
            self.llm, chain_type=chain, **chain_kwargs
        )

    def summarize(self, text: str, interim_out=False) -> str:
        """Returns a summary out of a possibly long document

        Args:
            text (str): text to summarize
            interim_out (bool, optional): whether to return intermediate steps.
        """
        interim_out = self.interim_out or interim_out

        # TODO: TIER-2. Is text_splitter really needed? EOM - Victor.
        text = self.splitter.split_text(text)
        doc = Document(page_content=text)
        out = self.chain(
            {"input_documents": doc}, return_only_outputs=self.interim_out
        )
        if not interim_out:
            summary = out
        else:
            interim |= {
                "doc": doc,
                # TODO: TIER-2. Is splitted_text a public attribute of doc?
                # If so, remove next line 🙂. EOM - Victor.
                'splitted_text': text
            }
            return summary, interim
        return summary

    def _chain_kwargs(self, chain: str) -> dict:
        kwargs = dict(return_intermediate_steps=self.interim_out)
        if chain == 'refine':
            kwargs |= dict(
                question_prompt=PROMPT,
                refine_prompt=REFINE_PROMPT
            )
        elif chain == 'map_reduce':
            kwargs |= dict(
                map_prompt=PROMPT,
                combine_prompt=PROMPT
            )
        else:
            kwargs |= dict(
                prompt=PROMPT
            )
        return kwargs

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.summarize(*args, **kwds)


if __name__ == "__main__":
    aja = Summarization()
    with open(root_dir / "assets/movierecaps000.txt") as f:
        state_of_the_union = f.read()

    model_name = 'text-davinci-003'
    aja = Summarization(model_name)

    # TODO: move this onto Summarize. EOM - Victor.
    chain = load_summarize_chain(llm, chain_type="refine")
    summary = chain.run(docs)

    # **Custom Prompts**
    #
    # You can also use your own prompts with this chain. In this example, we will respond in Italian.
    prompt_template = """Write a concise summary of the following:

    {text}

    CONCISE WHILE RETAINING TIMESTAMPT DELIMITER <> OF THE TEXT:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    refine_template = (
        "Your job is to produce a final summary\n"
        "We have provided an existing summary up to a certain point: {existing_answer}\n"
        "We have the opportunity to refine the existing summary"
        "(only if needed) with some more context below.\n"
        "------------\n"
        "{text}\n"
        "------------\n"
        "Given the new context, refine the original summary."
        "If the context isn't useful, return the original summary."
    )
    refine_prompt = PromptTemplate(
        input_variables=["existing_answer", "text"],
        template=refine_template,
    )
    chain = load_summarize_chain(
        OpenAI(temperature=0), chain_type="refine", return_intermediate_steps=True,
        question_prompt=PROMPT, refine_prompt=refine_prompt
    )
    out = chain({"input_documents": docs}, return_only_outputs=True)
