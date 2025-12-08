from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Count

from .models import JobPost, Applicant
from .serializers import JobPostSerializer, ApplicantSerializer


@api_view(['POST'])
def create_job(request):
    serializer = JobPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_jobs(request):
    jobs = JobPost.objects.all()
    serializer = JobPostSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def apply_job(request):
    email = request.data.get('email')
    today = timezone.now().date()

    count = Applicant.objects.filter(
        email=email,
        applied_at__date=today
    ).count()

    if count >= 3:
        return Response(
            {"error": "You can apply to only 3 jobs per day"},
            status=status.HTTP_429_TOO_MANY_REQUESTS
        )

    serializer = ApplicantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def job_summary(request):
    jobs = JobPost.objects.annotate(
        applicant_count=Count('applicants')
    ).order_by('-applicant_count')

    data = []
    for job in jobs:
        data.append({
            "id": job.id,
            "title": job.title,
            "location": job.location,
            "posted_by": job.posted_by,
            "applicant_count": job.applicant_count
        })

    return Response(data)

