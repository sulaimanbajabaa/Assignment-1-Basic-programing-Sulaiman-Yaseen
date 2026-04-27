# CBMM 2013 - Assignment 1
# Movie Collection Manager (Starter Template)
# Lecturer: Mohd Faiz bin Alias

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 8.9},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6}
]


def show_menu():
    print("\nMovie Collection Manager")
    print("1. Add movie")
    print("2. View movies")
    print("3. Search movie")
    print("4. Exit")

def add_movie():

    title = input("Enter movie title: ").strip()
    genre = input("Enter genre: ").strip()
    
    while True:
        try:
            rating = float(input("Enter rating (0-10): "))
            if 0 <= rating <= 10:
                break
            else:
                print("Rating must be between 0-10.")
        except ValueError:
            print("Please enter a valid number.")
    
    movies.append({"title": title, "genre": genre, "rating": rating})
    print(f"Movie '{title}' added successfully!")
    


def view_movies():
    if not movies:
        print("No movies available")
        return
    
    print("\nMovie Collection:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']}")
        print(f"   Genre  : {movie['genre']}")
        print(f"   Rating : {movie['rating']}/10")
        print("_" * 40)



def search_movie():
    """Search for a movie by title"""
    search_title = input("Enter movie title to search: ").strip().lower()
    
    found = False
    for movie in movies:
        if search_title in movie['title'].lower():
            print(f"\nMovie found!")
            print(f"Title  : {movie['title']}")
            print(f"Genre  : {movie['genre']}")
            print(f"Rating : {movie['rating']}/10")
            found = True
            break
    
    if not found:
        print(f"Movie '{search_title}' not found.")


def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_movie()

        elif choice == "2":
            view_movies()

        elif choice == "3":
            search_movie()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


main()
