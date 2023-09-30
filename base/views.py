from django.shortcuts import render
from rest_framework.response import Response
from rest_api_payload import error_response, success_response
from rest_framework import generics
from django.http import HttpRequest, HttpResponse
from rest_framework import status
import uuid
from .serializers import CreateRecordingSerializer, GetRecordingSerializer, GetRecordingVideoSerializer, VideoSerializers
from .models import Recordings, VideoRecordings

# Create your views here.


class CreateRecordingView(generics.CreateAPIView):
    serializer_class = CreateRecordingSerializer
    queryset = Recordings.objects.all()



    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request:HttpRequest):
        serializer = CreateRecordingSerializer(data=request.data)
        name = serializer.initial_data.get("name")
        if serializer.is_valid():
            serializer.save()

            payload = success_response(
                    status="success",
                    message=f"Recording(s) saved successfully!",
                    data=serializer.data
                )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = error_response(
                status="Failed something went wrong",
                message=serializer.errors
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)

class AllRecordingsView(generics.ListAPIView):
    serializer_class = GetRecordingSerializer
    queryset = Recordings.objects.all()

    def get(self, request:HttpRequest):
        
        recordings = self.get_queryset()
        serializers = self.serializer_class(recordings, many=True)
        payload = success_response(
            status="success",
            message=f"All recordings fetched successfully!",
            data=serializers.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)  
        
class VideoRecordingsView(generics.ListAPIView):
    serializer_class = GetRecordingVideoSerializer

    def get(self, request:HttpRequest, id:int):
        try:
            recording = Recordings.objects.get(id=id)
            videos = VideoRecordings.objects.filter(recording=recording)
            serializers = GetRecordingVideoSerializer(instance={'recording': recording, 'videos': videos}, many=False)
            payload = success_response(
                status="success",
                message=f"Videos for recording {recording.name} fetched successfully!",
                data=serializers.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        except Recordings.DoesNotExist:
            payload = error_response(
                status="Failed, something went wrong", 
                message=f"Recording does not exist"
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        
class SingleVideoView(generics.ListAPIView):
    serializer_class = VideoSerializers

    def get(self, request:HttpRequest, id:int):
        try:
            video = VideoRecordings.objects.get(id=id)
            serializers = VideoSerializers(video, many=False)
            payload = success_response(
                status="success",
                message=f"Video fetched successfully!",
                data=serializers.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        except VideoRecordings.DoesNotExist:
            payload = error_response(
                status="Failed, something went wrong", 
                message=f"Video does not exist"
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)