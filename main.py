class MazeSolver:
    """
    A class which accepts a maze file input (or array input) and outputs the solution.
    """
    def __init__(self, startPos, inputFilename=None, inputArray=None):
        """
        Initialize a new MazeSolver instance
        :param startPos: The coordinate of the starting position
        :param inputFilename: An input file containing the maze
        :param inputArray: Optionally, we can input an array instead of a file
        """
        self.startPos = startPos
        self.stack = []
        self.START_CHAR = "S"
        self.FINISH_CHAR = "F"
        self.WALL_CHAR = "*"
        self.PATH_CHAR = "o"
        if (inputArray == None):
            with open(inputFilename, "r+") as raw:
                self.maze = raw.readlines()
                self.maze = [list(i.replace("\n", "")) for i in self.maze]
        else:
            self.maze = inputArray

    def get_height(self):
        """
        Get the height of the maze
        :return: The height as an integer
        """
        return len(self.maze)

    def get_width(self):
        """
        Get the width of the maze
        :return: The width as an integer
        """
        return len(self.maze[0])

    def get_wall_char(self):
        """
        Get the character that marks a wall (default="*")
        :return: The wall character as a string
        """
        return self.WALL_CHAR

    def set_wall_char(self, char):
        """
        Set the wall character
        :param char: A single character for marking walls
        :return: A boolean True if the character is accepted, else False
        """
        if len(char) == 1:
            self.WALL_CHAR = char
            return True
        return False

    def get_path_char(self):
        """
        Get the character that marks the path traveled (default="o")
        :return: The path character as a string
        """
        return self.PATH_CHAR

    def set_path_char(self, char):
        """
        Set the path character
        :param char: A single character for marking path traveled
        :return: A boolean True if the character is accepted, else False
        """
        if len(char) == 1:
            self.PATH_CHAR = char
            return True
        return False

    def get_start_char(self):
        """
        Get the starting character (default="S")
        :return: The starting character as a string
        """
        return self.START_CHAR

    def set_start_char(self, char):
        """
        Set the starting character
        :param char: A single character for marking starting character
        :return: A boolean True if the character is accepted, else False
        """
        if len(char) == 1:
            self.START_CHAR = char
            return True
        return False

    def get_finish_char(self):
        """
        Get the finishing character (default="F")
        :return: The finishing character as a string
        """
        return self.FINISH_CHAR

    def set_finish_char(self, char):
        """
        Set the finish character
        :param char: A single character for marking the finish
        :return: A boolean True if the character is accepted, else False
        """
        if len(char) == 1:
            self.FINISH_CHAR = char
            return True
        return False
    
    
    def _check_input(self):
        """
        Confirms that the starting position is a starting character
        :return: Boolean True if starting position is valid, else false
        """
        if self.maze[self.startPos[0]][self.startPos[1]] != self.START_CHAR:
            print("Invalid starting location")
            return False
        return True

    def run(self):
        """
        Run the maze solver by pushing open spaces onto a stack and checking stack locations
        :return: Boolean True if maze is solved, else False
        """
        if self._check_input():
            self.stack.append(self.startPos)
            maze_solved = False
            while not maze_solved:

                try:
                    location = self.stack.pop()
                    if self.maze[location[0]][location[1]] == self.FINISH_CHAR:
                        print("\nSolved the Maze!")
                        maze_solved = True
                        return True
                    else:
                        i,j = location[0], location[1]
                        if self.maze[i][j] != self.PATH_CHAR:
                            self.maze[i][j] = self.PATH_CHAR
                            if self.maze[i+1][j] != self.WALL_CHAR and i + 1 <= self.get_height():
                                self.stack.append((i+1,j))
                            if self.maze[i-1][j] != self.WALL_CHAR and i - 1 > 0:
                                self.stack.append((i-1,j))
                            if self.maze[i][j+1] != self.WALL_CHAR and j + 1 <= self.get_width():
                                self.stack.append((i,j+1))
                            if self.maze[i][j-1] != self.WALL_CHAR and j - 1 > 0:
                                self.stack.append((i,j-1))
                        #print(self.toString())
                except IndexError:
                    #No more pathes to check
                    print("\nThis maze does not have a solution!")
                    maze_solved = True
                    return False

    def toString(self):
        """
        Get the string representation of the maze
        :return: A string representation
        """
        result = ""
        for i in self.maze:
            for j in i:
                result += str(j)
            result += "\n"
        return result


# test code with runner
if __name__ == "__main__":
    mazeTrue = MazeSolver((4, 0), inputFilename="example_mazes/maze.txt")
    print("Expected True: " + str(mazeTrue.run()))
    print(mazeTrue.toString())

    mazeFalse = MazeSolver((4, 0), inputFilename="example_mazes/maze_impossible.txt")
    print("Expected False: " + str(mazeFalse.run()))
    print(mazeFalse.toString())
