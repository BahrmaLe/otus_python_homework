from Socket.html_parser import GetHTMLContent
from Socket.requests import Requests


def test_html_parsing(request):
    """Test HTML parsing"""
    data = Requests(request)
    get = GetHTMLContent()
    get.feed(data.text())
    if request.config.getoption("--links"):
        for link in get.links:
            print(link)

    if request.config.getoption("--images"):
        for img in get.img:
            print(img)

    if request.config.getoption("--tags"):
        frequency_analysis = dict((i, get.tags.count(i)) for i in get.tags)
        sorted_frequency_analysis = sorted(frequency_analysis.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_frequency_analysis:
            print(item)

    if request.config.getoption("--toptag"):
        frequency_analysis = dict((i, get.tags.count(i)) for i in get.tags)
        sorted_frequency_analysis = sorted(frequency_analysis.items(), key=lambda x: x[1], reverse=True)
        print("Top tag: ", sorted_frequency_analysis[0])
