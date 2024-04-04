from flask import Flask, request, jsonify
import chatbot
import logging

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def respond():
    message = request.json['message']
    ints = chatbot.predict_class(message)
    res = chatbot.get_response(ints, chatbot.intents)
    return jsonify({'response': res})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'UP'}), 200

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting Flask server...')
    app.run(debug=False)