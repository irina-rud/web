from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from post.forms import SearchForm
from .models import Post

class PostList(ListView):
	template_name = "post/post_list.html"
	model = Post

class PostView(DetailView):
	model = Post
	template_name = 'post/post.html'
	context_object_name = 'post'

def search_form(request):
	res = None
	if request.method == 'GET':
		form = SearchForm(request.GET)
		if form.is_valid():
			res = Post.objects.filter(sign = form.cleaned_data['query'])
	else:
		form = SearchForm()

	return render(request, 'search-form.html', {'form': form, 'res': res})
