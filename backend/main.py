from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

suits = ["♠", "♥", "♦", "♣"]
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def get_card_value(card):
    rank = card["rank"]
    if rank in ["J", "Q", "K"]:
        return 10
    if rank == "A":
        return 11
    return int(rank)

def calculate_value(hand):
    total = sum(get_card_value(c) for c in hand)
    aces = sum(1 for c in hand if c["rank"] == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def generate_deck(num_decks=6):
    deck = [{"rank": r, "suit": s} for r in ranks for s in suits] * num_decks
    random.shuffle(deck)
    return deck

# Store game state (in-memory for now, later can use DB/session)
games = {}

@app.post("/start")
def start_game(game_id: str = "default", bet: int = 10):
    deck = generate_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    games[game_id] = {
        "deck": deck,
        "player": player,
        "dealer": dealer,
        "bet": bet,
        "chips": 1000,
        "message": ""
    }

    return games[game_id]

@app.post("/hit")
def hit(game_id: str = "default"):
    game = games[game_id]
    game["player"].append(game["deck"].pop())
    if calculate_value(game["player"]) > 21:
        game["message"] = "You bust!"
        game["chips"] -= game["bet"]
    return game

@app.post("/stand")
def stand(game_id: str = "default"):
    game = games[game_id]
    while calculate_value(game["dealer"]) < 17:
        game["dealer"].append(game["deck"].pop())

    p_val = calculate_value(game["player"])
    d_val = calculate_value(game["dealer"])

    if d_val > 21 or p_val > d_val:
        game["chips"] += game["bet"]
        game["message"] = "You win!"
    elif p_val < d_val:
        game["chips"] -= game["bet"]
        game["message"] = "You lose!"
    else:
        game["message"] = "Push!"

    return game
