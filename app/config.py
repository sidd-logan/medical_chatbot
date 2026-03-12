import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
# The Euri API key is required to interact with the chat completions endpoint.
# It's best to keep keys out of source control, so we first look for an
# environment variable. You can also hard‑code a value here for quick tests,
# but make sure to remove it before committing.

API_KEY = os.environ["OPENAI_API_KEY"]

# sanity check so the app fails fast with a meaningful message instead of
# a confusing 401 from the HTTP client.
if not API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable is not set. "
        "Please export a valid key or set it in app/config.py."
    )
