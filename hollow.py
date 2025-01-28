import trimatic

selected = trimatic.get_selection()
originals = []
originals = trimatic.duplicate(selected)
solids = trimatic.find_group("Solid")
if not solids:
    trimatic.create_group("Solid", originals)
else:
    solids.add_items(originals)

trimatic.hollow(entities = selected, 
                hollow_type = trimatic.HollowType.Outside, 
                distance= 2)
