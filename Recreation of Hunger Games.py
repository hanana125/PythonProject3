#Hunger Games recreation because why not (I'll fix)

import random

# Function to create a player
def create_player():
    name = input("Enter player name: ")
    district = input("Enter district (1-12): ")
    strength = int(input("Enter Strength (1-10): "))
    agility = int(input("Enter Agility (1-10): "))
    intelligence = int(input("Enter Intelligence (1-10): "))

    # Stats dictionary for the player
    player = {
        'name': name,
        'district': district,
        'strength': strength,
        'agility': agility,
        'intelligence': intelligence
    }
    return player

# Death messages
death_messages = [
    "was struck down by an unknown force.",
    "fell to the ground, lifeless.",
    "was consumed by the arena's deadly traps.",
    "was eliminated in a dramatic battle.",
    "succumbed to the hunger and exhaustion."
]

# Function to simulate a battle between two players
def battle(player1, player2):
    stats = ['strength', 'agility', 'intelligence']
    player1_score = 0
    player2_score = 0

    for stat in stats:
        if player1[stat] > player2[stat]:
            player1_score += 1
        elif player1[stat] < player2[stat]:
            player2_score += 1

    # Determine winner and loser
    if player1_score > player2_score:
        winner = player1
        loser = player2
    elif player1_score < player2_score:
        winner = player2
        loser = player1
    else:
        # If it's a tie, randomly select a winner
        winner = random.choice([player1, player2])
        loser = player1 if winner == player2 else player2

    # Random death message
    death_message = random.choice(death_messages)
    print(f"{loser['name']} from district {loser['district']} {death_message}")

    return winner


# Main game loop
def game():
    num_players = int(input("Enter the number of players: "))
    players = []

    # Create players
    for _ in range(num_players):
        player = create_player()
        players.append(player)

    print("\nThe game begins...\n")

    # Simulate battles until one player remains
    while len(players) > 1:
        # Randomly select two players to battle
        player1, player2 = random.sample(players, 2)
        print(f"\nBattle between {player1['name']} and {player2['name']}...")
        winner = battle(player1, player2)
        players.remove(player1 if winner == player2 else player2)

    # The last remaining player is the winner
    winner = players[0]
    print(f"\n{winner['name']} from District {winner['district']} is the winner!")


# Start the game
if __name__ == "__main__":
    game()
