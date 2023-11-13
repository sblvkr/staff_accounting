from django.shortcuts import render, get_object_or_404, redirect
from staff.models import Employer, Position
from staff.forms import EmployerForm, PositionForm


def create_or_edit_object(request, form_class, template_name, redirect_to, instance_id=None):
    instance = get_object_or_404(form_class.Meta.model, pk=instance_id) if instance_id else None
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_to)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {'form': form})


def remove_object(request, model, redirect_to, instance_id):
    instance = get_object_or_404(model, pk=instance_id)
    instance.delete()
    return redirect(redirect_to)


# Views for Employers

def employer_list(request):
    employers = Employer.objects.all()
    return render(
        request,
        'staff/employer_list.html',
        {'employers': employers},
    )


def employer_create(request):
    return create_or_edit_object(
        request,
        EmployerForm,
        'staff/employer_form.html',
        'staff:employer_list',
    )


def employer_edit(request, employer_id):
    return create_or_edit_object(
        request,
        EmployerForm,
        'staff/employer_form.html',
        'staff:employer_list',
        instance_id=employer_id,
    )


def employer_remove(request, employer_id):
    return remove_object(
        request,
        Employer,
        'staff:employer_list',
        instance_id=employer_id,
    )


# Views for Positions

def positions_list(request):
    positions = Position.objects.all()
    return render(
        request,
        'staff/position_list.html',
        {'positions': positions},
    )


def position_create(request):
    return create_or_edit_object(
        request,
        PositionForm,
        'staff/position_form.html',
        'staff:positions_list',
    )


def position_edit(request, position_id):
    return create_or_edit_object(
        request,
        PositionForm,
        'staff/position_form.html',
        'staff:positions_list',
        instance_id=position_id,
    )


def position_remove(request, position_id):
    return remove_object(
        request,
        Position,
        'staff:positions_list',
        instance_id=position_id,
    )
