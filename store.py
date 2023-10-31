#from sentence_transformers import SentenceTransformer, util
import sys

from transformers import pipeline
from csv import writer
import ast
# link="https://www.livemint.com/news/world/gaza-hospital-bombing-israel-shares-footage-of-hamas-islamic-jihad-discussing-failed-rocket-launch-that-killed-500-11697621886093.html"
# Para='''Gaza hospital attack news: The Israeli Defense Forces (IDF) have released a footage which allegedly is a recording of ‘Palestinian Terrorists’ discussing the “failed rocket launch" that killed between 200 and 300 people. Health authorities in Hamas-ruled Gaza said the “failed rocket launch" killed 500 people and was caused by the latest in a wave of Israeli air strikes.  The Israeli military blamed militants in Palestine, saying an outgoing Islamic Jihad rocket misfired and that it would provide evidence.  The IDF took to micro-blogging site ‘X’ to share the voice note and said, “Islamic Jihad struck a Hospital in Gaza—the IDF did not. Listen to the terrorists as they realize this themselves".The IDF claimed that the voice note was of Hamas fighters discussing the ‘failed rocket launch’ that hit Al Ahli hospital, killing Gazans. The IDF's tweet attached transcription to the voice note.  The IDF's transcription reads:  Hamas Operative #2: I'm telling you this is the first time that we see a missile like this failing and so that's why we are saying it belongs to the Palestinian Islamic Jihad.  Hamas Operative #1: What?  Hamas Operative #2: They are saying it belongs to Palestinian Islamic Jihad  Hamas Operative #1: It's from us?  #2: It looks like it  #1: Who says this?  #2: They are saying that the shrapnel from the missile is local shrapnel and not like Israeli shrapnel  #1: What are you saying (name)?#2: But God bless, it couldn't have found another place to explode?  #1: Nevermind, (name), yes they shot it from the cemetery behind the hospital  #2: What?  #1: They shot it coming from the cemetery behind the Al-Ma'amadani Hospital, and it misfired and fell on them  #2: there is a cemetery behind it?  #1: Yes, Al-Ma'amadani is exactly in the compound  #2: Where is it when you enter the compound?  #1: You first enter the compound and don't go towards the city and it's on the right side of the Al-Ma'amadani Hospital.  Yes , I know it.  (Please note: The transcription of the voice note was done by IDF. Mint could not independently verify this transcription)  Doctors in Gaza City, faced with dwindling medical supplies, performed surgery on hospital floors, often without anesthesia, in a desperate bid to save badly wounded victims of a massive blast that killed civilians sheltering in a nearby hospital amid Israeli bombings and a blockade of the territory.  The Hamas militant group blamed the blast on an Israeli airstrike, while the Israeli military blamed a rocket misfired by other Palestinian militants. At least 500 people were killed, the Hamas-run Health Ministry said.  Rage at the hospital carnage spread through the West Asia as US President Joe Biden landed in Israel in hopes of stopping a spread of the war, which started after Hamas militants attacked towns and cities across southern Israel 7 October. Israeli strikes on Gaza continued on Wednesday, including attacks on cities in south Gaza that Israel had described as “safe zones" for Palestinian civilians.'''
inputs=ast.literal_eval(sys.argv[1])
# print(inputs)
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
# data = read_csv("datas.csv")
# links = data['Links'].tolist()
# more_details=data['Passages'].tolist()
# summarized_data=data['Summary'].tolist()
# print(summarized_data[0])

for i in range(1,len(links)):
    link=links[i]
    Para=inputs[link]
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarized=(summarizer(Para, max_length=130, min_length=40, do_sample=False))
    titles=['Links','Passages','Summary']
    list=[link,Para,summarized[0]["summary_text"]]
    # print(summarized)

    with open('datas.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list)
        f_object.close()

print("data saved")
