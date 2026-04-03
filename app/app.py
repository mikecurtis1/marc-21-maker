from flask import Flask, request, render_template, Response
import csv
from marc21 import MARC21Maker

app = Flask(__name__)

@app.before_request
def log_request():
    app.logger.info(f"Incoming request: {request.method} {request.path} from {request.remote_addr}")

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def upload():
    file = request.files["csv"]

    decoded = file.stream.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded, delimiter="\t")

    output = ""

    for row in reader:
        mrc = MARC21Maker(row['L5'], row['L6'], row['L7'])

        mrc.add_control_field('001', row['number'])
        mrc.add_data_field('100', '0', ' ', '$a' + row['author'])
        mrc.add_data_field('245', ' ', ' ', '$a' + row['title'])
        mrc.add_data_field('264', ' ', '1', '$c' + row['pubdate'])

        output += mrc.get_mrc()

    return Response(
        output,
        mimetype="application/marc",
        headers={
            "Content-Disposition": "attachment; filename=set_of_marc_records.mrc"
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
