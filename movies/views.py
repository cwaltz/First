from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FilmsForm
from .models import Films, Places

# Create your views here.

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FilmsForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			film_list = Films.objects.filter(title=request.POST['title'])
			context = {'film_list': film_list}
			return render(request, 'movies/result.html', context)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = FilmsForm()

	return render(request, 'movies/index.html', {'form': form})
