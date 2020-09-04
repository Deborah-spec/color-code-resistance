from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return"findresistance"

@app.route("findresistance/<string:a>",methods=['GET'])
def findresistance(a,b,c,d):
     color_digit ={'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
     multiplier = {'black': '1', 'brown': '10', 'red': '100', 'orange': '1k', 'yellow': '10k', 'green': '100k', 'blue': '1M', 'violet': '10M', 'grey': '100M', 'white': '1G'}
     tolerance = {'brown': '+/- 1%', 'red': '+/-2%', 'green': '+/-0.5%', 'blue': '+/- 0.25%', 'violet': '+/- 0.1%', 'gold': '+/- 5%', 'silver': '+/- 10%', 'none': '+/- 20%'}
     if (a in color_digit
        and b in color_digit\
        and c in multiplier
        and d in tolerance):
        xx = color_digit.get(a)
        yy = color_digit.get(b)
        zz = multiplier.get(c)
        aa = tolerance.get(d)
        print("resistance =" +xx + yy+ " * " +zz+ " ohms " +aa)
        result
        {
        "Resistance": resistance
        }
     else:
        print("Invalid Colors")


        return jsonify({result})
