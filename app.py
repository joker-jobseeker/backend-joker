from remotejob import app, db
import os

if __name__ == '__main__':
    app.run()
    #app.run(host="0.0.0.0", port=5000, debug=os.environ.get('DEBUG')=="1")