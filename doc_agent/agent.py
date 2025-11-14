from os import write
from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from .writer_agent.agent import writer_agent
from doc_agent.tools import write_doc

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A documentation search agent that helps users find relevant information in the documentation.',
    instruction="""
        You will assist users by searching the documentation for relevant information based on their queries.
        You accept a Swift keyword and return the definition and usage in Clojure map format.

        Output Requirements:
        Clojure map with the following keys:
        - {
           :keyword {keyword?}
           :definition {definition?}
           :usage {usage?}
           }
        """,
    sub_agents=[writer_agent],
    tools=[FunctionTool(write_doc)],
    output_key="documentation",
)
