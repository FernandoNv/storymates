
# from moque import get_articles, create_article, update_article, delete_article
# from moque import get_comments, create_comment, update_comment, delete_comment
from client import get_articles, get_article_by_id, create_article, update_article, delete_article
from client import get_comments, create_comment, update_comment, delete_comment

def print_articles():
    articles = get_articles()
    for article in articles:
        print(f"ID: {article['id']}, Title: {article['title']}, Content: {article['content']}")

def print_comments(article_id):
    comments = get_comments(article_id)
    for comment in comments:
        print(f"ID: {comment['id']}, Content: {comment['content']}")

def main():
    name = input("Enter your name:")

    while True:
        print("\n1. List Articles")
        print("2. View Article")
        print("3. Create Article")
        print("4. Update Article")
        print("5. Delete Article")
        print("6. Create Comment")
        print("7. Update Comment")
        print("8. Delete Comment")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            print_articles()

        elif choice == '2':
            author_id = input("Enter the article id: ")
            article = get_article_by_id(author_id)
            print(f"\n  {article['title']}  ")
            print(f"author: {article['author']}")
            print(f"\n\n{article['content']}\n\n")
            for comment in article['comments']:
                print(f"{comment["id"]}. {comment["author"]}:\n\n {comment["content"]}")

        elif choice == '3':
            title = input("Enter the article title: ")
            content = input("Enter the article content: ")
            create_article(name, {"title": title, "content": content})
            print("Article created successfully!")

        elif choice == '4':
            
            article_id = input("Enter the article ID to update: ")
            title = input("Enter the new article title: ")
            content = input("Enter the new article content: ")
            update_article(name, article_id, {"title": title, "content": content})
            print("Article updated successfully!")

        elif choice == '5':
            article_id = input("Enter the article ID to delete: ")
            delete_article(name, article_id)
            print("Article deleted successfully!")

        elif choice == '6':
            article_id = input("Enter the article ID to add a comment: ")
            content = input("Enter the comment content: ")
            create_comment(name, {"content": content, "articleId": article_id })
            print("Comment created successfully!")

        elif choice == '7':
            comment_id = input("Enter the comment ID to update: ")
            content = input("Enter the new comment content: ")
            update_comment(comment_id, content)
            print("Comment updated successfully!")

        elif choice == '8':
            comment_id = input("Enter the comment ID to delete: ")
            delete_comment(comment_id)
            print("Comment deleted successfully!")

        elif choice == '9':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
