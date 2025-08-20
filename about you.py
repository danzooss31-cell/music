import time
import sys
import os

def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.03):
    """Animasi teks dengan efek ketik"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flash_effect(text, flashes=3, delay=0.2):
    """Efek berkedip pada teks"""
    for _ in range(flashes):
        print(f"\r\033[93m{text}\033[0m", end="")  # Kuning
        time.sleep(delay)
        print("\r" + " " * len(text), end="")
        time.sleep(delay)
    print(f"\r{text}")

def loading_animation(duration=2):
    """Animasi loading"""
    print(f"\nLoading...")
    for i in range(int(duration * 10)):
        symbols = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        print(f"\r{symbols[i % len(symbols)]} {i*10}%", end="")
        time.sleep(0.1)
    print(f"\r✓ Ready!{' ' * 20}")

def print_banner():
    """Banner keren"""
    banner = r"""
    ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ██████╗ ██████╗ ██████╗ 
    ████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██╔══██╗██╔══██╗██╔══██╗
    ██╔████╔██║██║   ██║███████╗██║██║         ██████╔╝██████╔╝██████╔╝
    ██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔═══╝ ██╔══██╗██╔══██╗
    ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ██║     ██║  ██║██████╔╝
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝     ╚═╝  ╚═╝╚═════╝ 
    """
    print(banner)

def sing_song():
    """Menampilkan lirik lagu dengan efek-efek keren"""
    clear_screen()
    
    # Header dengan efek
    print("="*60)
    print_banner()
    print("="*60)
    
    loading_animation(1)
    
    print("\n🎤 Lagu Dimulai...\n")
    
    # Lirik dengan berbagai efek
    time.sleep(1)
    animate_text("🎵 Do you think I have forgotten?", 0.04)
    
    time.sleep(1.2)
    animate_text("🎵 Do you think I have forgotten?", 0.04)
    
    time.sleep(1)
    animate_text("🎵 Do you think I have forgotten", 0.04)
    
    time.sleep(0.8)
    flash_effect("🎵 about you?")
    
    time.sleep(1.5)
    animate_text("🎵 There was something bout you that now I cant remember", 0.03)
    
    time.sleep(1.8)
    animate_text("🎵 Its the same damn thing that made my heart surrender", 0.03)
    
    time.sleep(1.8)
    animate_text("🎵 And I miss you on a train, I miss you in the morning", 0.03)
    
    time.sleep(1.8)
    animate_text("🎵 I never know what to think about", 0.03)
    
    time.sleep(2)
    # Efek khusus untuk lirik terakhir
    print("\033[91m", end="")  # Warna merah
    animate_text("🎵 I think about you" + "u"*15 + "!", 0.01)
    print("\033[0m", end="")  # Reset warna
    
    # Efek akhir yang dramatis
    print("\n" + "💥" * 30)
    flash_effect("✨ SONG FINISHED ✨", 3, 0.3)
    print("💥" * 30)
    
    # Footer
    print(f"\n🎧 Thank you for listening!")
    print("="*60)

def main():
    """Program utama"""
    try:
        while True:
            sing_song()
            
            # Tanya user apakah ingin mengulang
            print(f"\nWant to hear it again? (y/n): ", end="")
            choice = input().lower()
            if choice != 'y':
                print("👋 Goodbye!")
                break
            clear_screen()
                
    except KeyboardInterrupt:
        print(f"\n⏹️ Music stopped by user")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()