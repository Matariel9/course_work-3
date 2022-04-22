from dataclasses import dataclass
import json

def get_posts_all():
    with open('coursework2_source/data/data.json', encoding="utf8") as jsonFile:
        data = json.load(jsonFile)
    return data

def get_posts_by_user(name,data):
    posts = []
    for i in range(len(data)):
        if data[i]['poster_name'].lower() == name.lower():
            posts.append(data[i])
    return posts

def get_comments_by_post_id(post_id,data):
    comments = []
    comms = []
    with open('coursework2_source/data/comments.json', encoding="utf8") as jsonFile:
        comms = json.load(jsonFile)
    for i in range(len(data)):
        if post_id == comms[i]['post_id']:
            comments.append(comms[i])
    print(comments)
    return comments

def search_for_posts(query,data):
    found = []
    for i in range(len(data)):
        if (query in data[i]['content']) or (query in data[i]['poster_name']):
            found.append(data[i])
    return found

def get_posts_by_pk(pk,data):
    for i in range(len(data)):
        if(data[i]['pk'] == pk):
            return data[i]

def length(data):
    if len(data)>10:
        return 10
    else:
        return len(data)