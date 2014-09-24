from app import app
import sys

host = sys.argv[1]
port = int(sys.argv[2])

app.run(debug=True, host=host, port=port)
