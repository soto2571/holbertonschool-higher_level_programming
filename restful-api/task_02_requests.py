import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        # Iterate through the parsed JSON data
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        # Structure the data into a list of dictionaries
        post_list = [{'id': post['id'],
                      'title': post['title'],
                      'body': post['body']}
                     for post in posts]

        # Write the data into a CSV file called posts.csv
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(post_list)
