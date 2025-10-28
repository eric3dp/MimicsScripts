import trimatic as tm

sel = tm.get_selection()

visible_idxs = [i for i, p in enumerate(sel) if p.visible]
nxt = ((visible_idxs[-1] + 1) % len(sel)) if visible_idxs else 0

sel[nxt].visible = True
for i in visible_idxs:
    if i != nxt:
        sel[i].visible = False
