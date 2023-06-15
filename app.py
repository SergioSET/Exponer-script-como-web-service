from flask import Flask, request
import yfinance

app = Flask(__name__)

@app.route('/', methods=['POST'])
def consultAction():
    data = request.get_json()
    action = data['accion']
    startDate = data['fecha_inicial']
    endDate = data['fecha_final']

    data = yfinance.download(action, startDate, endDate)
    
    data = data.tail()

    string = f"Se mostrarán las acciones de {action} desde {startDate} hasta {endDate}\n {data}"

    return string

if __name__ == '__main__':
    print('Starting Flask Server')
    app.run(debug=True)