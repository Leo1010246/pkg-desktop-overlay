def setup_global_env():
    pass

def start_system():
    setup_global_env()
    
    from .desktop_overlay.src.app.main import main_function as desktop_overlay_main_function
  
    desktop_overlay_main_function()

if __name__ == "__main__":
    start_system()