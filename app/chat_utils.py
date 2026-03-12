from euriai.langchain import create_chat_model

API_KEY = None
MODEL = "gpt-4.1-nano"
TEMPERATURE = 0.7

def get_chat_model(api_key: str = None):
    return create_chat_model(
        api_key=api_key or API_KEY,
        model=MODEL,
        temperature=TEMPERATURE
    )

def ask_chat_model(chat_model, prompt: str):
    """Invoke the chat model and return the text response.

    If the underlying HTTP client raises an HTTPError we catch it so that the
    caller can see a clearer message (for example, bad API key or rate limit
    exceeded).
    """
    try:
        response = chat_model.invoke(prompt)
    except Exception as err:
        # The euriai client uses ``requests`` internally; ``raise_for_status``
        # will yield an HTTPError on 4xx/5xx codes. Detect unauthorizeds and
        # provide a helpful hint.
        from requests.exceptions import HTTPError

        if isinstance(err, HTTPError) and err.response is not None:
            status = err.response.status_code
            if status == 401:
                raise RuntimeError(
                    "Unauthorized: check that your EURI_API_KEY is valid and "
                    "has not expired or been revoked."
                ) from err
        # Re‑raise whatever we got if it's not something we special‑case.
        raise

    return response.content
