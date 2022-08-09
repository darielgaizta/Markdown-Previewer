from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method == 'POST':
		markdown = request.POST['markdown']
		return render(request, 'index.html', {'markdown':markdown})
	return render(request, 'index.html')