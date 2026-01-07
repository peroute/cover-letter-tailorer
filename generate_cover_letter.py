import ollama

# Your cover letter template (with placeholders)
COVER_LETTER_TEMPLATE = """Dear Hiring Manager, 
I am a Computer Science undergraduate at Texas Tech University with a deep-seated 
interest in building scalable, reliable software systems. My approach to engineering is 
driven by a "learning by building" philosophy, I am less interested in just writing code that 
works and more interested in understanding the underlying architecture that makes 
software production-ready. 
Recently, I have focused on evolving my Macy’s Price Tracker project from a monolithic 
script into a microservices-oriented architecture. By integrating Docker and CI/CD 
workflows, I’ve gained hands-on experience with container orchestration and the 
challenges of deploying scalable applications. This transition has been instrumental in 
developing my technical judgment regarding modern, industry-standard engineering 
practices. 
My background also includes applying computer vision to physical systems. I previously 
developed a follow-line robot using Python and image processing on Raspberry Pi, and 
built a mobile application that uses CV to recommend recipes based on detected 
ingredients. These projects required me to bridge the gap between theoretical algorithms 
and real-world hardware constraints, sharpening my debugging and problem-solving skills. 
I am particularly drawn to the [Position Title] at [Company Name] because of your work in 
[mention one specific thing: e.g., cloud infrastructure / consumer-facing UX / FinTech 
security]. I am eager to apply my background in full-stack development and 
containerization to help [Company Name] build impactful solutions. 
Thank you for your time and consideration. I look forward to the possibility of discussing 
how my curiosity and project experience can contribute to your engineering team. 
Sincerely, 
Hedi Bouassida
"""

def generate_cover_letter(job_description: str, model: str = "llama3") -> str:
    """
    Given a raw job description, ask the model to:
    - infer Position Title
    - infer Company Name
    - infer one specific thing they work on
    and fill in the brackets in the template.
    """
    system_prompt = (
        "You are a professional writing assistant. "
        "Your job is to fill in the bracketed placeholders in the given cover letter template "
        "using the job description.\n\n"
        "Rules:\n"
        "- Replace [Position Title] with the exact position title from the job description.\n"
        "- Replace [Company Name] with the company name from the job description.\n"
        "- Replace [mention one specific thing: e.g., cloud infrastructure / consumer-facing UX / FinTech security]\n"
        "  with ONE specific area of work mentioned in the job description that fits the role.\n"
        "- Do NOT change any other wording in the template.\n"
        "- Do NOT add new paragraphs.\n"
        "- Do NOT add spaces between paragraphs"
        "- Output ONLY the completed cover letter text, nothing else.\n"
    )

    user_content = f"""
COVER LETTER TEMPLATE:
<<<TEMPLATE_START>>>
{COVER_LETTER_TEMPLATE}
<<<TEMPLATE_END>>>

JOB DESCRIPTION RAW TEXT:
<<<JD_START>>>
{job_description}
<<<JD_END>>>
"""

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    # Example: your Waymo job text (shortened for demo, you can paste the full thing)
    waymo_job_description = """
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
"""

    cover_letter = generate_cover_letter(waymo_job_description, model="llama3")
    print(cover_letter)
