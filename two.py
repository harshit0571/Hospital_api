from unittest import result
from autoscraper import AutoScraper

url = 'https://www.justdial.com/Delhi/Hospitals'


wanted_list = ["Dharamshila Narayana Supers..", "4.8",
               "https://content.jdmagicbox.com/comp/delhi/v5/011pxx11.xx11.190318155805.s1v5/catalogue/dharamshila-narayana-superspeciality-hospital-vasundhara-enclave-delhi-hospitals-2to1bg98o9.jpg?clr=#333333?fit=around%7C270%3A130&crop=270%3A130%3B%2A%2C%2A"]

scrapper = AutoScraper()

result = scrapper.build(url, wanted_list)
# print(result)

new1 = scrapper.get_result_similar(
    "https://www.justdial.com/Delhi/Hospitals", grouped=True)
# print(new1)
lists = list(new1.keys())
# print(lists)

scrapper.set_rule_aliases(
    {lists[0]: "Hospital-Name", lists[1]: "Stars", lists[3]: "Img"})
scrapper.keep_rules([lists[0], lists[1], lists[3]])
scrapper.save('justdial-search')


new_result = scrapper.get_result_similar(
    "https://www.justdial.com/Ambala/Hospitals", group_by_alias=True)

# print(new_result)
