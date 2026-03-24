import json
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

def get_reporters_file():
    return os.path.join(settings.BASE_DIR, 'reporters.json')

def get_issues_file():
    return os.path.join(settings.BASE_DIR, 'issues.json')

def read_json_file(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_json_file(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

@csrf_exempt
def reporter_list_create(request):
    reporters_file = get_reporters_file()
    
    if request.method == 'GET':
        reporters = read_json_file(reporters_file)
        reporter_id = request.GET.get('id')
        
        if reporter_id:
            try:
                reporter_id = int(reporter_id)
            except ValueError:
                return JsonResponse({'error': 'Invalid ID format'}, status=400)
                
            for reporter in reporters:
                if reporter['id'] == reporter_id:
                    return JsonResponse(reporter, status=200)
            return JsonResponse({'error': 'Reporter not found'}, status=404)
            
        return JsonResponse(reporters, safe=False, status=200)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
        reporters = read_json_file(reporters_file)
        
        new_id = 1
        if reporters:
            new_id = max(r.get('id', 0) for r in reporters) + 1
            
        try:
            reporter = Reporter(
                id=new_id,
                name=data.get('name'),
                email=data.get('email', ''),
                team=data.get('team')
            )
            reporter.validate()
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
            
        reporter_dict = reporter.to_dict()
        reporters.append(reporter_dict)
        write_json_file(reporters_file, reporters)
        
        return JsonResponse(reporter_dict, status=201)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def issue_list_create(request):
    issues_file = get_issues_file()
    
    if request.method == 'GET':
        issues = read_json_file(issues_file)
        issue_id = request.GET.get('id')
        status_filter = request.GET.get('status')
        
        if issue_id:
            try:
                issue_id = int(issue_id)
            except ValueError:
                return JsonResponse({'error': 'Invalid ID format'}, status=400)
                
            for issue in issues:
                if issue['id'] == issue_id:
                    return JsonResponse(issue, status=200)
            return JsonResponse({'error': 'Issue not found'}, status=404)
            
        if status_filter:
            filtered_issues = [issue for issue in issues if issue.get('status') == status_filter]
            return JsonResponse(filtered_issues, safe=False, status=200)
            
        return JsonResponse(issues, safe=False, status=200)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
        issues = read_json_file(issues_file)
        
        new_id = 1
        if issues:
            new_id = max(i.get('id', 0) for i in issues) + 1
            
        priority = data.get('priority')
        
        try:
            if priority == 'critical':
                issue = CriticalIssue(
                    id=new_id,
                    title=data.get('title'),
                    description=data.get('description'),
                    status=data.get('status'),
                    priority=priority,
                    reporter_id=data.get('reporter_id')
                )
            elif priority == 'low':
                issue = LowPriorityIssue(
                    id=new_id,
                    title=data.get('title'),
                    description=data.get('description'),
                    status=data.get('status'),
                    priority=priority,
                    reporter_id=data.get('reporter_id')
                )
            else:
                issue = Issue(
                    id=new_id,
                    title=data.get('title'),
                    description=data.get('description'),
                    status=data.get('status'),
                    priority=priority,
                    reporter_id=data.get('reporter_id')
                )
            
            issue.validate()
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
            
        response_data = issue.to_dict()
        response_data['message'] = issue.describe()
        
        save_data = issue.to_dict()
        issues.append(save_data)
        write_json_file(issues_file, issues)
        
        return JsonResponse(response_data, status=201)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)
