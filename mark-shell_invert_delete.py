import trimatic


selected = trimatic.get_selection()
for x in selected:
    if isinstance(x, trimatic.Group):
        for y in x.items:
            trimatic.filter_small_shells(y)
    else:
        trimatic.filter_small_shells(x)
            
            # y.activate_mark_shell()
            # trimatic.get_marked_triangles()
            # trimatic.show_only()
            # if trimatic.message_box("Delete?"):
            #     y.delete()

                