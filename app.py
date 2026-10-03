from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nota Online - Prof Joni</title>
<style>
body{font-family:Arial;background:#f0f4f8;padding:20px}
.card{background:white;max-width:500px;margin:auto;padding:25px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
h1{color:#1e40af;text-align:center}
input{width:100%;padding:12px;margin:8px 0;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:#2563eb;color:white;border:none;border-radius:8px;font-size:16px;font-weight:bold}
.result{margin-top:15px;padding:15px;background:#dbeafe;border-radius:8px;text-align:center;font-size:18px}
</style>
</head>
<body>
<div class="card">
<h1>📚 Calculadora de Notas</h1>
<p style="text-align:center">Prof. Joni - Informática - Beira</p>
<form method="POST">
<input type="number" step="0.1" name="n1" placeholder="Nota 1 (ACS)" required>
<input type="number" step="0.1" name="n2" placeholder="Nota 2 (ACP)" required>
<input type="number" step="0.1" name="n3" placeholder="Nota 3 (Exame/Teste)" required>
<button type="submit">Calcular Média</button>
</form>
{% if media is not none %}
<div class="result">
Média: <b>{{ media }}</b><br>
Situação: <b>{{ situ }}</b>
</div>
{% endif %}
<br><a href="/" style="text-align:center;display:block">Recalcular</a>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def index():
    media = None
    situ = ""
    if request.method == 'POST':
        try:
            n1=float(request.form['n1']); n2=float(request.form['n2']); n3=float(request.form['n3'])
            media = round((n1+n2+n3)/3,2)
            if media >= 10: situ="✅ APROVADO"
            elif media >= 7: situ="🟡 RECUPERAÇÃO"
            else: situ="❌ REPROVADO"
        except: media=0
    from flask import render_template_string
    return render_template_string(HTML, media=media, situ=situ)

if __name__ == '__main__':
    app.run()
