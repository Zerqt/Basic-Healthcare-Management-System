from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Patient, Supply

# Patient Views
class PatientListView(ListView):
    model = Patient
    template_name = 'healthcare/patient_list.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['name', 'age', 'contact_info', 'medical_condition', 'treatment_notes']
    template_name = 'healthcare/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['name', 'age', 'contact_info', 'medical_condition', 'treatment_notes']
    template_name = 'healthcare/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'healthcare/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')

# Supply Views
class SupplyListView(ListView):
    model = Supply
    template_name = 'healthcare/supply_list.html'

class SupplyCreateView(CreateView):
    model = Supply
    fields = ['name', 'quantity', 'expiry_date']
    template_name = 'healthcare/supply_form.html'
    success_url = reverse_lazy('supply_list')

class SupplyUpdateView(UpdateView):
    model = Supply
    fields = ['name', 'quantity', 'expiry_date']
    template_name = 'healthcare/supply_form.html'
    success_url = reverse_lazy('supply_list')

class SupplyDeleteView(DeleteView):
    model = Supply
    template_name = 'healthcare/supply_confirm_delete.html'
    success_url = reverse_lazy('supply_list')