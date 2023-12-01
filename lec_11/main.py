import requests

def perform_request(method, url):
    response = requests.request(method, url)
    if response.status_code == 200:
        print(f"{method.upper()} request successful, status code {response.status_code}")
        return response.json()
    else:
        print(f"Failed to make {method.upper()} request, status code {response.status_code}")
        return None

def filter_titles_and_bodies(data):
    titles = [item["title"] for item in data if len(item["title"]) > 6]
    bodies = [item["body"] for item in data if len(item["body"].split('\n')) > 3]
    return titles, bodies

get_data = perform_request("get", "https://jsonplaceholder.typicode.com/posts")
post_data = perform_request("post", "https://jsonplaceholder.typicode.com/posts/11")
put_data = perform_request("put", "https://jsonplaceholder.typicode.com/posts/2")
delete_data = perform_request("delete", "https://jsonplaceholder.typicode.com/posts/3")

if get_data:
    get_titles, get_bodies = filter_titles_and_bodies(get_data)
    print("Filtered Titles:")
    print(get_titles)
    print("\nFiltered Bodies:")
    print(get_bodies)