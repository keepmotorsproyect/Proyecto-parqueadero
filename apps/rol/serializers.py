from rest_framework import serializers
from .models import *


<<<<<<< HEAD
class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = ('__all__')
=======
class rolSerializer(serializers.ModelSerializer):

    class Meta:
        model = rol
        fields = ('__all__')
>>>>>>> e6c33c2472c76b9bf7f602194754eb756a8f30ba
