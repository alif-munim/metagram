from flask import Flask, flash, request, redirect, url_for, Response
from werkzeug.utils import secure_filename
from imageCleaup import ImageProcessing
import os

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)


# real credentials are privated
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os


credentials_dict = {
    'type': 'service_account',
    'client_id': os.environ['BACKUP_CLIENT_ID'],
    'client_email': os.environ['BACKUP_CLIENT_EMAIL'],
    'private_key_id': os.environ['BACKUP_PRIVATE_KEY_ID'],
    'private_key': os.environ['BACKUP_PRIVATE_KEY'],
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict
)



@app.route('/upload_albumn', methods=['POST'])
def filter_images():
    file = request.files['file[]']
    if file:
        filename = secure_filename(file.filename)
        imgs = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        for i in imgs:
            pic = ImageProcessing(UPLOAD_FOLDER + i)
            pic.process_all(export=True, outputName='/results'+i)

        client = storage.Client(credentials=credentials, project='myproject')
        bucket = client.get_bucket('mybucket')
        blob = bucket.blob('myfile')
        file_names = [f for f in os.listdir('/results') if os.path.isfile(os.path.join('/results', f))]

        # upload files
        for i in file_names:
            blob.upload_from_filename(i)

        # remove files
        for f in os.listdir('/results'):
            os.remove(os.path.join('/results', f))

    return Response(status=200)


