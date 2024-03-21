def latex_table_generator(data):
    n_columns = len(data[0])
    table = "\documentclass[12pt, letterpaper]{article}\n" + "\\begin{document}\n" + "\\begin{tabular}{|" + "|".join(["c"] * n_columns) + "|}\n" + "\hline\n"

    for row in data:
        table += "& ".join(str(cell) for cell in row) + "\\\\\n"
        table += "\hline\n"
    
    table += "\end{tabular}\n" + "\end{document}"

    return table

def latex_image_generator(path_to_folder_with_img, selected_img_in_folder):
    preamble = "\\documentclass{article}\n" + "\\usepackage{graphicx}\n" + "\\graphicspath{" + "{" + path_to_folder_with_img + "}" + "}\n"
    body = preamble + "\\begin{document}\n" + "\\includegraphics" + "{" + selected_img_in_folder + "}\n" + "\\end{document}"
    
    return body

def document(first_latex, second_latex):
    text_first_latex = first_latex.split("\n")
    text_second_latex = second_latex.split("\n")

    if any('&' in line for line in text_first_latex) == True: # the first latex has a table
        del text_first_latex[-1]
        del text_second_latex[0]
        first_preamble = text_second_latex.pop(0)
        second_preamble = text_second_latex.pop(0)
        del text_second_latex[-3]
        # text_second_latex.remove("\begin{document}")

        text_first_latex.insert(1, first_preamble)
        text_first_latex.insert(2, second_preamble)

        correct_latex = '\n'.join(text_first_latex + text_second_latex)

        return correct_latex
    
    else: # the first latex has an image
        del text_first_latex[-1]
        del text_second_latex[0]
        del text_second_latex[1]

        correct_latex = '\n'.join(text_first_latex + text_second_latex)

        return correct_latex



