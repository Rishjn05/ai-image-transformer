// components/VariationGrid.tsx

export default function VariationGrid({ images }) {
  return (
    <div className="grid grid-cols-2 gap-4 mt-4">
      {images.map((img, i) => (
        <img
          key={i}
          src={img.image_url || img.url}
          className="rounded-lg"
        />
      ))}
    </div>
  );
}