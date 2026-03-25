# autogen-plasmate

Plasmate web browsing tool for AutoGen agents. Get clean semantic page content using 10-16x fewer tokens than Chrome.

## Install

```bash
pip install autogen-plasmate
```

## Usage

```python
from autogen import ConversableAgent, register_function
from autogen_plasmate import plasmate_fetch

assistant = ConversableAgent("assistant", llm_config={"model": "gpt-4o"})
user = ConversableAgent("user", human_input_mode="NEVER")
register_function(plasmate_fetch, caller=assistant, executor=user,
                  name="plasmate_fetch", description="Fetch a web page as semantic content")
user.initiate_chat(assistant, message="Fetch https://example.com and summarize it")
```

## What is Plasmate?

[Plasmate](https://plasmate.dev) is a lightweight web browsing engine for AI agents. It returns a Semantic Object Model (SOM) instead of raw HTML, reducing token usage by 10-16x compared to headless Chrome.

## Links

- [Plasmate Documentation](https://plasmate.dev)
- [W3C Web Agents Community Group](https://www.w3.org/community/web-agents/)
- [GitHub](https://github.com/nicobailey/plasmate)

## License

Apache 2.0
