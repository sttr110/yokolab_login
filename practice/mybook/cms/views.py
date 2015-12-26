from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from cms.forms import BookForm
from cms.models import Book




###index####
def book_list(request):
  books = Book.objects.all().order_by('id')
  return render_to_response('cms/book_list.html',
                            {'books': books},
                            context_instance=RequestContext(request))

### create edit ####
def book_edit(request, book_id=None):
  if book_id:
    book = get_object_or_404(Book, pk=book_id)
  else:
    book = Book()

  if request.method == 'POST':
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
      book = form.save(commit=False)
      book.save()
      return redirect('cms:book_list')
  else:
    form = BookForm(instance=book)
    
  return render_to_response('cms/book_edit.html',
                            dict(form=form, book_id=book_id),
                            context_instance=RequestContext(request))

###delete####
def book_del(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  book.delete()
  return redirect('cms:book_list')
 

###impressons_show####
def impressions_show(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  impressions = book.impressions.all()
  return render_to_response('cms/impression/impressions_show.html',
                            {'impressions': impressions},
                            context_instance=RequestContext(request))

