import flet as ft

def use_is_admin():
    is_admin, set_is_admin = ft.use_state(False)

    async def on_mount():
        set_is_admin(await ft.SharedPreferences().get("admin.role") == "admin")
    ft.on_mounted(on_mount)

    return is_admin
