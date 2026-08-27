import pathlib
import sys

# Agar `import main` di tests/ menemukan src/main.py
sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))
