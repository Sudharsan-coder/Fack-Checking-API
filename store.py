import sys
from transformers import pipeline
from csv import writer
import ast
inputs=ast.literal_eval(sys.argv[1])

links=list(inputs.keys())

link=links[0]
Para=inputs[link]
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarized=(summarizer(Para, max_length=130, min_length=40, do_sample=False))
titles=['Links','Passages','Summary']
list=[link,Para,summarized[0]["summary_text"]]

with open('datas.csv', 'w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(titles)
    writer_object.writerow(list)
    f_object.close()

for i in range(1,len(links)):
    link=links[i]
    Para=inputs[link]
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarized=(summarizer(Para, max_length=130, min_length=40, do_sample=False))
    titles=['Links','Passages','Summary']
    list=[link,Para,summarized[0]["summary_text"]]

    with open('datas.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list)
        f_object.close()

print("data saved")
