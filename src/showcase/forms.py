from django import forms
from .models import Product,Item

class ProductForm(forms.ModelForm):

    items_count = forms.IntegerField()

    def save(self, commit=True):
        
        items_count = self.cleaned_data.get('items_count', None)
        # ...do something with extra_field here...
        a = super(ProductForm, self).save(commit=commit)
        commit = True
        if commit :
            a.save()


        item_objects = []
        for i in range(items_count):
            item_objects.append(Item(product_id = a.id))

        foos = Item.objects.bulk_create(item_objects)
        

        return a

    class Meta:
        model = Product
        fields = '__all__' 