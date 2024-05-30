import json
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database connection
engine = create_engine('sqlite:///super_tic_tac_toe.db', echo=True)
Base = declarative_base()

# Define the Player model
class Player(Base):
    __tablename__ = 'player'

    username = Column(String, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    games = relationship("GamePlayedBy", back_populates="player")

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    age = Column(Integer)

# Define the Game model
class Game(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    num_of_moves = Column(Integer)
    winner = Column(String)
    matrix = Column(String)

    players = relationship("GamePlayedBy", back_populates="game")

# Define the GamePlayedBy model to establish many-to-many relationship between players and games
class GamePlayedBy(Base):
    __tablename__ = 'game_played_by'

    game_id = Column(Integer, ForeignKey('game.game_id'), primary_key=True)
    player_username = Column(String, ForeignKey('player.username'), primary_key=True)

    game = relationship("Game", back_populates="players")
    player = relationship("Player", back_populates="games")

# Define the PlayerStats model
class PlayerStats(Base):
    __tablename__ = 'player_stats'

    username = Column(String, primary_key=True)
    num_of_games = Column(Integer)
    num_of_wins = Column(Integer)

# Create the tables
Base.metadata.create_all(engine)

# Function to add a new user
def add_user(username, age):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(username=username, age=age)
    session.add(user)
    session.commit()
    session.close()

# Function to fetch all users
def fetch_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

# Function to delete a player
def delete_player(old_username):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        player = session.query(User).filter_by(username=old_username).first()
        if player:
            session.delete(player)
            session.commit()
            print(f"Player {old_username} deleted successfully.")
        else:
            print(f"Player {old_username} does not exist.")
    except Exception as e:
        print("Error deleting player:", e)
    finally:
        session.close()

# Function to check if usernames exist
def check_usernames_exist(username1, username2):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        user1 = session.query(User).filter_by(username=username1).first()
        user2 = session.query(User).filter_by(username=username2).first()

        if user1 and user2:
            print(f"Both usernames '{username1}' and '{username2}' exist in the database.")
            return True
        elif user1:
            print(f"Username '{username1}' exists in the database, but '{username2}' does not.")
            return False
        elif user2:
            print(f"Username '{username2}' exists in the database, but '{username1}' does not.")
            return False
        else:
            print(f"Neither username '{username1}' nor '{username2}' exist in the database.")
            return False
    except Exception as e:
        print("Error checking usernames:", e)
        return False
    finally:
        session.close()

# Function to store game information
def store_game_info(game_info):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Extract relevant information from game_info
        game_id = game_info['game_id']
        player1 = game_info['player1']
        player2 = game_info['player2']
        winner = game_info['winner']
        matrix = game_info['matrix']
        num_of_moves = game_info['num_of_moves']

        # Update or insert player_stats for player1
        player1_stats = session.query(PlayerStats).filter_by(username=player1).first()
        if player1_stats:
            player1_stats.num_of_games += 1
            if winner == player1:
                player1_stats.num_of_wins += 1
        else:
            player1_stats = PlayerStats(username=player1, num_of_games=1, num_of_wins=1 if winner == player1 else 0)
            session.add(player1_stats)

        # Update or insert player_stats for player2
        player2_stats = session.query(PlayerStats).filter_by(username=player2).first()
        if player2_stats:
            player2_stats.num_of_games += 1
            if winner == player2:
                player2_stats.num_of_wins += 1
        else:
            player2_stats = PlayerStats(username=player2, num_of_games=1, num_of_wins=1 if winner == player2 else 0)
            session.add(player2_stats)

        # Insert game information into the game table
        game = Game(game_id=game_id, num_of_moves=num_of_moves, winner=winner, matrix=json.dumps(matrix))
        session.add(game)

        # Insert game information into the game_played_by table
        game_played_by1 = GamePlayedBy(game_id=game_id, player_username=player1)
        game_played_by2 = GamePlayedBy(game_id=game_id, player_username=player2)
        session.add_all([game_played_by1, game_played_by2])

        session.commit()
        print("Game information stored successfully.")
    except Exception as e:
        print("Error storing game information:", e)
    finally:
        session.close()

# Function to load a game
def load_game(game_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        game = session.query(Game).filter_by(game_id=game_id).first()
        if game:
            matrix = json.loads(game.matrix)
            player1 = game.players[0].player_username
            player2 = game.players[1].player_username
            num_of_moves = game.num_of_moves
            winner = game.winner
            return {'game_id': game_id, 'matrix': matrix, 'player1': player1, 'player2': player2,
                    'num_of_moves': num_of_moves, 'winner': winner}
        else:
            print(f"Game with ID {game_id} not found.")
            return None
    except Exception as e:
        print("Error loading game:", e)
        return None
    finally:
        session.close()

# Function to update game information
def update_game_info(game_id, new_board, num_of_moves, winner):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        game = session.query(Game).filter_by(game_id=game_id).first()
        if game:
            game.matrix = json.dumps(new_board)
            game.num_of_moves = num_of_moves
            game.winner = winner
            session.commit()
            print("Game information updated successfully.")
        else:
            print(f"Game with ID {game_id} not found.")
    except Exception as e:
        print("Error updating game information:", e)
    finally:
        session.close()
