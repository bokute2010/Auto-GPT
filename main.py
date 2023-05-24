from autogpt import main,utils

from autogpt.main import run_auto_gpt
import api_services


from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)
import pickle



# data = [{
    
#     'id': 1,
#     'continuous': False,
#     'continuous_limit': None,
#     'ai_settings': None,
#     'skip_reprompt': False,
#     'speak': False,
#     'debug': False,
#     'gpt3only': False,
#     'gpt4only': False,
#     'memory_type': None,
#     'browser_name': None,
#     'allow_downloads': False,
#     'skip_news': False,
#     'workspace_directory': None,
#     'install_plugin_deps': False,
# }]
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file) 


@app.route("/api/get_openai_response", methods=['POST'])
@cross_origin(origins='*')
def get_openai_response():
    body = api_services.get_args(request)
    user_id = body.get('user_id')
    user_frontend_input = body.get('user_frontend_input')
    user_data = utils.get_pickle(user_id)
    result = run_auto_gpt(
            user_data.get('continuous'),
            user_data.get('continuous_limit'),
            user_data.get('ai_settings'),
            user_data.get('skip_reprompt'),
            user_data.get('speak'),
            user_data.get('debug'),
            user_data.get('gpt3only'),
            user_data.get('gpt4only'),
            user_data.get('memory_type'),
            user_data.get('browser_name'),
            user_data.get('allow_downloads'),
            user_data.get('skip_news'),
            user_data.get('workspace_directory'),
            user_data.get('install_plugin_deps'),
            user_frontend_input
        )
    return result
    


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000, use_reloader=True)