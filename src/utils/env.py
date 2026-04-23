import os

def expand_env_vars(text: str) -> str:
    expanded = os.path.expandvars(text)

    if "${" in expanded:
        raise ValueError("Unresolved environment variables in input")

    return expanded