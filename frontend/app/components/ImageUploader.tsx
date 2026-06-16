export default function ImageUploader({ setImageUrl }) {
  return (
    <input
      placeholder="Image URL"
      onChange={(e) => setImageUrl(e.target.value)}
      className="w-full border p-2"
    />
  );
}