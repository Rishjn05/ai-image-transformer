export default function PromptBox({ setPrompt }) {
  return (
    <textarea
      placeholder="Enter prompt..."
      onChange={(e) => setPrompt(e.target.value)}
      className="w-full border p-2"
    />
  );
}