from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch  # langchain-tavily

load_dotenv()


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():

    # content = "What is the weather in Tokyo?"
    content = "search for 3 job posting for an ai engineer using langchain in monterrey mexico on linkedin and list their details"

    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content=content)})
    print(result)


if __name__ == "__main__":
    main()
