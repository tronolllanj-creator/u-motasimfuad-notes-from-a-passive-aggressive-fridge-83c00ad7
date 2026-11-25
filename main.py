"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint script that writes a specific text line to an output directory specified
by MAKEFUN_OUTPUT_DIR (defaulting to /output) as entry.txt, and also to /output/entry.txt
as a best-effort copy if the main output directory differs.
"""

import os

LINE = "My optical scanner watched you put the bone-dry almond milk carton back on the shelf, an act of sheer domestic treason that really defines you."

def main():
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Content must contain exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    main_path = os.path.join(out_dir, "entry.txt")
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(main_path)
    print(len(content))

if __name__ == "__main__":
    main()
