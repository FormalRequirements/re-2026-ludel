# Sports Equipment E-Store – Requirements Project

## Project Context

The growing demand for fast and accessible online services, combined with the continuous evolution of digital technologies, has strongly contributed to the expansion of e-commerce platforms. This rapid growth has intensified competition, both in terms of technological innovation and commercial offerings.

Despite this evolution, many existing e-stores still present significant shortcomings, particularly with regard to **system reliability, usability, ergonomics, and overall user experience**.

This project addresses these challenges by focusing on the **requirements engineering phase** of an online e-store dedicated to the sale of sports equipment. Its objective is to define, analyze, and structure a complete and coherent set of requirements necessary for the design of an efficient, secure, and reliable system.

---

## Project Objectives

The main objectives of this project are:

- To identify and formalize the functional, non-functional, and organizational requirements of a sports equipment e-store
- To structure these requirements using a rigorous and traceable methodology
- To automate the generation of a final requirements document in **PDF** and **HTML** formats
- To ensure a reproducible and auditable documentation workflow

---

## Requirements Methodology

The requirements are structured according to the **PEGS methodology**, which separates concerns into four complementary books:

- **Environment Book** – context, actors, constraints, assumptions, and invariants
- **Goals Book** – objectives, benefits, limitations, and stakeholders
- **Project Book** – roles, planning, risks, and technical choices
- **System Book** – system architecture, components, interfaces, requirements, and acceptance criteria

This structure ensures clarity, traceability, and consistency across the entire specification.

---

## Repository Organization & Workflow

To ensure a clean and collaborative development process, the repository follows a **branch-based workflow**:

- **`main`**  
  Contains stable and validated versions of the project.

- **`feat2/branche-requirement`**  
  Dedicated to the writing and refinement of the requirements documents (Environment Book, Goals Book, Project Book, and System Book).

- **Documentation branch**  
  Used for updates and improvements to the `README.md` file and project documentation.

This workflow allows:

- clear separation of responsibilities
- better version control
- easier review and validation of changes

---

## Technologies & Tools

### Documentation & Requirements

- **Markdown (`.md`)**  
  Used as the source format to write and maintain requirements in a readable, version-controlled way.

- **PDF & HTML**  
  Final output formats generated automatically for submission and review.

### Conversion Tools

- **Pandoc**  
  Used to convert Markdown documents into structured PDF and HTML deliverables.

---

## Automation

### Continuous Integration

- **GitHub Actions (`ci.yml`)**  
  Used to automate:
  - the validation of the requirements structure
  - the generation of PDF and HTML documents from Markdown
  - the production of consistent and reproducible deliverables
  - the attachment of generated files to GitHub Actions artifacts and releases

The automation pipeline guarantees that all deliverables correspond exactly to the validated source requirements.

---

## AI Assistance

To support the quality and consistency of the work, **Large Language Models (LLMs)** were used as assistance tools:

- ChatGPT
- Gemini

These tools were used exclusively for:

- requirement clarification
- consistency checking
- assistance in script writing for validation tests
- methodological guidance

All design decisions and final content remain under human control.

---

## Access to Deliverables via GitHub Actions

The project provides the following deliverables:

- A structured requirements document
- A **PDF version** generated automatically via the CI pipeline
- An **HTML version** for online consultation
- A reproducible and documented automation pipeline

### Availability of Generated Files

All generated deliverables (PDF and HTML) are **automatically produced by the Continuous Integration (CI) pipeline** at each commit on the `main` branch and on tagged releases.

These files are **not committed directly to the repository**.  
Instead, they are published as **GitHub Actions artifacts**, ensuring traceability, reproducibility, and repository cleanliness.

### How to Retrieve the Files

1. Go to the **Actions** tab of the GitHub repository.
2. Open the **most recent workflow run** corresponding to the latest commit.
3. Scroll down to the **Artifacts** section.
4. Download the artifact named `requirements-docs`.
5. The artifact is provided as a **ZIP file**.
6. Once extracted, the ZIP file contains:
   - the generated **PDF document**
   - the generated **HTML document**

---

## Expected Outcomes

By the end of this project, the repository provides:

- a clear and complete specification of the e-store requirements
- a professional and structured documentation workflow
- an automated and reproducible generation process
- deliverables easily accessible by instructors via GitHub Actions and GitHub Releases

---

## Authors

- **ABDEL-AZIZ ISSAKHA** — [GitHub](https://github.com/Abdel4353)
- **BELLA NGUEMA Luce** — [GitHub](https://github.com/Luce58)
