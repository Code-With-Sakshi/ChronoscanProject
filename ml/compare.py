@app.route("/compare-ui", methods=["POST"])
def compare_ui():
    scan1 = request.files["scan_t1"]
    scan2 = request.files["scan_t2"]

    path1 = os.path.join(UPLOAD_DIR, scan1.filename)
    path2 = os.path.join(UPLOAD_DIR, scan2.filename)

    scan1.save(path1)
    scan2.save(path2)

    result = run_pipeline(path1, path2)

    return f"""
    <h2>📊 Analysis Result</h2>
    <p><b>Change Score:</b> {result['change_score']}</p>
    <h3>🧠 GenAI Clinical Report</h3>
    <pre>{result['report']}</pre>
    <br>
    <a href="/">⬅ Analyze another case</a>
    """


