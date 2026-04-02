from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import User, Query, QueryResponse
from .serializers import QuerySerializer, QueryResponseSerializer


def assign_query(query):

    support_members = User.objects.filter(role="support")

    support = support_members.annotate(
        total_queries=Count('assigned_queries')
    ).order_by('total_queries').first()

    if support:
        query.assigned_to = support
        query.status = "assigned"
        query.assigned_at = timezone.now()
        query.save()

    return query


def check_escalation():

    queries = Query.objects.filter(status="assigned")

    for q in queries:

        if q.assigned_at:

            time_passed = timezone.now() - q.assigned_at

            if time_passed > timedelta(hours=2):

                q.status = "escalated"
                q.save()


class QueryViewsets(viewsets.ModelViewSet):

    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def create(self, request, *args, **kwargs):

        serializer = QuerySerializer(data=request.data)

        if serializer.is_valid():
            query = serializer.save()

            assign_query(query)

            return Response(QuerySerializer(query).data, status=201 )

        return Response(serializer.errors, status=400)


class ResponseViewsets(viewsets.ModelViewSet):

    queryset = QueryResponse.objects.all()
    serializer_class = QueryResponseSerializer

    def perform_create(self, serializer):

        response = serializer.save(responder=self.request.user)

        query = response.query
        query.status = "resolved"
        query.save()