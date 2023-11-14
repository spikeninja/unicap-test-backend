import random


def get_random_user_agent(user_agents_path: str) -> str:
    """"""

    with open(user_agents_path, "r") as f:
        text = f.read()

    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '']

    return random.choice(lines)


if __name__ == "__main__":
    user_agent = get_random_user_agent('./user_agents.txt')
    print("user agent: ", user_agent)
