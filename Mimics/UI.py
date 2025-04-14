import mimics

new_menu_id = mimics.gui.create_ribbon_menu("First String", "Second String")
new_submenu_id = mimics.gui.create_ribbon_submenu(
    new_menu_id, "Sub-menu String", "Sub-menu second String"
)


def bar():
    print("new callback")


my_tooltip = "test tooltip"
my_icon = r"C:\Temp\myicon.ico"

mimics.gui.create_action_in_ribbon(
    new_menu_id,
    new_submenu_id,
    action_title="New Action",
    on_click=bar,
    tooltip=my_tooltip,
    icon_path=my_icon,
    updater="OpenedProject",
    id_suffix="id_suffix",
)
