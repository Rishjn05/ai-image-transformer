"use client";

import { useState } from "react";

export default function Home() {
  const [imageUrl, setImageUrl] = useState("");
  const [strength, setStrength] = useState(0.7);
  const [images, setImages] = useState([]);

  const generate = async () => {
    const res = await fetch("http://localhost:8000/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image_url: imageUrl, strength })
    });

    const data = await res.json();
    setImages(data.images);
  };

  return (
    <div className="p-6">
      <input
        placeholder="Image URL"
        onChange={(e) => setImageUrl(e.target.value)}
        className="border p-2 w-full"
      />

      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        onChange={(e) => setStrength(Number(e.target.value))}
      />

      <button onClick={generate}>
        Generate
      </button>

      <div className="grid grid-cols-2 gap-4 mt-4">
        {images.map((img, i) => (
          <img key={i} src={img.image_url} />
        ))}
      </div>
    </div>
  );
}