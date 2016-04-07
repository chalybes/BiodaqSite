from django.shortcuts import render, redirect
from .models import Profile
from .forms import EntryForms


# Old index --- uncomment if new update doesn't work
def index(request):
    things = Profile.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })


def specifics(request, slug):
    # grab the object...
    details = Profile.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/specifics.html', {
        'details': details,
    })


def edit_entry(request, slug):

    entry = Profile.objects.get(slug=slug)
    form_class = EntryForms

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('specifics', slug=entry.slug)
    else:
        form = form_class(instance=entry)

    return render(request, 'things/edit_entry.html', {
        'entry': entry,
        'form': form,
    })


