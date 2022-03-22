"""
Author’s Last Name, First Name. “Title of Work.” Website, Day Month Year of publication, URL.
"""

import pandas as p


def cite_formatting():
    df = p.read_csv("sources_info.csv")

    l = []
    for i in range(len(df.index)):
        row = dict(df.iloc[i])
        last_name, first_name, title, website_name, date_of_publication, url = row['lastName'], row[
            'firstName'], row['title'], row['websiteName'], row['dataOfPublication'], row['url']

        final_cite = f'{last_name}, {first_name}. "{title}." {website_name}, {date_of_publication}, {url}'
        l.append(final_cite)
    return l


l = cite_formatting()
for x in range(len(l)):
    print(l[x])
