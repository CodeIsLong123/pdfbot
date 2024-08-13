
from ultralytics import YOLO
import pypdfium2 as pdfium
from pdf2image import convert_from_path

## Ich will einen Bot, der die Kernaussagen eines Textes herausfiltert. Diese Kernaussagen sollen dann in fragen umgewandelt werden, die ich mir selbst beantworten kann.
## Der bot soll mir auch antworten auf die Fragen geben, die ich mir dann anschauen kann nachdem ich mir die angeguckt habe. 
## Der Bot soll mir auch die Zusammenfassung des Textes geben.  --> Das ist die Kernaussage des Textes.
## Der Bot soll mir auch die wichtigsten Begriffe des Textes geben und diese abfragen.


#########################################################################
# Ich möchte erst versuchen die Texte mit der Hilfe YOLO zu analysieren.#
#########################################################################




def pdf_to_image(filename, output_path):
    images = convert_from_path(filename)
    for i in range(len(images)):
        images[i].save(f"{output_path}/{filename.split('/')[-1].replace('.pdf', '')}_{i}.png", 'PNG')
        





def ocr_on_image(image_path):
    pass



if __name__ == '__main__':
    import os
    ## folder with pdfs
    folder = "Data"
    
    ## get all pdfs in folder
    pdfs = [f for f in os.listdir(folder) if f.endswith(".pdf")]

    clean_pdfs = [f.strip(" ") for f in pdfs ]
    
    for pdf in clean_pdfs:
        pdf_to_image(f"{folder}/{pdf}", "images")
        