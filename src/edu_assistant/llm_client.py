import os
from openai import OpenAI

from edu_assistant.config import LLMConfig


def get_llm_client(llm_config: LLMConfig) -> OpenAI:
    # Get client to call LLM
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    return OpenAI(
            api_key=api_key,
            base_url=llm_config.base_url,
            timeout=llm_config.timeout,
        )
