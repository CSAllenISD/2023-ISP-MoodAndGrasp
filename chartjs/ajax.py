from dajaxice.utils import deserialize_form
from chartjs.form import SurveyForm
from dajax.core import Dajax
from chartjs.models import *

@dajaxice_register
def send_form(request, form):
   dajax = Dajax()
   form = SurveyForm(deserialize_form(form))
   
   if form.is_valid():
      dajax.remove_css_class('#my_form input', 'error')
      dr = Student.objects.get(user=self.request.user)
      dr.Mood = form.cleaned_data.get('Mood')
      dr.Grasp = form.cleaned_data.get('Grasp')
      dr.save()
      
      dajax.alert("Student Entry %s was successfully saved.")
   else:
      dajax.remove_css_class('#my_form input', 'error')
      for error in form.errors:
         dajax.add_css_class('#id_%s' % error, 'error')
			
   return dajax.json()
