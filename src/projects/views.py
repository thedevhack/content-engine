from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from projects.models import Project


def delete_project_session(request):
    try:
        del request.session['project_handle']
    except:
        pass


def activate_project_view(request, handle=None):

    if handle is None:
        return HttpResponseBadRequest()

    try:
        project_obj = Project.objects.get(
            owner=request.user,
            handle=handle
        )

    except Exception as e:
        print("inside exception", e)
        project_obj = None

    print(project_obj, handle)

    if project_obj is None:
        delete_project_session(request)
        messages.error(request, "Project could not activate. please try again")
        return redirect('/projects')
    request.session['project_handle'] = handle
    messages.error(request, "Project activated.")
    return redirect('/')


def deactivate_project_view(request, handle=None):
    delete_project_session(request)
    return redirect('/')

