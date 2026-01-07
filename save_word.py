from docx import Document
from generate_cover_letter import generate_cover_letter

text = generate_cover_letter("""
Waymo is an autonomous driving technology company with the mission to be the world's most trusted driver.
2026 Summer Intern, MS/PhD, Compute, Compiler
Mountain View, California, United States
Intern
Hardware Engineering

You will:
- Design and implement compiler passes for custom silicon
- Design and implement efficient firmware libraries for memory management
- Measure and analyze performance on either simulator or silicon
- Integrate the solution into production grade memory allocator for custom silicon

You have:
- C/C++ programming skills
- Knowledge of compiler principles 
- Knowledge of modern computer architecture
- Performance analysis and optimization skills

We prefer:
- Experience with compilers for neural networks
- Knowledge of deep neural network
- Experience with RISC-V vector extension
""")

# Create the document
doc = Document()
doc.add_paragraph(text)

# Save to a local file (same folder as script)
file_path = "output3.docx"
doc.save(file_path)

print(f"Word file saved as: {file_path}")
