from flask import Flask, render_template, jsonify
import speedtest

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def run_speedtest():
    try:
        # Initialize the Speedtest object
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        
        # Return the results as JSON
        return jsonify({
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': round(ping, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if _name_ == '_main_':
    app.run(debug=True)
