from latex_components_generator.latex_components_generator import generate_latex_table


def main():
    sample_data = [
        ["Имя", "Фамилия", "Отчество", "Возраст"],
        ["Михаил", "Иванов", "Сергеевич", "52"],
        ["Петр", "Смирнов", "Евгеньевич", "42"],
        ["Лев", "Львов", "Львович", "27"]
    ]

    latex_document = [
        "\\documentclass{article}",
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage[english,russian]{babel}",
        "\\begin{document}",
        generate_latex_table(sample_data),
        "\\end{document}"
    ]
    with open("../artifacts/task_1.tex", "w") as f:
        f.write("\n".join(latex_document))


if __name__ == "__main__":
    main()
