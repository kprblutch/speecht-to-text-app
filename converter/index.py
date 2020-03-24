import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.utils import secure_filename

from converter.auth import login_required
from .static import const
from speechtotext import converter as conv


bp = Blueprint('index', __name__)

# Check if the audi file has the right extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in const.ALLOWED_EXTENSIONS


# function to allow users to login
@bp.route('/', methods=('GET', 'POST'))
@login_required
def converter():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filelocation= os.path.join(os.path.dirname(os.getcwd()),const.UPLOAD_FOLDER, filename)
            file.save(filelocation)
        language = request.form.get('lanuagedropdown')
        samplerate = request.form['samplerate']
        encoding = request.form['encoding']

        text = conv.convert_local_file(os.path.join(os.path.dirname(os.getcwd()),const.UPLOAD_FOLDER, filename), language, samplerate, encoding)

        error = None

        flash(error)
        if error is None:
            return render_template('index/show.html', filename=filename, language=language, samplerate=samplerate, encoding=encoding, text=text)
    return render_template('index/index.html')
