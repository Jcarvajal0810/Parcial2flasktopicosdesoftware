from flask import Flask, render_template

app = Flask(__name__)

# Función para calcular el factorial
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

# Ruta principal
@app.route('/')
def index():
    return render_template('factorial.html', mensaje="Ingresa un número en la URL para calcular su factorial")

# Ruta para calcular el factorial
@app.route('/factorial/<int:numero>')
def factorial(numero):
    try:
        if numero < 0:
            return render_template('factorial.html', mensaje="Error: No se puede calcular el factorial de un número negativo.", error=True)
        elif numero > 170:
            return render_template('factorial.html', mensaje="Error: El número es demasiado grande para calcular su factorial.", error=True)
        
        resultado = calcular_factorial(numero)
        return render_template('factorial.html', mensaje=f"El factorial de {numero} es: {resultado}", numero=numero)
    except RecursionError:
        return render_template('factorial.html', mensaje="Error: El número es demasiado grande para calcular su factorial.", error=True)
    except Exception as e:
        return render_template('factorial.html', mensaje=f"Error: {str(e)}", error=True)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)