from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Adoption, Employee, Feed, Account, Donation
from .forms import AnimalForm, AdoptionForm, EmployeeForm, FeedForm, AccountForm, DonationForm
from django.http import HttpResponse

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})


def animal_add(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animals/animal_add.html', {'form': form})

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

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds/feed_list.html', {'feeds': feeds})

def feed_detail(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    return render(request, 'feeds/feed_detail.html', {'feed': feed})

def feed_create(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed_list')
    else:
        form = FeedForm()
    return render(request, 'feeds/feed_form.html', {'form': form})

def feed_update(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    if request.method == 'POST':
        form = FeedForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return redirect('feed_detail', pk=pk)
    else:
        form = FeedForm(instance=feed)
    return render(request, 'feeds/feed_form.html', {'form': form})

def feed_delete(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    if request.method == 'POST':
        feed.delete()
        return redirect('feed_list')
    return render(request, 'feeds/feed_confirm_delete.html', {'feed': feed})

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'accounts/account_detail.html', {'account': account})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'accounts/account_form.html', {'form': form})

def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_detail', pk=pk)
    else:
        form = AccountForm(instance=account)
    
    return render(request, 'accounts/account_form.html', {'form': form})


def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'accounts/account_confirm_delete.html', {'account': account})

def account_donation_create(request, pk):
    account = get_object_or_404(Account, pk=pk)
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.account = account  # Привязываем пожертвование к счету
            donation.save()
            account.total_donations += donation.amount  # Обновляем общую сумму пожертвований на счету
            account.save()
            return redirect('account_detail', pk=pk)
    else:
        form = DonationForm()
    
    return render(request, 'accounts/account_donation_form.html', {'form': form, 'account': account})

def account_donation_delete(request, account_pk, donation_pk):
    account = get_object_or_404(Account, pk=account_pk)
    donation = get_object_or_404(Donation, pk=donation_pk)
    
    if request.method == 'POST':
        account.total_donations -= donation.amount
        account.save()
        donation.delete()
        return redirect('account_detail', pk=account_pk)
    
    return render(request, 'accounts/account_donation_confirm_delete.html', {'account': account, 'donation': donation})

def index(request):
    return HttpResponse("Привет, мир! Это мой первый Django проект.")

