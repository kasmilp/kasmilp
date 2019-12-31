import os
from blog_ku import app

#class User dan Post sebelumnya dipindah ke models.py


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
