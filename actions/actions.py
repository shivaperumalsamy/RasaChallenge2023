from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from server.chatgpt import chat_gpt_request, parse_file_and_get_answer

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        print("Inside actions")

        print((tracker.latest_message)['text'])

        # Calling file to fetch content
        response = parse_file_and_get_answer((tracker.latest_message)['text'])
        print(response)
        dispatcher.utter_message(text=response)
        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]