import csv
import pandas as pd

def add_game():
    filename = "games.csv"

    new_game = {
        "name": input("Enter the game name: "),  
        "abbrev": input("Enter abbreviation: "),
        "release_year": int(input("Enter the release year (e.g., 2023): ")),
        "developer": input("Enter the developer name: "),  
        "rating": str(input("Enter the game rating: ")),
        "plot_summary": input("Enter the plot summary: "), 
        "links": {  
            "xbox": input("Enter the Xbox link: "),
            "playstation": input("Enter the PlayStation link: "),
            "steam": input("Enter the Steam link: ")
        },
        "likes": 0,
        "dislikes": 0,
        "img": input("Enter the image source URL: "), 
        "score": float(input("Enter the score: "))  
    }

    # Append to CSV
    try:
        with open(filename, mode="a", newline="") as file:
            fieldnames = [
                "name", "release_year", "developer", "rating", "plot_summary",
                "xbox", "playstation", "steam", "likes", "dislikes", "img", "score"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header only if the file is empty
            if file.tell() == 0:
                writer.writeheader()

            # Write the game data directly
            writer.writerow({
                "name": new_game["name"],
                "release_year": new_game["release_year"],
                "developer": new_game["developer"],
                "rating": new_game["rating"],
                "plot_summary": new_game["plot_summary"],
                "xbox": new_game["links"]["xbox"],
                "playstation": new_game["links"]["playstation"],
                "steam": new_game["links"]["steam"],
                "likes": new_game["likes"],
                "dislikes": new_game["dislikes"],
                "img": new_game["img"],
                "score": new_game["score"]
            })

        print(f"Game data appended to {filename}.")
    except Exception as e:
        print(f"Error: {e}")