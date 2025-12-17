import math
import trimatic

# === Constants ===
DENSITY = 0.0012  # g/mm³ — equivalent to 1.2 g/cm³ SOMETHING IS WRONG HERE
MAGNET_PULL = 75  # g — pull strength of 2×1 mm neodymium magnet (axial)
ORIENTATION_FACTOR = 1.0  # 1.0 = vertical (axial); 3–5 = horizontal/shear
SAFETY_FACTOR = 2.0  # Multiplier to ensure secure hold


# === Helper: recursively collect all parts from selection/group ===
def collect_parts(selection):
    parts = []
    for item in selection:
        if isinstance(item, trimatic.Part):
            parts.append(item)
        elif isinstance(item, trimatic.Group):
            parts.extend(collect_parts(item.items))
    return parts


# === Main Logic ===
selection = trimatic.get_selection()
parts = collect_parts(selection)

if not parts:
    print("⚠️ No parts selected.")
else:
    total_volume = sum(p.volume for p in parts)
    total_weight = total_volume * DENSITY
    required_force = total_weight * ORIENTATION_FACTOR * SAFETY_FACTOR
    magnets_needed = math.ceil(required_force / MAGNET_PULL)

    print(f"📦 Selected Parts: {len(parts)}")
    for p in parts:
        print(f"  - {p.name} ({p.volume:.2f} cm³)")

    print(f"\n🧮 Total Volume: {total_volume:.2f} cm³")
    print(f"⚖️ Estimated Weight: {total_weight:.2f} g")
    print(f"💪 Required Hold Force: {required_force:.2f} g")
    print(f"🧲 Magnets Needed: {magnets_needed}")
