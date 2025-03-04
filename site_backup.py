from flask import Flask, request, render_template, send_file
import datetime
import zipfile
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    error = None
    if request.method == 'POST':
        files = request.files.getlist('files')
        if not files:
            error = "Nenhum arquivo foi selecionado!"
        else:
            try:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
                zip_filename = f"backup_{timestamp}.zip"
                
                memory_file = io.BytesIO()
                with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                    for file in files:
                        zf.writestr(file.filename, file.read())
                
                memory_file.seek(0)
                return send_file(
                    memory_file,
                    download_name=zip_filename,
                    as_attachment=True
                )
            except Exception as e:
                error = f"Ocorreu um erro durante o processamento: {str(e)}"
    return render_template('index.html', message=message, error=error)

if __name__ == '__main__':
    app.run(debug=True)

