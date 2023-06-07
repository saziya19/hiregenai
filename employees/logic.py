import openai
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
from docx import Document
# import gradio as gr 
import re
from nltk.stem import WordNetLemmatizer

openai.api_key = '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'

# nltk.download('all')
def get_resume_names(folder_path):
    resume_names = [doc for doc in os.listdir(folder_path) if doc.endswith(('.txt', '.pdf', '.docx')) and not doc.startswith('~$')]
    return resume_names

def filtered_files(description):
   
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize in a short form and get the technologies:\n{description}\n",
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=10,
    )

    summary = response.choices[0].text.strip()
    lemmatizer = WordNetLemmatizer()

    lemmatized_words = [lemmatizer.lemmatize(word) for word in summary]
    print(lemmatized_words)
    print(summary)
    stop_words =stopwords.words("english")
    stop_words.extend(['.',",",":",")",",","software","(","want","person","knowledge","skills","percent","years","year","different","some", "experience","expertise","technology","technologies", "get", "must","resume","resumes","developer", "latest","engineer","exp","yrs",";","tech","experience"])
    folder_path = "C:/Users/sp13/OneDrive/Desktop/docs"
    
    
    matching_files = []
    matching_files1 = []
    matching_files2 = []
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith('.docx'):
            document = Document(os.path.join(folder_path, file))

            text = "\n".join([paragraph.text for paragraph in document.paragraphs])
            text = text.lower()

           
            pattern = r"(?i)(?:(\d+(?:\.\d+)?|\d+\+?)\s*(?:years|yrs|yr.|years of experience))|(?:\b(\w+)\s+years\s+of\s+experience\b)"
            
            matches = re.findall(pattern, text)
            
            numeric_matches = [match[0] for match in matches if match[0]]
            word_matches = [match[1] for match in matches if match[1]]
            
            totals = numeric_matches + word_matches

            print(totals)


            summary_pattern = r"(?i)(?:(\d+(?:\.\d+)?|\d+\+?)\s*(?:years|yrs|yr.|years of experience))|(?:\b(\w+)\s+years\s+of\s+experience\b)"

            matches = re.findall(summary_pattern, description)
            
            
            numeric_matches1 = [match[0] for match in matches if match[0]]
            word_matches1 = [match[1] for match in matches if match[1]]
            
            sum_totals = numeric_matches1 + word_matches1

            print(sum_totals)


            state = ""
            for sum_total in sum_totals:
                for total in totals:
                    if sum_total in total:
                        state = str("Experience {} years match " .format(total))
                        print(state)
                   

            tokens = word_tokenize(summary.lower())
            filtered_words = []
            for token in tokens:
                if token not in stop_words:
                    filtered_words.append(token)
            print(filtered_words)
            num_keywords = len(filtered_words)
            matching_keywords = []
            for word in filtered_words:
                if word in text:
                    matching_keywords.append(word)



            matching_keywords1 = len(matching_keywords)
            print(matching_keywords)
            matching_percentage = matching_keywords1 / num_keywords * 100
            print(matching_percentage)
            matching = []

            if matching_percentage>=1:

                if matching_percentage >= 75:
                    matching_files.append((file, matching_percentage,matching_keywords,state))
                elif matching_percentage>=50 and matching_percentage<75:
                    matching_files1.append((file, matching_percentage,matching_keywords,state))
                elif matching_percentage>=1 and matching_percentage<50:
                # else:
                    matching_files2.append((file, matching_percentage,matching_keywords,state)) 
                else:
                    print("No Files Found")

            else:
                print("No Files Found")
    
            sorted_files1 = sorted(matching_files, key=lambda x: x[1], reverse=True)
   
            sorted_files2 = sorted(matching_files1, key=lambda x: x[1], reverse=True)
   
            sorted_files3 = sorted(matching_files2, key=lambda x: x[1], reverse=True)
    
    filtered_files=[]
    folder_path = "C:/Users/sp13/OneDrive/Desktop/docs/"

    for file_info in sorted_files1:
        file_name = file_info[0]
        file_path = folder_path + file_name
        filtered_files.append(file_path)

    print("filtered_files with sorted_files1 start")
    print(filtered_files)
    print("filtered_files with sorted_files1 end")




    filtered_files1=[]
    folder_path = "C:/Users/sp13/OneDrive/Desktop/docs/"

    for file_info in sorted_files2:
        file_name = file_info[0]
        file_path = folder_path + file_name
        filtered_files1.append(file_path)

    print("filtered_files1 with sorted_files2 start")
    print(filtered_files1)
    print("filtered_files1 with sorted_files2 end")

    filtered_files2=[]
    folder_path = "C:/Users/sp13/OneDrive/Desktop/docs/"

    for file_info in sorted_files3:
        file_name = file_info[0]
        file_path = folder_path + file_name
        filtered_files2.append(file_path)

    print("filtered_files2 with sorted_files3 start")
    print(filtered_files2)
    print("filtered_files2 with sorted_files3 start")
    

    matching_files_str = "\n".join([f"{file}         {percentage:.2f}%   with Matching Keywords  {matching_keywords} {state} " for file, percentage,matching_keywords,state in sorted_files1])
    matching_files_str1 = "\n".join([f"{file}        {percentage:.2f}%   with Matching Keywords  {matching_keywords} {state}" for file, percentage,matching_keywords,state in sorted_files2])
    matching_files_str2 = "\n".join([f"{file}        {percentage:.2f}%   with Matching Keywords  {matching_keywords} {state}" for file, percentage,matching_keywords,state in sorted_files3])
      

    count = len(matching_files + matching_files1 + matching_files2)

    print(f" {count} files were filtered ".format(count))


    return count,filtered_files,matching_files_str,filtered_files1,matching_files_str1,filtered_files2,matching_files_str2


# inputs = gr.inputs.Textbox(lines=4, label="Description",placeholder = "Enter some detailed job description.....")   


# outputs = [gr.outputs.Textbox(label="NUMBER OF FILES FILTERED"),gr.outputs.File(label="FILES TO DOWNLOAD ABOVE 75%"),gr.outputs.Textbox(label="FILES WITH MATCHING and MATCHING KEYWORDS PERCENTAGE ABOVE 75%"),gr.outputs.File(label="FILES TO DOWNLOAD BETWEEN 50% to 75%"),gr.outputs.Textbox(label="FILES WITH MATCHING PERCENTAGE and MATCHING KEYWORDS PERCENTAGE BETWEEN 50% to 75%"),gr.outputs.File(label="FILES TO DOWNLOAD BELOW 50%"),gr.outputs.Textbox(label="FILES WITH MATCHING PERCENTAGE and MATCHING KEYWORDS BELOW 50%")]
