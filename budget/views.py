from django.shortcuts import render,redirect
from django.views.generic import View
from budget.models import Transaction
from django import forms
# Create your views here.
class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        exclude=("created_date",)
        # fields = "__all__"      // all fields
        # fields = ["field1","field2",]

  

# View for listing all transactions
# url localhost:8000/transactions/all/
#  method : get
class TransactionListView(View):
    def get(self,request,*args,**kwargs):
        qs=Transaction.objects.all()
        return render(request,"transaction_list.html",{"data":qs})
    

# View for creating a new transaction
# url localhost:8000/transactions/add/
#  method : get,post
class TransactionCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TransactionForm()
        return render(request,"transaction_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transaction-list")
        else:
            return render(request,"transaction_add.html",{"form":form})

# View for transaction detail
# url localhost:8000/transactions/{id}/
#  method : get
class TransactionDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Transaction.objects.get(id=id)
        return render(request,"transaction_detail.html",{"data":qs})
    