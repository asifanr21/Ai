class VacuumEnvironment:
    def __init__(self):
        # Initializing locations A and B randomly with dirty (1) or clean (0) status
        import random
        self.locations = {
            'A': random.choice([0, 1]),
            'B': random.choice([0, 1])
        }
        # Start the vacuum at a random location
        self.vacuum_location = random.choice(['A', 'B'])

    def display_status(self):
        print(f"Current Environment Status -> Location A: {'Dirty' if self.locations['A'] else 'Clean'}, Location B: {'Dirty' if self.locations['B'] else 'Clean'}")
        print(f"Vacuum Cleaner is currently at Location: {self.vacuum_location}\n")

    def is_completely_clean(self):
        return self.locations['A'] == 0 and self.locations['B'] == 0


def reflex_vacuum_agent(location, status):
    """
    Determines the next action based on the current location and its status.
    """
    if status == 1:  # 1 means Dirty
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'


def run_simulation():
    # Setup the environment
    env = VacuumEnvironment()
    print("--- Starting Vacuum Cleaner Simulation ---")
    env.display_status()
    
    steps = 0
    # Run the vacuum until both locations are clean
    while not env.is_completely_clean() and steps < 10:
        steps += 1
        current_loc = env.vacuum_location
        current_status = env.locations[current_loc]
        
        # Agent decides the action based on current percepts
        action = reflex_vacuum_agent(current_loc, current_status)
        print(f"[Step {steps}] Perceived: ({current_loc}, {'Dirty' if current_status else 'Clean'}) -> Action: {action}")
        
        # Execute the action inside the environment
        if action == 'Suck':
            env.locations[current_loc] = 0  # Clean the location
            print(f"-> Successfully cleaned Location {current_loc}.")
        elif action == 'Right':
            env.vacuum_location = 'B'
            print("-> Moved to Location B.")
        elif action == 'Left':
            env.vacuum_location = 'A'
            print("-> Moved to Location A.")
        
        env.display_status()
        
    print(f"Simulation ended in {steps} steps. All rooms are clean!")

if __name__ == "__main__":
    run_simulation()
