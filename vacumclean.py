import random

class VacuumEnvironment:
    def __init__(self):
        self.locations = {
            'A': random.choice([0, 1]),
            'B': random.choice([0, 1])
        }
        self.vacuum_location = random.choice(['A', 'B'])

    def display_status(self):
        print(f"Current Environment Status -> Location A: {'Dirty' if self.locations['A'] else 'Clean'}, Location B: {'Dirty' if self.locations['B'] else 'Clean'}")
        print(f"Vacuum Cleaner is currently at Location: {self.vacuum_location}\n")

    def is_completely_clean(self):
        return self.locations['A'] == 0 and self.locations['B'] == 0

def reflex_vacuum_agent(location, status, env):
    """
    Determines the next action to ensure Location A is cleaned first,
    then Location B.
    """
    if status == 1:
        return 'Suck'
    
    if env.locations['A'] == 1 and location != 'A':
        return 'Left'
    
    if env.locations['A'] == 0 and env.locations['B'] == 1 and location != 'B':
        return 'Right'

    return 'NoOp'

def run_simulation():
    env = VacuumEnvironment()
    print("--- Starting Sequential Vacuum Cleaner Simulation (A then B) ---")
    env.display_status()
    
    steps = 0
    
    if env.is_completely_clean():
        print("Initial State: Both locations are already clean!")
        return


    while not env.is_completely_clean() and steps < 10:
        steps += 1
        current_loc = env.vacuum_location
        current_status = env.locations[current_loc]
        
        action = reflex_vacuum_agent(current_loc, current_status, env)
        
        print(f"[Step {steps}] Perceived: ({current_loc}, {'Dirty' if current_status else 'Clean'}) -> Action: {action}")
        
        if action == 'Suck':
            env.locations[current_loc] = 0
            print(f"-> Successfully cleaned Location {current_loc}.")
        elif action == 'Right':
            env.vacuum_location = 'B'
            print("-> Moved to Location B.")
        elif action == 'Left':
            env.vacuum_location = 'A'
            print("-> Moved to Location A.")
        elif action == 'NoOp':
            print("-> No action needed.")
            break
            
        env.display_status()

    if env.is_completely_clean():
        print(f"Simulation ended successfully in {steps} steps. All rooms are clean!")
    else:
        print(f"Simulation stopped after reaching the maximum limit of {steps} steps.")

if __name__ == "__main__":
    run_simulation()
