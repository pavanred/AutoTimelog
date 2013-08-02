from gi.repository import Gtk, Wnck

def main():

    screen = Wnck.Screen.get_default()
    screen.force_update()  # recommended per Wnck documentation
    
    window_list = screen.get_windows()
    
    for item in window_list:
        print item.get_name()
        
    
    active_window = screen.get_active_window()
    print active_window.get_name()

if __name__ == "__main__":
    main()
    Gtk.main()