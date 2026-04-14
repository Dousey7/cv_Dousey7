from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

WIDTH, HEIGHT = A4
PRIMARY = HexColor("#0077B6")
DARK = HexColor("#1B1B1B")
LIGHT_BG = HexColor("#F0F4F8")
ACCENT = HexColor("#00A2E8")
GRAY = HexColor("#555555")
LIGHT_GRAY = HexColor("#888888")

def draw_header(c, y):
    # Header background
    c.setFillColor(PRIMARY)
    c.rect(0, y - 5*mm, WIDTH, 55*mm, fill=True, stroke=False)

    # Name
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(20*mm, y + 30*mm, "SEYDOU NOUROU AW")

    # Title
    c.setFont("Helvetica", 14)
    c.drawString(20*mm, y + 20*mm, "Developpeur Web Full Stack")

    # Contact line
    c.setFont("Helvetica", 9)
    contact = "Dakar, Senegal  |  seydaw7@gmail.com  |  +221 77 112 76 10  |  github.com/Dousey7"
    c.drawString(20*mm, y + 8*mm, contact)

    c.setFont("Helvetica", 8)
    c.drawString(20*mm, y + 2*mm, "LinkedIn: sn.linkedin.com/in/seydou-nourou-aw-342168185")

    return y - 10*mm

def draw_section_title(c, y, title):
    y -= 8*mm
    # Accent bar
    c.setFillColor(PRIMARY)
    c.rect(20*mm, y + 1*mm, 4*mm, 5*mm, fill=True, stroke=False)

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(28*mm, y + 1.5*mm, title.upper())

    # Underline
    c.setStrokeColor(HexColor("#E0E0E0"))
    c.setLineWidth(0.5)
    c.line(20*mm, y, WIDTH - 20*mm, y)

    return y - 6*mm

def draw_skill_category(c, y, category, skills):
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, y, category + " :")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 9)

    # Calculate where skills text starts
    cat_width = c.stringWidth(category + " : ", "Helvetica-Bold", 9)
    x_start = 25*mm + cat_width
    max_width = WIDTH - 25*mm - x_start

    # Simple wrapping
    text = skills
    if c.stringWidth(text, "Helvetica", 9) + x_start > WIDTH - 20*mm:
        c.drawString(x_start, y, text[:70])
        y -= 4.5*mm
        c.drawString(25*mm, y, text[70:])
    else:
        c.drawString(x_start, y, text)

    return y - 5.5*mm

def draw_experience(c, y, period, company, role, tasks):
    if y < 40*mm:
        c.showPage()
        y = HEIGHT - 20*mm

    # Period
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(25*mm, y, period)

    # Company & Role
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm, y - 5*mm, company)

    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(25*mm, y - 10.5*mm, role)

    y -= 16*mm

    # Tasks
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8.5)
    for task in tasks:
        if y < 25*mm:
            c.showPage()
            y = HEIGHT - 20*mm
        # Bullet
        c.setFillColor(PRIMARY)
        c.circle(27*mm, y + 1.2*mm, 1*mm, fill=True, stroke=False)
        c.setFillColor(GRAY)
        c.drawString(30*mm, y, task)
        y -= 4.5*mm

    return y - 3*mm

def draw_education(c, y, period, school, diploma, detail=""):
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(25*mm, y, period)

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm, y - 5*mm, school)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 9)
    c.drawString(25*mm, y - 10.5*mm, diploma)

    if detail:
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(25*mm, y - 15.5*mm, detail)
        return y - 22*mm

    return y - 17*mm

def draw_project(c, y, name, stack, description):
    if y < 45*mm:
        c.showPage()
        y = HEIGHT - 20*mm

    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(25*mm, y, name)

    c.setFillColor(PRIMARY)
    c.setFont("Helvetica", 8)
    c.drawString(25*mm, y - 5*mm, "Stack : " + stack)

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8.5)
    # Wrap description
    words = description.split()
    line = ""
    line_y = y - 10.5*mm
    for word in words:
        test = line + " " + word if line else word
        if c.stringWidth(test, "Helvetica", 8.5) > WIDTH - 50*mm:
            c.drawString(25*mm, line_y, line)
            line_y -= 4*mm
            line = word
        else:
            line = test
    if line:
        c.drawString(25*mm, line_y, line)
        line_y -= 4*mm

    return line_y - 3*mm

def draw_tags(c, y, items):
    x = 25*mm
    for item in items:
        tag_width = c.stringWidth(item, "Helvetica", 8) + 8*mm

        if x + tag_width > WIDTH - 20*mm:
            x = 25*mm
            y -= 7*mm

        # Tag background
        c.setFillColor(LIGHT_BG)
        c.roundRect(x, y - 1*mm, tag_width, 6*mm, 2*mm, fill=True, stroke=False)

        c.setFillColor(DARK)
        c.setFont("Helvetica", 8)
        c.drawString(x + 4*mm, y + 0.5*mm, item)

        x += tag_width + 3*mm

    return y - 10*mm

def generate_cv():
    c = canvas.Canvas("docs/mon_CV_pro.pdf", pagesize=A4)
    c.setTitle("CV - Seydou Nourou Aw")
    c.setAuthor("Seydou Nourou Aw")

    y = HEIGHT - 55*mm

    # === HEADER ===
    y = draw_header(c, y)

    # === COMPETENCES ===
    y = draw_section_title(c, y, "Competences Techniques")

    y = draw_skill_category(c, y, "Frontend",
        "React.js, JavaScript ES6+, HTML5, CSS3, Bootstrap, Chart.js, Responsive Design")
    y = draw_skill_category(c, y, "Backend",
        "PHP, Symfony, Next.js, API REST, JWT Authentication, EasyAdmin")
    y = draw_skill_category(c, y, "Bases & Outils",
        "PostgreSQL, MySQL, Git, GitHub, Docker, VS Code, Postman")
    y = draw_skill_category(c, y, "Autres",
        "Flutter, Dart, TypeScript, Laravel/Blade")

    # === EXPERIENCE ===
    y = draw_section_title(c, y, "Experience Professionnelle")

    y = draw_experience(c, y,
        "Novembre 2023 - Present",
        "Universite Amadou Mahtar Mbow",
        "Developpeur Web Full Stack",
        [
            "Developpement application gestion bulletins de salaire (Symfony, MySQL)",
            "Creation interfaces d'administration avec EasyAdmin",
            "Mise en place d'API REST securisees (JWT)",
            "Deploiement avec Docker"
        ])

    y = draw_experience(c, y,
        "Decembre 2022 - Juillet 2023",
        "Foundever (Sitel Group)",
        "Technicien Support Informatique",
        [
            "Support client Orange (1413)",
            "Resolution incidents reseau et services",
            "Accompagnement utilisateurs"
        ])

    y = draw_experience(c, y,
        "Juin 2022 - Octobre 2022",
        "Demarch",
        "Stage Developpement Web",
        [
            "Application de gestion de projets avec React & Node.js",
            "Application de gestion des associations de jeunes",
            "Application Python de gestion de donnees utilisateurs",
            "Administration base de donnees et archivage projets"
        ])

    y = draw_experience(c, y,
        "Fevrier 2022 - Juin 2022",
        "Wave Senegal",
        "Agent Commercial",
        [
            "Distribution terrain et promotion services Wave",
            "Ouverture comptes clients",
            "Support et assistance utilisateurs"
        ])

    # === FORMATION ===
    y = draw_section_title(c, y, "Formation")

    y = draw_education(c, y,
        "2019 - 2022",
        "Sup de Co",
        "Diplome d'ingenieur Informatique",
        "Genie Logiciel & Reseaux")

    y = draw_education(c, y,
        "2018 - 2019",
        "Groupe Scolaire le Baobab",
        "Baccalaureat Litteraire",
        "Mention Assez Bien")

    # === PROJETS ===
    y = draw_section_title(c, y, "Projets")

    y = draw_project(c, y,
        "Application RH - Gestion des bulletins de salaire",
        "Symfony, MySQL, EasyAdmin, Chart.js",
        "Upload ZIP, notifications email + SMS, dashboard statistique, export PDF/Excel, authentification securisee, gestion des roles.")

    y = draw_project(c, y,
        "Plateforme Location / Vente de Vehicules",
        "Next.js, React, PostgreSQL, JWT",
        "Systeme premium, annonces dynamiques, interface responsive, JWT authentication.")

    # === SOFT SKILLS ===
    y = draw_section_title(c, y, "Soft Skills")
    y = draw_tags(c, y, [
        "Analyse & resolution de problemes",
        "Rigueur et organisation",
        "Sens de l'ecoute",
        "Adaptabilite",
        "Perseverance"
    ])

    # === LANGUES ===
    y = draw_section_title(c, y, "Langues")

    langs = [("Francais", "Courant"), ("Anglais", "Professionnel"), ("Wolof", "Langue maternelle")]
    for lang, level in langs:
        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(25*mm, y, lang)
        c.setFillColor(LIGHT_GRAY)
        c.setFont("Helvetica", 9)
        c.drawString(55*mm, y, level)
        y -= 5.5*mm

    c.save()
    print("CV genere avec succes : docs/mon_CV_pro.pdf")

if __name__ == "__main__":
    generate_cv()
