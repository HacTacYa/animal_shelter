from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Adoption
from .forms import AnimalForm, AdoptionForm

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animals/animal_detail.html', {'animal': animal})

def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animals/animal_form.html', {'form': form})

def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animals/animal_form.html', {'form': form})

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')
    return render(request, 'animals/animal_confirm_delete.html', {'animal': animal})