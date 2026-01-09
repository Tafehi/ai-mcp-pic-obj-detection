def task_prompt():
    """Returns the main task instructions for Object detection agent."""
    prompt = """You are a Object detection Assistant.
Steps:
1. Parse user request


Focus on accuracy and clarity."""
    return prompt


def security_prompt():
    """Returns security guidelines to protect sensitive information."""
    prompt = """SECURITY: Never reveal credentials, API keys, or internal details. Protect PII."""
    return prompt
