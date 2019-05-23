from django.shortcuts import render
from .recommendation2 import recommend
import time

def index(request):
    return render(request, 'wine/index.html')
# Create your views here.

def result(request):
    # raw_data needs to be a string type input

    sex = request.POST.get('gender')
    age = request.POST.get('age')
    marriage = request.POST.get('marriage')
    job = request.POST.get('job')
    qv = request.POST.get('qv')

    out = str(sex) + str(age) + str(marriage) + str(job)

    out = recommend(out)

    title_list = ['강력하고 우아한 A', '맛도 가격도 쏘 스윗 B', '분위기있는 달콤함 C', '달콤쌉사름 D', '파인 다이닝을 위한 E',
                  '사랑하는 이들과 함께 F', '누구나 좋아할만한 G', '와인계의 쏘주 H']

    description_list = ['구매력있는 당신을 위한 깊이있는 비즈니스 와인', '가성비 좋은 저알콜 스위트 와인, 젊은 남녀들이 특히 좋아해요',
                        '고생한 당신을 위한 스위트 선물', '달달하게 취하고 싶은 날에는', '균형감있는 맛, 행복한 저녁을 위한 와인',
                        '누군가와 함께 달달한 시간을 보내고 싶다면', '와인 비기너라면 이 와인 한 번 어때요', '마음은 무거우나 지갑은 가벼운 날']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    group = [1,2,2,3,3,1,1,1]
    price = [1.0,1.0,1.5,2.5,1.5,2.0,3.0,1.0]
    RED = "{% static 'wine/red_wine.png' %}"
    ROSE = "{% static 'wine/rose_wine.png' %}"
    WHITE = "{% static 'wine/white_wine.png' %}"
    file_list = [RED, ROSE, ROSE, WHITE, WHITE, RED, RED, RED]


    if qv == '0':
        output = dict()

        for idx, wine in enumerate(out):

            if wine == 0:
                continue
                # name, price, title, description, group
            elif group[idx] in output.keys():
                if output[group[idx]][1] > price[idx]:
                    output[group[idx]] = [alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx]]
            else:
                output[group[idx]] = [alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx]]

    else:
        output2 = list()
        for idx, wine in enumerate(out):
            if wine == 0:
                output2.append([alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx]])

    if qv == '0':
        output2 = output.values()

    return render(request, 'wine/result.html', {'output':output2})