# === Fake API Keys for Testing ===

# OpenAI
openai_api_key = "sk-1234567890abcdefghijklmnopqrstuv"

# HuggingFace
hf_token = "hf_abcd1234efgh5678ijkl"

# Groq
groq_key = "gsk_0987lkjh6543mnbv"

# AWS
aws_secret_key = "AKIAIOSFODNN7EXAMPLE"

# Google Gemini (Google API key format)
google_key = "AIzaSyAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQ"

# Stripe
stripe_key = "sk_live_abc1234567890xyzABC"

# GitHub
github_token = "ghp_abcdefghijklmnopqrstuvwxyz123456"

# Non-critical examples (local dev or dummy)
fake_key = "local_dev_key_test"
another_key = "123456789"

# Noise (no keys here)
random_text = "This is a normal line without a key."

# Multi-step assignments
a = "hf_fake_token_value"
token = a

tmp = "gsk_fakegroqvalue"
groq_token = tmp

# Google Gemini in request param (test API key usage detection)
key = "AIzaSyZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
    params={"key": key}
)


# Literal 'keyword' variable
keyword = "sk-abc123EXAMPLEKEYFOROPENAI"

# Generic but sensitive-looking variable name
secret = "hf_fakehuggingfaceKEY999"

# Very ambiguous variable name, still should match by value
access = "ghp_abcdEFGHijklMNOPqrstUVWXYZ123456"

config = {
    "auth": {
        "key": "sk-abc987EXAMPLEKEY",
        "backup_key": "hf_extraKEY_EXAMPLE123"
    }
}

# in a list
keys = ["sk-live-fakevalueEXAMPLE", "hf_anotherFakeKeyExample"]

# key in an object or class
class Auth:
    def __init__(self):
        self.api_key = "sk-embeddedKEYEXAMPLE"
        self.hf = "hf_AnotherHiddenKeyExample"

# via join
openai_key = "".join(["sk-", "abc", "123", "EXAMPLE", "KEY"])

