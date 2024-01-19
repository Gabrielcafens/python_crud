from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulação de um banco de dados simples para usuários (substitua isso com um sistema de autenticação real)
usuarios = {
    'usuario1': {'senha': 'senha123'},
    'usuario2': {'senha': 'senha456'}
}

@app.route("/login", methods=['POST'])
def login():
    # Verificar se a requisição contém dados JSON no corpo
    if request.is_json:
        # Obter os dados JSON da requisição
        dados_login = request.get_json()

        # Extrair nome de usuário e senha do JSON
        usuario = dados_login.get('usuario')
        senha = dados_login.get('senha')

        # Verificar se o usuário existe e a senha está correta
        if usuario in usuarios and usuarios[usuario]['senha'] == senha:
            # Se as credenciais estiverem corretas, retornar uma mensagem de sucesso
            return jsonify({"mensagem": "Login bem-sucedido!"})
        else:
            # Se as credenciais estiverem incorretas, retornar uma mensagem de erro
            return jsonify({"error": "Credenciais inválidas"}), 401
    else:
        # Se a requisição não contiver dados JSON, retornar uma mensagem de erro
        return jsonify({"error": "A requisição deve conter dados JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)
