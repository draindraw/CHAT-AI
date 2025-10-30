import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="API",
)

def get_last_sender(chat_log: str) -> str | None:
    """
    Extracts the sender of the last message in the chat log.
    Works for any sender.
    """
    lines = chat_log.strip().split("\n")

    # Find last non-empty line
    for line in reversed(lines):
        if line.strip():
            last_line = line.strip()
            break
    else:
        return None  # empty log

    # Expected format: [time] Sender: message
    if "]" in last_line and ":" in last_line:
        try:
            sender = last_line.split("]")[1].split(":")[0].strip()
            return sender
        except IndexError:
            return None
    return None


def is_last_from(chat_log: str, name: str) -> bool:
    """
    Returns True if the last message is from the given person (case-insensitive).
    """
    last_sender = get_last_sender(chat_log)
    if last_sender is None:
        return False
    return last_sender.lower() == name.lower()


# Step 1: Click on the chrome icon
pyautogui.click(1183, 1163)
time.sleep(1)  # wait for app to open
while True:

    # Step 2: Drag to select text
    pyautogui.moveTo(663, 183)
    pyautogui.dragTo(1879, 1049, duration=1, button='left')

    # Step 3: Copy selected text (Ctrl + C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)

    # Step 4: Get copied text into a variable
    chat_history = pyperclip.paste()

    print(chat_history)

    if not is_last_from(chat_history, "Debtanu datta"):

        completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {"role": "system","content": "You are a person named debtanu datta who speaks hindi,english as well as bengali. "
            "You are from india and you are a coder. You analyse chat history and respond like debtanu datta. if the person is someone older be respectfull but if the person is a friend you can be disrespectfull when needed. analyse images as well along with text messages."
            "Outputshould be the next chat response (text message only)"},
            {"role": "user","content": chat_history}
        ]
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click target location
        pyautogui.click(1205, 1092)
        time.sleep(0.5)

        # Step 6: Paste the copied text
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        # Step 7: Press Enter
        pyautogui.press("enter")

         # ✅ Exit after sending the message

        exit()
