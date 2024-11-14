from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Parse the JSON data sent in the webhook
    if data:  # Check if data is received
        print("Webhook received:", data)

        # Extract necessary information from the webhook data
        contact_id = data.get("contact_id")
        phone = data.get("phone")
        country = data.get("country")
        contact_source = data.get("contact_source")
        workflow_id = data["workflow"].get("id") if data.get("workflow") else None
        session_source = data["attributionSource"].get("sessionSource") if data.get("attributionSource") else None
        custom_data = data.get("customData", {})

        # Print or log the information for debugging purposes
        print(f"Contact ID: {contact_id}")
        print(f"Phone: {phone}")
        print(f"Country: {country}")
        print(f"Contact Source: {contact_source}")
        print(f"Workflow ID: {workflow_id}")
        print(f"Session Source: {session_source}")
        print(f"Custom Data: {custom_data}")

    # Respond with a 200 status code to acknowledge receipt
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
