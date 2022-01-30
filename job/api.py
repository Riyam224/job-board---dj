from .serializers  import JobSerializer

from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def joblistapi(request):
    # all the jobs 
    all_jobs = Job.objects.all()
    # convert to json 
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def job_details_api(request, id):
    job_detail = Job.objects.get(id=id)
    # convert to json 
    data = JobSerializer(job_detail).data
    return Response({'data': data})

# generic views 

class JobListView(generics.ListCreateAPIView):
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [IsAdminUser]


class JobDetailsApi(generics.RetrieveUpdateDestroyAPIView):

    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'