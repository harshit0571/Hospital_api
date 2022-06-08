
from autoscraper import AutoScraper
from flask import Flask, request

Just_dial_scrapper = AutoScraper()
Just_dial_scrapper.load('justdial-search')
app = Flask(__name__)


def get_justdial_result(search_query):
    url = 'https://www.justdial.com/' + search_query + '/Hospitals'
    result = Just_dial_scrapper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)


def _aggregate_result(result):
    final_result = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:

            final_result.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return final_result


@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    print(query)
    return dict(result=get_justdial_result(query))


if __name__ == '__main__':
    app.run(debug=True)
