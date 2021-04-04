# Moss API service
 Receives codes and send for similarity check to MOSS API, and then returns parsed results of similarity with html report. 

## Installation guide
  * git clone repo
  * create virtualenv
  * `cd mosspy`
  * `pip install -r requirement.txt`

## API documentation
### To send codes: 
* Request method: POST
* URL: http://127.0.0.1:5000/
* Body: 
    * send: List of codes = {submissions = (unique code id, code), template_code}
    * - receive: List of similarity = { reports = [(unique code id, similarity)], html_report}
```
curl --location --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "basefile": "#include <stdio.h>\n #include <math.h>\n\n int main(void) {\n \treturn 0;\n}",
    "comparison_files": [
        {
            "code": "#include <stdio.h>\n #include <math.h>\n\n int main(void) {\n asdsadsadsadasd\treturn 0;\n}",
            "id": "1"
        },
        {
            "code": "#include <stdio.h>\n #include <math.h>\n\n int main(void) {\n sadsadsadasdas\treturn 0;\n}",
            "id": "2"
        },
        {
            "code": "#include <stdio.h>\n #include <math.h>\n\n int main(void) {\n asdasdasdasdasdasdasdasdas\treturn 0;\n}",
            "id": "3"
        }
    ]
}'
```