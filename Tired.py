import random

def push_rank():
    options = [
        "\n\n\n\n\t\t\t\t\t\tYes, masih awal ni >:(\n\n\n",
        "\n\n\n\n\t\t\t\t\t\t15 mins break\n\n\n",
        "\n\n\n\n\t\t\t\t\t\tHmm... sikit lagi lah\n\n\n",
        "\n\n\n\n\t\t\t\t\t\tRest now, u've done enough for today\n\n\n"
    ]
    return random.choice(options)

input("\n\n\n\n\t\t\t\t\t\tshould i continue studying ? ")

print(push_rank())