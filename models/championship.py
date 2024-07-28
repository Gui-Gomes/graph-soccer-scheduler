import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from .team import Team
from .round import Round


class Championship:
    # Constructor to initialize the championship with a name
    def __init__(self, name):
        self.__restrictions = nx.Graph()
        self.__teams = {}
        self.__rounds = {}
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

    # Property to get the dictionary of rounds
    @property
    def rounds(self):
        return self.__rounds

    # Setter to set the dictionary of rounds
    @rounds.setter
    def rounds(self, rounds):
        self.__rounds = rounds

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

    # Private method to get the number of rounds
    def __number_of_rounds(self):
        return (self.__number_of_teams() - 1) * 2

    # Private method to get the number of colors of the colored graph
    def __get_largest_number_of_teams_in_same_city(self):
        return max(dict(self.restrictions.degree()).values()) + 1

    # Private method to initialize the rounds
    def __initialize_rounds(self):
        for i in range(1, self.__number_of_rounds() + 1):
            self.rounds[i] = Round(i)

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

    # Private method to check if there is a restriction between two teams
    def __check_team_restriction(self, home_team_acronym, away_team_acronym):
        return self.restrictions.has_edge(home_team_acronym, away_team_acronym)

    # Private method for check if a valid schedule can be created with city constraints
    def __can_generate_schedule_with_restrictions(self):
        return (
            self.__get_largest_number_of_teams_in_same_city()
            * (self.__number_of_rounds() // 2)
            <= self.__number_of_rounds()
        )

    def generate_round_robin_schedule(self, directory="."):
        number_of_teams = self.__number_of_teams()
        if number_of_teams % 2 != 0:
            raise ValueError("Number of teams must be even.")

        if not self.__can_generate_schedule_with_restrictions():
            print(
                "It's not possible to generate a schedule with the given restrictions."
            )
            return

        self.__initialize_rounds()
        teams = list(self.teams.keys())
        half_rounds = self.__number_of_rounds() // 2

        # Generate the first half of the schedule
        for round_index in range(half_rounds):
            round_instance = self.rounds[round_index + 1]
            random.shuffle(teams)

            home_teams = set()
            away_teams = set()

            for i in range(0, number_of_teams // 2):
                home_team = teams[i]
                away_team = teams[number_of_teams - i - 1]

                # Check city restrictions
                if any(
                    self.__check_team_restriction(home_team, ht) for ht in home_teams
                ):
                    home_team, away_team = away_team, home_team

                round_instance.add_home_team(home_team)
                round_instance.add_away_team(away_team)
                round_instance.create_match_pair(home_team, away_team)

                home_teams.add(home_team)
                away_teams.add(away_team)

            round_instance.generate_bipartite_graph_image(directory)

        # Generate the second half of the schedule as the inverse of the first half
        for round_index in range(half_rounds):
            round_instance = self.rounds[half_rounds + round_index + 1]
            first_half_round = self.rounds[round_index + 1]

            for home_team, away_team in first_half_round.matches.edges():
                round_instance.add_home_team(away_team)
                round_instance.add_away_team(home_team)
                round_instance.create_match_pair(away_team, home_team)

            round_instance.generate_bipartite_graph_image(directory)

    # Method to generate a graph coloring image of the restrictions
    def generate_graph_coloring_image(
        self, directory=".", filename="championship_restrictions_graph.png"
    ):
        # Generate a coloring for the graph
        coloring = nx.coloring.greedy_color(self.restrictions, strategy="largest_first")

        # Create a color map for the nodes
        colors = [coloring[node] for node in self.restrictions.nodes()]
        unique_colors = set(colors)

        # Draw the graph with a resolution of 1920x1080 and margins
        plt.figure(figsize=(19.2, 10.8))
        ax = plt.gca()
        ax.margins(0.1)  # Add margins around the graph
        pos = nx.spring_layout(self.restrictions, k=1)
        nx.draw(
            self.restrictions,
            pos,
            with_labels=True,
            node_color=colors,
            node_size=500,
            cmap=plt.cm.rainbow,
            font_size=10,
            font_color="black",
            ax=ax,
        )

        # Add legend
        legend_elements = [
            Patch(
                facecolor=plt.cm.rainbow(color / len(unique_colors)),
                edgecolor="k",
                label=f"Color {color}",
            )
            for color in unique_colors
        ]
        plt.legend(handles=legend_elements, loc="upper right")

        # Construct the full file path
        file_path = directory + "/" + filename if directory else filename

        # Save the image
        plt.savefig(file_path)
        plt.close()

    # Method to print all rounds and their matches in ascending order
    def print_all_rounds(self):
        # Sort rounds in ascending order
        sorted_rounds = sorted(self.rounds.items(), key=lambda x: x[0])

        # Print each round and the teams that will face each other
        for round_num, round_instance in sorted_rounds:
            print(f"Round {round_num}:")
            matches = list(
                round_instance.matches.edges()
            )  # Convert to list to index matches
            if not matches:
                print("No matches")
                continue

            for match_num, (home_team, away_team) in enumerate(matches, start=1):
                home_team_name = self.teams[home_team].name
                away_team_name = self.teams[away_team].name
                print(f"Match {match_num}: {home_team_name} vs {away_team_name}")

            print()
