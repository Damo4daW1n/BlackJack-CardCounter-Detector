import { useState } from "react";
import { Button } from "@/components/ui/button";

function getCardValue(card) {
  if (["J", "Q", "K"].includes(card.rank)) return 10;
  if (card.rank === "A") return 11;
  return Number(card.rank);
}

function calculateValue(hand) {
  let total = hand.reduce((sum, card) => sum + getCardValue(card), 0);
  let aces = hand.filter(c => c.rank === "A").length;
  while (total > 21 && aces > 0) {
    total -= 10;
    aces -= 1;
  }
  return total;
}

export default function App() {
  const [deck, setDeck] = useState(generateDeck(6));
  const [playerHand, setPlayerHand] = useState([]);
  const [dealerHand, setDealerHand] = useState([]);
  const [chips, setChips] = useState(1000);
  const [bet, setBet] = useState(1);
  const [message, setMessage] = useState("");

  function generateDeck(numDecks) {
    const suits = ["♠", "♥", "♦", "♣"];
    const ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"];
    let cards = [];
    for (let d=0; d<numDecks; d++) {
      for (let suit of suits) {
        for (let rank of ranks) {
          cards.push({ rank, suit });
        }
      }
    }
    return shuffle(cards);
  }

  function shuffle(array) {
    let a = [...array];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function dealCard(handSetter) {
    setDeck(prev => {
      const card = prev[0];
      handSetter(h => [...h, card]);
      return prev.slice(1);
    });
  }

  function startRound() {
    setPlayerHand([]);
    setDealerHand([]);
    setMessage("");
    dealCard(setPlayerHand);
    dealCard(setDealerHand);
    dealCard(setPlayerHand);
    dealCard(setDealerHand);
  }

  function hit() {
    dealCard(setPlayerHand);
    if (calculateValue([...playerHand, deck[0]]) > 21) {
      setMessage("You bust!");
      settle("lose");
    }
  }

  function stand() {
    // Dealer plays
    let dealer = [...dealerHand];
    while (calculateValue(dealer) < 17) {
      dealer.push(deck[dealer.length]); // naive draw
    }
    setDealerHand(dealer);

    const pVal = calculateValue(playerHand);
    const dVal = calculateValue(dealer);

    if (dVal > 21 || pVal > dVal) settle("win");
    else if (pVal < dVal) settle("lose");
    else settle("push");
  }

  function settle(outcome) {
    if (outcome === "win") {
      setChips(c => c + bet);
      setMessage("You win!");
    } else if (outcome === "lose") {
      setChips(c => c - bet);
      setMessage("You lose!");
    } else {
      setMessage("Push!");
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-green-900 text-white">
      <h1 className="text-3xl font-bold mb-4">Blackjack</h1>

      <p className="mb-2">Chips: {chips}</p>

      <div className="mb-4">
        <p>Dealer Hand: {dealerHand.map(c => `${c.rank}${c.suit}`).join(" ")} ({calculateValue(dealerHand)})</p>
        <p>Your Hand: {playerHand.map(c => `${c.rank}${c.suit}`).join(" ")} ({calculateValue(playerHand)})</p>
      </div>

      <div className="flex gap-2 mb-4">
        <Button onClick={startRound}>Deal</Button>
        <Button onClick={hit}>Hit</Button>
        <Button onClick={stand}>Stand</Button>
        <Button disabled>Double (placeholder)</Button>
        <Button disabled>Split (placeholder)</Button>
        <Button disabled>Insurance (placeholder)</Button>
      </div>

      {message && <p className="text-xl">{message}</p>}
    </div>
  );
}
