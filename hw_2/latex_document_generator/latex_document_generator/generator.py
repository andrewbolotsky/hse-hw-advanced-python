from latex_components_generator.image_latex_generator import generate_latex_image
from latex_components_generator.table_latex_generator import generate_latex_table


def generate_latex_document(
        tables: list[list[list]] = None,
        images: list[tuple[str, int, int]] = None,
        output_file: str = "generated_document.tex"
) -> None:
    latex_document = [
        "\\documentclass{article}",
        "\\usepackage{graphicx}",
        "\\usepackage{booktabs}",
        "\\usepackage{array}"
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage[english,russian]{babel}",
        "\\begin{document}",
    ]

    if tables:
        for table_data in tables:
            latex_document.append(generate_latex_table(table_data))
            latex_document.append("")
    if images:
        for filepath, width, height in images:
            latex_document.append(generate_latex_image(filepath, width, height))
            latex_document.append("")
    latex_document.extend([
        "\\end{document}"
    ])
    with open(output_file, "w") as f:
        f.write("\n".join(latex_document))


def main():
    sample_tables = [
        [
            ["Имя", "Фамилия", "Отчество", "Возраст"],
            ["Михаил", "Иванов", "Сергеевич", "52"],
            ["Петр", "Смирнов", "Евгеньевич", "42"],
            ["Лев", "Львов", "Львович", "27"]
        ]
    ]

    sample_images = [
        ("../image/photo.png", 200, 150),
    ]

    generate_latex_document(
        tables=sample_tables,
        images=sample_images,
        output_file="../results/document.tex"
    )
