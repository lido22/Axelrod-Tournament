import os
import importlib.util
from typing import Callable
from outcomes import Outcome
from matplotlib import pyplot as plt

scores:dict[str, list[int]]= {}
functions:dict[str, Callable]= {}
agents:list[str]= []

def load_agents():
    global scores
    global functions
    global agents
    agents_directory = "./agents"
    function_name = "play"
    for filename in os.listdir(agents_directory):
        # Check if the file is a Python file
        if filename.endswith(".py"):
            # Remove the .py extension to get the module name
            module_name = filename[:-3]

            # Construct the full module path
            module_path = os.path.join(agents_directory, filename)

            # Load the module dynamically
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Check if the function exists in the module
            if hasattr(module, function_name):
                # init score
                scores[module_name] = [0]
                agents.append(module_name)

                function_to_call = getattr(module, function_name)
                functions[module_name] = function_to_call
            else:
                print(f"Function '{function_name}' not found in module '{module_name}'")


def play_game(number_of_rounds:int = 100):
    global scores
    global functions
    global agents
    for i in range(len(agents)):
        for j in range(i+1, len(agents)):
            first_agent_name = agents[i]
            second_agent_name = agents[j]
            first_agent_history = []
            second_agent_history = []
            for _ in range(number_of_rounds):
                # playing the round
                first_agent_outcome = functions[first_agent_name](second_agent_history, first_agent_history)
                second_agent_outcome = functions[second_agent_name](first_agent_history, second_agent_history)

                #calculating the scores
                first_agent_score, second_agent_score = calculate_score(first_agent_outcome, second_agent_outcome)
                scores[first_agent_name].append(scores[first_agent_name][-1]+first_agent_score)
                scores[second_agent_name].append(scores[second_agent_name][-1]+second_agent_score)

                #updating history
                first_agent_history.append(first_agent_outcome)
                second_agent_history.append(second_agent_outcome)

def calculate_score(first_agent_outcome:Outcome, second_agent_outcome:Outcome)->tuple[int,int]:
    # two cooperated
    if first_agent_outcome.value * second_agent_outcome.value == 1:
        return 3, 3

    # the two defected
    if first_agent_outcome.value + second_agent_outcome.value == 0:
        return 1, 1

    # first cooperated and the second defected
    if first_agent_outcome.value > second_agent_outcome.value:
        return 0, 5
    # second cooperated and the first defected
    return 5, 0


load_agents()
play_game()
for agent in agents:
    plt.plot(scores[agent], label=agent)

    # Add labels, title, and legend
plt.xlabel("Time Steps")
plt.ylabel("Score")
plt.title("Score of Multiple Agents Over Time")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()