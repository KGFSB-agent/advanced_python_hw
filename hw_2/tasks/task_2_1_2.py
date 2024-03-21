from task_2_1_1 import latex_table_generator

example = [["Title1", "Title2", "Title3"], [1, 2, 3], [4, 5, 6]]

table = latex_table_generator(example)

with open("hw_2/artifacts/artifact_task_2_1/latex_table.tex", "w") as file:
    file.write(table)