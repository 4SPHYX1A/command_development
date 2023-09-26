def get_greeting_message(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    m =  get_greeting_message("John Doe")
    print(m)

