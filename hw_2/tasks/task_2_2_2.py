from LaTeX_PyPi import latex_image_generator, latex_table_generator, document
from pdflatex import PDFLaTeX
import os

table_example = [["Title1", "Title2", "Title3"], [1, 2, 3], [4, 5, 6]]
path_to_folder = "artifacts/arifacts_task_2_2/"
path_to_img = "artifacts/arifacts_task_2_2/Mr_Svin.png"

table = latex_table_generator(table_example)
image = latex_image_generator(path_to_folder, path_to_img)

end_doc = document(table, image)

with open("artifacts/arifacts_task_2_2/latex_table_and_image.tex", "w") as file:
    file.write(end_doc)

pdfl = PDFLaTeX.from_texfile(os.path.join("artifacts", "arifacts_task_2_2", "latex_table_and_image.tex"))
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)
