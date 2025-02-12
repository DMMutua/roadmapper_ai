from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from crew import RoadmapperaiCrew
from task_callbacks import user_select_tools, load_task_output
from output_structure import Tool_Structure

tool_options_bp = Blueprint('tool_options_bp', __name__)

@tool_options_bp.route('/tool_options_input', methods=['GET', 'POST'])
def tool_options_input():
    if request.method == 'POST':
        role = request.form.get('role')
        ins = {'position': role}
        task_output = RoadmapperaiCrew().tool_options().run(inputs=ins)
        return redirect(url_for('tool_options_bp.tool_options_output',
                                task_output=task_output))
    return render_template('tool_options_input.html')

@tool_options_bp.route('/tool_options_output', methods=['GET', 'POST'])
def tool_options_output():
    task_output = request.args.get('task_output')
    data = load_task_output(task_output, Tool_Structure)
    tools_list = data["TOOLS_LIST"]

    if request.method == 'POST':
        selected_tools = request.args.getlist('selected_tools')
        if len(selected_tools) > 2:
            return "Please Select No More than 2 Tools.", 400
        # Processing Selected Tools
        updated_task_output = user_select_tools(task_output, max_choices=2)
        return jsonify({"status": "success",
                        "message": "Tools selected successfully",
                        "updated_task_output": updated_task_output})
    return render_template('tool_options_output.html',
                           tools_list=tools_list,
                           position=data['POSITION'])