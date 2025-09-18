import { useState } from "react";
import { Button } from "@/components/ui/button";

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [game, setGame] = useState(null);

  async function startGame() {
    const res = await fetch(`${API_URL}/start`, { method: "POST" });
    setGame(await res.json());
  }

  async function hit() {
    const res = await fetch(`${API_URL}/hit`, { method: "POST" });
    setGame(await res.json());
  }

  async function stand() {
    const res = await fetch(`${API_URL}/stand`, { method: "POST" });
    setGame(await res.json());
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-green-900 text-white">
      <h1 className="text-3xl font-bold mb-4">Blackjack</h1>

      {!game && (
        <Button onClick={startGame}>Deal</Button>
      )}

      {game && (
        <>
          <p className="mb-2">Chips: {game.chips}</p>

          <div className="mb-4">
            <p>Dealer: {game.dealer.map(c => `${c.rank}${c.suit}`).join(" ")}</p>
            <p>Player: {game.player.map(c => `${c.rank}${c.suit}`).join(" ")}</p>
          </div>

          <div className="flex gap-2 mb-4">
            <Button onClick={startGame}>Deal</Button>
            <Button onClick={hit}>Hit</Button>
            <Button onClick={stand}>Stand</Button>
            <Button disabled>Double (placeholder)</Button>
            <Button disabled>Split (placeholder)</Button>
            <Button disabled>Insurance (placeholder)</Button>
          </div>

          {game.message && <p className="text-xl">{game.message}</p>}
        </>
      )}
    </div>
  );
}
