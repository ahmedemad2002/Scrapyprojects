# import json
# data = json.load(open('fullurls.json', 'r'))

# start_urls = [data[i]['url'] for i in range(len(data))]
# print(start_urls, '/n')


data = '[{"rank":20,"year":2014},{"rank":19,"year":2015},{"rank":18,"year":2016},{"rank":12,"year":2017},{"rank":8,"year":2018},{"rank":4,"year":2019},{"rank":2,"year":2020},{"rank":1,"year":2021},{"rank":1,"year":2022},{"rank":1,"year":2023}]'

print(eval(data)[1]['rank'])
