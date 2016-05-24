from flask import request, jsonify, abort
from services import app

# TODO: modify this to db
site_addr = ""


@app.route("/sites/usr/request_report", methods=["GET"])
def user_request_report():
    global site_addr
    reply = {"site-ip": site_addr}
    return jsonify(reply)


@app.route("/sites/site/report", methods=["POST"])
def site_report():
    global site_addr
    content = request.json
    if not content or "addr" not in content:
        abort(400)

    try:
        print content
        site_addr = content["addr"]
    except Exception, e:
        print str(e)
        abort(400)

    return jsonify({})
