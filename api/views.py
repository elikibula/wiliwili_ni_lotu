from html5lib import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datahub.models import DatahubLewenilotu
from .serializers import DatahubLewenilotuSerializer

@api_view(['GET'])
def getData(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    serializer = DatahubLewenilotuSerializer(DatahubLewenilotus, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	DatahubLewenilotus = DatahubLewenilotu.objects.get(id=pk)
	serializer = DatahubLewenilotuSerializer(DatahubLewenilotus, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = DatahubLewenilotuSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	DatahubLewenilotus = DatahubLewenilotu.objects.get(id=pk)
	serializer = DatahubLewenilotuSerializer(instance=DatahubLewenilotus, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	DatahubLewenilotus = DatahubLewenilotu.objects.get(id=pk)
	DatahubLewenilotus.delete()

	return Response('Item succsesfully delete!')