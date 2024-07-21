import networkx as nx
import matplotlib.pyplot as plt
from .team import Team


class Championship:
    # Constructor to initialize the championship with a name
    def __init__(self, name):
        self.__restrictions = nx.Graph()
        self.__teams = {}
        self.__name = name

    # Property to get the graph of restrictions
    @property
    def restrictions(self):
        return self.__restrictions

    # Setter to set the graph of restrictions
    @restrictions.setter
    def restrictions(self, restrictions):
        self.__restrictions = restrictions

    # Property to get the dictionary of teams
    @property
    def teams(self):
        return self.__teams

    # Setter to set the dictionary of teams
    @teams.setter
    def teams(self, teams):
        self.__teams = teams

    # Property to get the name of the championship
    @property
    def name(self):
        return self.__name

    # Setter to set the name of the championship
    @name.setter
    def name(self, name):
        self.__name = name

    # Method to add a team to the championship
    def add_team(self, acronym, name, city):
        if acronym in self.teams:
            raise ValueError(
                f"Team {name} with acronym {acronym} already exists in the championship."
            )
        self.teams[acronym] = Team(acronym, name, city)
        self.restrictions.add_node(acronym)

    # Private method to get the number of teams
    def __number_of_teams(self):
        return len(self.teams)

    # Method to create restrictions based on teams from the same city
    def create_restrictions(self):
        teams_list = list(self.teams.values())

        for i in range(self.__number_of_teams()):
            for j in range(i + 1, self.__number_of_teams()):
                team1 = teams_list[i]
                team2 = teams_list[j]
                # Add an edge if teams are from the same city but have different acronyms
                if team1.city == team2.city and team1.acronym != team2.acronym:
                    self.restrictions.add_edge(team1.acronym, team2.acronym)

    # Method to generate and save a graph coloring image
    def generate_graph_coloring_image(
        self, directory=".", filename="championship_restrictions_graph.png"
    ):
        # Generate a coloring for the graph
        coloring = nx.coloring.greedy_color(self.restrictions, strategy="largest_first")

        # Create a color map for the nodes
        colors = [coloring[node] for node in self.restrictions.nodes()]

        # Draw the graph
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.restrictions)
        nx.draw(
            self.restrictions,
            pos,
            with_labels=True,
            node_color=colors,
            node_size=500,
            cmap=plt.cm.rainbow,
            font_size=10,
            font_color="black",
        )

        # Construct the full file path
        file_path = directory + "/" + filename if directory else filename

        # Save the image
        plt.savefig(file_path)
        plt.close()
