from flask import Flask, jsonify, request
app = Flask(__name__)

list=[{
    id:1,
    name:'raju',
    contact: '9813563290',
    done: False
},{
    id:2,
    name:'rajiv',
    contact: '9113523690',
    done: False
    
}]

@app.route('/')

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            status:'error',
            message:'please provide the data'
        })

    contact={
        id:task[-1]['id']+1,
        name:request.json['name'],
        contact:request.json.get('contact',''),
        done:False


    }

    List.append(contact)
    return jsonify({
            status:'success',
            message:'contact added succesfully'
        })

@app.route('/get-data')

def get_task():
    return jsonify({
        data:List
    })

if(__name__ == '__main__') :
    app.run(debug=True)