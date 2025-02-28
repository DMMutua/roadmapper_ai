from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
#from crew import RoadmapperaiCrew
from ..task_callbacks import user_select_tools, load_task_output
from ..output_structure import Tool_Structure
from .task_runner import run_single_task

tool_options_bp = Blueprint('tool_options_bp', __name__)

@tool_options_bp.route('/tool_options_input', methods=['GET', 'POST'])
def tool_options_input():
    if request.method == 'POST':
        role = request.form.get('role')
        inputs = {'position': role.strip()}
        
        try:
            task_output = run_single_task('tool_options', inputs)
            # Storing task output in session for later use
            session['task_output'] = task_output
            
            return redirect(url_for('tool_options_bp.tool_options_output'))
        except Exception as e:
            return f"Error running task: {str(e)}", 500
            
    return render_template('tool_options_input.html')

@tool_options_bp.route('/tool_options_output', methods=['GET', 'POST'])
def tool_options_output():
    task_output = session.get('task_output')
    if not task_output:
        return redirect(url_for('tool_options_bp.tool_options_input'))
    
    data = load_task_output(task_output, Tool_Structure)
    tools_list = data["TOOLS_LIST"]

    if request.method == 'POST':
        selected_tools = request.form.getlist('selected_tools')
        if len(selected_tools) > 2:
            return "Please select no more than 2 tools.", 400
            
        # Processing selected tools
        updated_task_output = user_select_tools(task_output, max_choices=2)
        
        # Store updated output for next task
        session['updated_task_output'] = updated_task_output
        
        return jsonify({
            "status": "success",
            "message": "Tools selected successfully",
            "updated_task_output": updated_task_output
        })

    return render_template('tool_options_output.html', 
                         tools_list=tools_list,
                         position=data['POSITION'])