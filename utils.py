from bs4 import BeautifulSoup
import mosspy
import re

def put_text_into_files(basefile, comparison_files):
    put_text_to_file(
        basefile, 
        "basefile.c"
    )
    
    for comparison_file in comparison_files:
        filename = comparison_file['id'] + ".c"
        
        put_text_to_file(
            comparison_file['code'], 
            filename
        )

    
def put_text_to_file(text, filename):
    directory = 'submissions/' + filename
    file_object = open(directory, 'w')
    file_object.write(text)


USER_ID = 174135898
LANGUAGE = "c"
report_page = "submissions/report.html"

def moss_create_report_rage(comparison_files):
    client = mosspy.Moss(USER_ID, LANGUAGE)
    basefile = 'submissions/basefile.' + LANGUAGE
    client.addBaseFile(
        basefile
    )
    for comparison_file in comparison_files: 
        client.addFile(
            'submissions/' + comparison_file['id'] + '.' + LANGUAGE
        )

    url = client.send() 
    client.saveWebPage(url, report_page)


def moss_parse_html():
    html = open(report_page, 'r')
    html_code = html.read()
    html.close()
    
    parsed_html = BeautifulSoup(html_code).find_all("a")
    
     
    similarities = {}
    
    for a in parsed_html[6:]:
        parsed_line = re.sub('(submissions/|.c|\\(|\\))', '', a.text)
        id, similarity = parsed_line.split(' ')
        if id in similarities:
            similarities[id] = max(similarity, similarities[id])
        else: 
            similarities[id] = similarity
    return {
        "similarities": similarities,
        "html_code": str(html_code)
    }
        
    