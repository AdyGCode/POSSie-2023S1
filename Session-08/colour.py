from rich.console import Console
console = Console()
def square_text(letter=" "):
    console.print("   ", style="white on green")
    console.print(f" {letter} ", style="white on green")
    console.print("   ", style="white on green")

square_text("B")

print("\x1b[31mHello\x1b[m world")