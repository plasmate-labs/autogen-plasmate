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


---

## Part of the Plasmate Ecosystem

| | |
|---|---|
| **Engine** | [plasmate](https://github.com/plasmate-labs/plasmate) - The browser engine for agents |
| **MCP** | [plasmate-mcp](https://github.com/plasmate-labs/plasmate-mcp) - Claude Code, Cursor, Windsurf |
| **Extension** | [plasmate-extension](https://github.com/plasmate-labs/plasmate-extension) - Chrome cookie export |
| **SDKs** | [Python](https://github.com/plasmate-labs/plasmate-python) / [Node.js](https://github.com/plasmate-labs/quickstart-node) / [Go](https://docs.plasmate.app/sdk-go) / [Rust](https://github.com/plasmate-labs/quickstart-rust) |
| **Frameworks** | [LangChain](https://github.com/langchain-ai/langchain/pull/36208) / [CrewAI](https://github.com/plasmate-labs/crewai-plasmate) / [AutoGen](https://github.com/plasmate-labs/autogen-plasmate) / [Smolagents](https://github.com/plasmate-labs/smolagents-plasmate) |
| **Tools** | [Scrapy](https://github.com/plasmate-labs/scrapy-plasmate) / [Audit](https://github.com/plasmate-labs/plasmate-audit) / [A11y](https://github.com/plasmate-labs/plasmate-a11y) / [GitHub Action](https://github.com/plasmate-labs/som-action) |
| **Resources** | [Awesome Plasmate](https://github.com/plasmate-labs/awesome-plasmate) / [Notebooks](https://github.com/plasmate-labs/notebooks) / [Benchmarks](https://github.com/plasmate-labs/plasmate-benchmarks) |
| **Docs** | [docs.plasmate.app](https://docs.plasmate.app) |
| **W3C** | [Web Content Browser for AI Agents](https://www.w3.org/community/web-content-browser-ai/) |
