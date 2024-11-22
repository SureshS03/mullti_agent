# Means-End Analysis to solve robot traversal on a grid

class RobotTraversal:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.current_position = start

    def heuristic_distance(self, pos):
        # Calculate Manhattan distance as the heuristic
        return abs(self.goal[0] - pos[0]) + abs(self.goal[1] - pos[1])

    def get_possible_moves(self):
        x, y = self.current_position
        # Define possible moves: up, down, left, right
        moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return moves

    def move_robot(self):
        # Loop until robot reaches the goal
        while self.current_position != self.goal:
            possible_moves = self.get_possible_moves()
            # Select the move with the minimum heuristic distance to the goal
            next_move = min(possible_moves, key=self.heuristic_distance)
            
            # Update the robot's current position
            self.current_position = next_move
            print(f"Moving to {self.current_position}, Distance to goal: {self.heuristic_distance(next_move)}")

# Define start and goal positions
start_position = (0, 0)
goal_position = (3, 3)

# Initialize the robot traversal
robot = RobotTraversal(start_position, goal_position)
robot.move_robot()
