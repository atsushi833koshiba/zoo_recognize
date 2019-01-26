from PIL import Image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sklearn.externals import joblib
import numpy as np
import cv2
import chainer
import chainer.links as L
import chainer.functions as F
from . import googlenetmodel, image_manager
from .models import AnimalInfo



g_model = L.Classifier(googlenetmodel.GoogleNet())
chainer.serializers.load_npz('model_zoo.npz',g_model)

unknown_animal_id = 999


def index(request):
    return render(request, 'zoo_app/index.html', {})


def zoo(request):
    return render(request, 'zoo_app/zoo.html', {})


def recognizeImage(request):

    if request.method == 'POST':
        print('POST')
        try:
            animals = []
            base64_imgs = []
            probas = []
            #files = request.FILES['file']
            files = request.FILES.getlist('file')
            for file in files:
                np.random.seed(seed=0)
                imgObj =Image.open(file)
                nar = np.array(imgObj)
                img = cv2.resize(nar,(224,224))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) ## GRAY変換
                img = img.transpose(2,0,1) ## channel width height変換
                img = img.astype('f') ## float32変換
                print(img.shape)

                y = g_model.predictor(np.array([img], 'f'))
                y = F.softmax(y)
                y_proba = y.data
                y = y.array
                result = np.argmax(y, axis=1)
                animal_id = int(result)
                print('result',animal_id)

                # proba算出
                y_pre = np.argmax(y_proba, axis=1)[0]
                proba = round(y_proba[0][y_pre] * 100, 2)
                probas.append(proba)

                print('proba',proba)
                is_display = True;
                base64_imgs.append(image_manager.createBase64Image(imgObj))
                animal = AnimalInfo.objects.filter(animal_id=animal_id)

                if animal.exists():
                    animals.append(animal[0])
                else:
                    animals.append(AnimalInfo.objects.filter(animal_id=unknown_animal_id)[0])

            allList = zip(animals, base64_imgs, probas)
            return render(request, 'zoo_app/zoo.html',
            {'is_display':is_display,'allList':allList})

        except Exception as e:
            print(e,'error')

        return render(request, 'zoo_app/zoo.html', {})
    else:
        return render(request, 'zoo_app/zoo.html', {})
