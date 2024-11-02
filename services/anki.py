import genanki
import random
import json
import os
from flask import url_for, current_app
# from base import create_app

# app = create_app()


class AnkiDeckGenerator:
    def __init__(self, package_name):
        self.package_name = package_name

    def gen_deck(self, file):
        # Create a new model to work with
        new_model = genanki.Model(
            random.randrange(1 << 30, 1 << 50),
            'Simple_model',  # This is the name of the model
            # Defining the fields of the model
            fields=[
                {'name': "Question"},
                {'name': "Answer"},
            ],
            # Defining the template
            templates=[
                {
                    'name': 'Card',
                    'qfmt': '{{Question}}',
                    'afmt': '{{Question}}<hr id="answer">{{Answer}}',
                },
            ]
        )

        # Initialize a new anki deck
        new_deck = genanki.Deck(
            random.randrange(1 << 30, 1 << 50),
            self.package_name
        )

        # Open and read the JSON file
        with open(file, 'r') as f:
            questions = json.load(f)  # Load the JSON data as a list of dictionaries

        # Loop through each question in the JSON data
        for Qdict in questions:
            # Create a new note with the question and answer fields
            new_note = genanki.Note(
                model=new_model,
                fields=[Qdict["Question"], Qdict["Answer"]]
            )
            # Add the new note to the deck
            new_deck.add_note(new_note)

        save_path = os.path.join(current_app.root_path, f'static/success/{self.package_name}.apkg')

        # Create a package for the populated deck and save the file at Success Files/{package_name}
        genanki.Package(new_deck).write_to_file(save_path)
        print(f"{self.package_name} has been successfully created!")
        return 0


if __name__ == '__main__':
    with current_app.app_context():
        mn = AnkiDeckGenerator("GUIDE FOR PREPARATION FOR INTERVIEW")
        mn.gen_deck("GUIDE FOR PREPARATION FOR INTERVIEW.json")
