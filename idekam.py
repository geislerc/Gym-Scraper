from pathlib import Path
file = Path("new/")
file.parent.mkdir(parents=True, exist_ok=True)
#file.write_text("toto")