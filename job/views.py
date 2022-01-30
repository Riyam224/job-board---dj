from django.shortcuts import render , get_object_or_404 , redirect

# Create your views here.
from django.core.paginator import Paginator
from .models import Job , Category
from .forms import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

def job_list(request):
	jobs = Job.objects.all()
     
    # filter before paginator
	## filters

	myfilter = JobFilter(request.GET, queryset=jobs)
	jobs = myfilter.qs
  


	# paginator
	paginator = Paginator(jobs ,3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {'jobs' :page_obj ,
		
		 'myfilter' : myfilter}
   
	return render(request , 'job/job_list.html' , context)



def job_details(request , slug):
	job = get_object_or_404(Job , slug=slug)

	if request.method == 'POST':
		form = ApplyForm(request.POST , request.FILES)
		if form.is_valid():
			myform = form.save(commit=False)
			myform.job = job
			myform.save()
			print('done')
	
	form = ApplyForm()
	

	context = {

	    'job': job,
		'form': form,
		
	}

	return render(request , 'job/job_details.html' , context)




@login_required
def add_job(request):
	if request.method == 'POST':
		form = JobForm(request.POST , request.FILES)
		if form.is_valid():
			myform = form.save(commit=False)
			# add field owner that not add it in form in 
			myform.owner = request.user
			myform.save()
			# return redirect('job:job_list')
			return redirect(reverse('job:job_list'))
		    
	
	form = JobForm()

	context = {
		'form': form
	}
	return render(request , 'job/add_job.html' , context)
