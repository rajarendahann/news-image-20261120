import os
import shutil
import sys
from pathlib import Path

def main():
    # Use MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output
    output_dir_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_path).resolve()
    
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error: Could not create output directory {output_dir}: {e}", file=sys.stderr)
        sys.exit(1)
    
    source = Path("entry.png").resolve()
    if not source.exists():
        print(f"Error: Source file '{source}' not found.", file=sys.stderr)
        sys.exit(1)
        
    destination = output_dir / "entry.png"
    
    try:
        shutil.copy2(source, destination)
        print(f"Successfully copied source '{source}' to destination '{destination}'")
    except Exception as e:
        print(f"Error: Failed to copy file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
