from app import application

if __name__ == "__main__":
    application.run(debug=True, threaded=True, host='0.0.0.0', port=5000)
