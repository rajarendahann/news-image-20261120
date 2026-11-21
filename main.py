import os
import shutil
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    source = "entry.png"
    if not os.path.exists(source):
        print(f"Error: {source} not found.")
        sys.exit(1)
        
    destination = os.path.join(output_dir, "entry.png")
    shutil.copy2(source, destination)
    
    print(destination)

if __name__ == "__main__":
    main()
