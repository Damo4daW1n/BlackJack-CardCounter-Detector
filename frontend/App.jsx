import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
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

      {!game && <button onClick={startGame}>Deal</button>}

      {game && (
        <>
          <p className="mb-2">Chips: {game.chips}</p>

          <div className="mb-4">
            <p>Dealer: {game.dealer.map(c => `${c.rank}${c.suit}`).join(" ")}</p>
            <p>Player: {game.player.map(c => `${c.rank}${c.suit}`).join(" ")}</p>
          </div>

          <div className="flex gap-2 mb-4">
            <button onClick={startGame}>Deal</button>
            <button onClick={hit}>Hit</button>
            <button onClick={stand}>Stand</button>
            <button disabled>Double (placeholder)</button>
            <button disabled>Split (placeholder)</button>
            <button disabled>Insurance (placeholder)</button>
          </div>

          {game.message && <p className="text-xl">{game.message}</p>}
        </>
      )}
    </div>
  );
}

export default App;
