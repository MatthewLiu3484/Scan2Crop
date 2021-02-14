from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

from .models import *

class PhotoForm(forms.ModelForm):

        image = MultiImageField(min_num=1, max_num=20)


        class Meta:
            model = Post
            fields = ('name',)
            widgets = {'name': forms.HiddenInput()}

        def save(self, commit=True):
            instance = super(PhotoForm, self).save(commit)
            for each in self.cleaned_data['image']:
                Photo.objects.create(image=each, post=instance)

            return instance


