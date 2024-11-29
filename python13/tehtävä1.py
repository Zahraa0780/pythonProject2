from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def prime_check(number):
    result = {"number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=3000)