import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


class Round:
    # Constructor to initialize the round with an ID and an empty matches graph
    def __init__(self, id):
        self.__id = id
        self.__matches = nx.Graph()

    # Property to get the ID of the round
    @property
    def id(self):
        return self.__id

    # Setter to set the ID of the round
    @id.setter
    def id(self, id):
        self.__id = id

    # Property to get the matches graph
    @property
    def matches(self):
        return self.__matches

    # Setter to set the matches graph
    @matches.setter
    def matches(self, matches):
        self.__matches = matches

    # Method to check if a team is a home team
    def is_home_team(self, acronym):
        return (
            acronym in self.matches
            and self.matches.nodes[acronym].get("bipartite") == 0
        )

    # Method to check if a team is an away team
    def is_away_team(self, acronym):
        return (
            acronym in self.matches
            and self.matches.nodes[acronym].get("bipartite") == 1
        )

    # Method for check if a team is participating in the round
    def is_team_in_round(self, acronym):
        return self.is_home_team(acronym) or self.is_away_team(acronym)

    # Method for check if the round is valid
    def is_valid_round(self, number_of_teams):
        return len(self.matches.edges()) == (number_of_teams // 2)

    # Method to add a team as a home team
    def add_home_team(self, acronym):
        if self.is_home_team(acronym) or self.is_away_team(acronym):
            raise ValueError(f"Team {acronym} already exists.")
        self.matches.add_node(acronym, bipartite=0)

    # Method to add a team as an away team
    def add_away_team(self, acronym):
        if self.is_home_team(acronym) or self.is_away_team(acronym):
            raise ValueError(f"Team {acronym} already exists.")
        self.matches.add_node(acronym, bipartite=1)

    # Method to create a match pair between a home team and an away team
    def create_match_pair(self, home_team_acronym, away_team_acronym):
        if not self.is_home_team(home_team_acronym):
            raise ValueError(
                f"Home team {home_team_acronym} does not exist or is not a home team."
            )
        if not self.is_away_team(away_team_acronym):
            raise ValueError(
                f"Away team {away_team_acronym} does not exist or is not an away team."
            )

        self.matches.add_edge(home_team_acronym, away_team_acronym)

    # Method to clear all matches from the round
    def reset_matches(self):
        self.__matches.clear()

    # Method to generate and save a bipartite graph image
    def generate_bipartite_graph_image(self, directory):
        # Create a layout for the bipartite graph
        home_teams = {
            node
            for node, data in self.matches.nodes(data=True)
            if data["bipartite"] == 0
        }
        away_teams = set(self.matches) - home_teams

        pos = {}
        pos.update((node, (1, index)) for index, node in enumerate(home_teams))
        pos.update((node, (2, index)) for index, node in enumerate(away_teams))

        # Filename based on the round ID
        filename = f"Round_{self.__id}.png"
        filepath = f"{directory}/{filename}"

        # Draw the graph with a resolution of 1920x1080
        plt.figure(figsize=(19.2, 10.8))
        ax = plt.gca()
        ax.margins(0.1)  # Add margins around the graph
        nx.draw(
            self.matches,
            pos,
            with_labels=True,
            node_color=[
                "skyblue" if node in home_teams else "lightgreen"
                for node in self.matches
            ],
            ax=ax,
        )

        # Add legend
        legend_elements = [
            Patch(facecolor="skyblue", edgecolor="k", label="Home Teams"),
            Patch(facecolor="lightgreen", edgecolor="k", label="Away Teams"),
        ]
        plt.legend(handles=legend_elements, loc="upper right")

        plt.title(f"Round {self.__id}")
        plt.savefig(filepath)
        plt.close()
