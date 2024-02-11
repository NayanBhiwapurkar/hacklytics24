import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory

from .traversaal import get_search_from_traversaal
from .utils import augment_prompt




class InnSight:
    def __init__(self):
        self.chat = ChatOpenAI(
            openai_api_key=os.environ["OPENAI_API_KEY"],
            model='gpt-3.5-turbo'
        )

        first_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """I want you to act as a travel guide. Answer all questions to the best of your ability.
                        and explain why your answer satisfies the user's preference."""
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        self.chain = first_prompt | self.chat
        self.demo_ephemeral_chat_history = ChatMessageHistory()

    def _trim_messages(self):
        stored_messages = self.demo_ephemeral_chat_history.messages
        N_MESSAGES = 6
        if len(stored_messages) <= N_MESSAGES:
            return False

        self.demo_ephemeral_chat_history.clear()

        for message in stored_messages[-N_MESSAGES:]:
            self.demo_ephemeral_chat_history.add_message(message)

        return True


    def answer_user_prompt(self, prompt: str):
        self._trim_messages()

        self.demo_ephemeral_chat_history.add_user_message(prompt)
        internet_search_results = get_search_from_traversaal(prompt)
        prompt = augment_prompt(prompt, n_points=3, internet_search_results=internet_search_results)
        ai_response = self.chain.invoke(
            {
                "messages": self.demo_ephemeral_chat_history.messages,
            }
        )
        self.demo_ephemeral_chat_history.add_ai_message(ai_response)

        return ai_response.content