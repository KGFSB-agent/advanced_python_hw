from task_2_1_1 import latex_image_generator

path_to_folder = "hw_2/artifacts/arifacts_task_2_2/"
path_to_img = "hw_2/artifacts/arifacts_task_2_2/Mr_Svin.png"

image = latex_image_generator(path_to_folder, path_to_img)

with open("hw_2/artifacts/arifacts_task_2_2/latex_image.tex", "w") as file:
    file.write(image)
