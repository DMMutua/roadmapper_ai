from flask import render_template, request, jsonify
#from ..crew import RoadmapperaiCrew

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

#@app.route('/roadmap', methods=['POST'])
#def run_crew():
#    role = request.form.get('role')
#    ins = {'position': role}
#    RoadmapperaiCrew().crew().kickoff(inputs=ins)
#    return jsonify({"status": "success", "message": "Crew run Successfully"})


