    # # Save report file

    # # Download whole report locally including code diff links
    # mosspy.download_report(url, "submission/report/", connections=8)

report_page = "submissions/report.html"
if __name__ == '__main__':
    html = open(report_page, 'r')
    print(html.read())
    html.close()
