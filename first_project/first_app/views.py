from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm          
 
# Create your views here.

clicked = 1
def index(request) :
  global clicked
  clicked += 1
  my_dict = {'count' : clicked}
  return render(request, 'index.html', my_dict)


def help(request) :
  return render(request, 'help.html')

#def process_form(request) :
 # username = request.GET.get('user')
  #password = request.GET.get('pwd')
  #print(username, password)
  #return render(request, 'forms_renamed.html')

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
      s_name = form.cleaned_data['name']
      s_roll = form.cleaned_data['roll']
      s_degree = form.cleaned_data['degree']        
      s_branch = form.cleaned_data['branch']
      print(s_name)
 
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})



