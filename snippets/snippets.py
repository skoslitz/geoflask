def python():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
    data = json.load(open(json_url, 'r'))
    return render_template('python.jade', data=data)