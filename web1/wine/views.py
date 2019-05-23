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
    price = [3.5,1.0,1.5,2.5,1.5,2.0,3.0,1.0]
    RED = "{% static 'wine/red_wine.png' %}"
    ROSE = "{% static 'wine/rose_wine.png' %}"
    WHITE = "{% static 'wine/white_wine.png' %}"
    file_list = [RED, ROSE, ROSE, WHITE, WHITE, RED, RED, RED]
    scripts = ['이 와인은 잔에 따르자마자 블랙베리, 블루베리, 자두 등의 완숙된 검붉은 과실향이 넘실대며 시럽으로 코팅된 체리와 무화과, 크렘 드 까시스 향이 은은하게 피어오릅니다.감초 등의 달콤한 향신료는 토스트, 넛맥 등과 함께 와인에 복합미를 부여하고, 타바코, 모카 등의 다채로운 풍미가 신선한 과실 캐릭터와 함께 매우 조화롭게 어우러집니다. 입에서 느껴지는 구조감 또한 일품으로 풀 바디의 와인을 헤비하게 느껴지지 않게 하는 발란스와 결 좋은 탄닌 느낌이 길고 아름다운 여운으로 마무리됩니다.',
               '달고, 낮은 도수에 가볍게 즐기기 좋은 와인입니다. 자연적인 달콤함과 함께 과일의 향이 밝게 느껴집니다. 이 와인이 가진 상큼함과 신선함이 입안을 즐겁게 만들어 줄 것입니다. 특히, 20대 남녀 중심으로 아주 선호도가 높은 와인입니다.',
               '흑장미, 바이올렛 등의 향기와 함께 부드러우면서도 잘 익은 탄닌과 집중력 있는 탄닌이 느껴집니다. 달콤하지만 우아한 맛이 일품으로 향에서 느껴지던 모든 것들이 입안에 그대로 전달되는 잘 만들어진 와인입니다.',
               '블랙 체리와 커런트, 베리류와 달콤한 오크의 아로마를 느낄 수 있으며, 맛에서는 붉은과일과 검은과일의 조화가 실키한 질감과 함께 길게 지속되는 피니시를 이끌어 냅니다. 아주 조밀하며 부드러운 탄닌과 적절한 산도를 지니고 있으며 입안에 남는 진한 여운은 촉촉한 체리를 연상케 합니다.',
               '복합적 아로마를 지닌 미디엄 바디 와인으로, 블랙 체리, 자두 등 검은 과실 아로마에 시나몬, 라벤더, 코코아 뉘앙스와 약간의 스파이시함 바닐라, 오크 풍미도 느껴집니다. 진한 과실미, 유연하면서도 부드러운 질감이 조화롭게 어우러져 마시기 편하고 다양한 음식과 잘 어우러집니다.',
               '꽉 차 있으나 무겁지 않고 반짝이는 듯한 과실미와 Soft한 탄닌을 자랑하여 남녀의 지지를 골고루 받고 있습니다.\n깊고 아름다운 제비꽃 색을 가진 와인으로 체리와 같은 붉은 열매과일, 초콜릿, 담배향 등을 보입니다. 입에서는 Full-한 느낌을 주면서도, 둥글고 벨벳과 같은 유려한 식감을 줍니다.과실미의 뒤를 이어서 바닐라와 토스트된 느낌이 감돌면서 길고 스무드한 피니쉬를 남기면서 우아하며 따뜻하게 사라집니다.',
               '이 와인은 열매 과일, 블랙커런트, 시가 박스, 바닐라와 민트 향 등이 복합적이며, Fruit과 Oak의 느낌이 하나로 잘 화합하여 부드럽고 우아한 면모를 느낄 수 있습니다. 적당한 무게와 잘 짜여진 구조로 대중적인 선호가 높은 와인입니다.',
               '와인계의 소주같은 느낌, 가성비 좋은 고알콜의 와인입니다. 너무 달지 않은 맛에 과실향과 오크향이 균형이 좋아 데일리 와인으로 마시기 좋습니다.\n산뜻한 산미와 중간 정도의 감미에 청포도 본연의 향긋한 풍미를 그대로 지니고 있어 누구나 쉽게 즐길 수 있는 매력적인 와인입니다.']

    if qv == '0':
        output = dict()

        for idx, wine in enumerate(out):

            if wine == 0:
                continue
                # name, price, title, description, group
            elif group[idx] in output.keys():
                if output[group[idx]][1] > price[idx]:
                    output[group[idx]] = [alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx], scripts[idx]]
            else:
                output[group[idx]] = [alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx], scripts[idx]]

    else:
        output2 = list()
        for idx, wine in enumerate(out):
            if wine == 1:
                output2.append([alphabet[idx], price[idx], title_list[idx], description_list[idx], group[idx], scripts[idx]])

    if qv == '0':
        output2 = output.values()

    return render(request, 'wine/result.html', {'output':output2})
