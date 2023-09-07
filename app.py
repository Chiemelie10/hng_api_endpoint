"""This module defines the function get_information."""
from datetime import datetime
from flask import Flask, request, jsonify


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/api', methods=['GET'])
def get_information():
    """This function returns a response of specific required information."""
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None:
        return jsonify({'error': 'slack_name is required in the url string.'}), 400
    elif track is None:
        return jsonify({'error': 'track is required in the url string.'}), 400

    data = {
        'slack_name': slack_name,
        'current_day': datetime.utcnow().strftime('%A'),
        'utc_time': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'github_file_url': 'https://github.com/Chiemelie10/hng_api_endpoint/blob/main/app.py',
        'github_repo_url': 'https://github.com/Chiemelie10/hng_api_endpoint',
        'status_code': 200
    }

    return jsonify(data), 200


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)
