from flask import render_template, Blueprint, request, redirect, jsonify, url_for, flash, current_app
from services.anki import AnkiDeckGenerator
from werkzeug.utils import secure_filename
import os


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@main.route('/anncouncements', methods=['GET'])
def announcements():
    return render_template('announcements.html')


@main.route('/donate', methods=['GET'])
def donate():
    return render_template('donate.html')


@main.route('/get-deck', methods=['GET', 'POST'])
def get_deck():
    if request.method == 'POST':
        if 'lecture-note' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['lecture-note']

        if file.filename == '':
            flash("No file selected")
            return redirect(request.url)

        if file:
            # Secure the filename and define the upload path
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.static_folder, 'uploads', filename)

            # Save the file to the specified upload path
            file.save(upload_path)

            # Create an instance of AnkiDeckGenerator and generate the deck
            generator = AnkiDeckGenerator(filename.removesuffix('.json'))
            generator.gen_deck(upload_path)

            # Prepare download URL for the generated deck (assuming it saves as .apkg)
            return render_template('index.html', download_url=True, filename=filename.removesuffix('.json'))

    return jsonify({"Error": "File Upload Failed"}), 400

