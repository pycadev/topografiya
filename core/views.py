from django.shortcuts import render
from django.http import Http404

# Sahifalar ro'yxati
pages = [
    {'num': 1, 'title': "Direksion burchakdan azimutlarga o‘tish quyidagi formulalar yordamida bajariladi.", 'desc': "Direksion burchakdan shimolga nisbatan azimutlarni aniqlash formulalari yordamida hisoblash."},
    {'num': 2, 'title': "Azimutlardan Direksion burchakka o‘tish quyidagi formulalar yordamida bajariladi", 'desc': "Shimoliy yo‘nalishga nisbatan azimutdan yo‘l bo‘ylab direksion burchakni hisoblash usullari."},
    {'num': 3, 'title': "Xaritada masofalarni o‘lchash", 'desc': "Masshtab asosida xaritada berilgan masofani real masofaga aylantirish usuli."},
    {'num': 4, 'title': "Haqiqiy masofa va vaqt sarfi", 'desc': "Yurish tezligi asosida vaqt va masofa o‘rtasidagi bog‘liqlikni hisoblash."},
    {'num': 5, 'title': "Kuzatilayotgan predmetgacha bo‘lgan masofani uning chiziqli o‘lchamlari (bo‘yi, eni, balandligi) va burchak kattaliklari bo‘yicha aniqlash.", 'desc': "Burchak va o‘lchamlar yordamida nishongacha bo‘lgan masofani aniqlash."},
    {'num': 6, 'title': "Predmetning balandligi uning burchak kattaligi bo‘yicha ", 'desc': "Trigonometrik burchaklar asosida predmet balandligini hisoblash formulalari."},
    {'num': 7, 'title': "Predmetning balandligi soya yordamida", 'desc': "Soya uzunligidan foydalangan holda balandlikni aniqlash usuli."},
    {'num': 8, 'title': "Yo‘l korrekturasi ", 'desc': "Haqiqiy yo‘nalishdan og‘ishlarni inobatga olib yo‘lni tuzatish usuli."},
    {'num': 9, 'title': "Xaritadan nuqtalarning o‘zaro ko‘rinishini aniqlash", 'desc': "Topografik chiziqlar asosida ikki nuqta orasidagi ko‘rinish mavjudligini aniqlash."},
    {'num': 10, 'title': "Ko‘rish uzoqligi (km da)", 'desc': "Obyekt balandligi va yerni egriligi hisobga olingan holda ko‘rish masofasini aniqlash."},
    {'num': 11, 'title': "Pana joyning chuqurligini aniqlash", 'desc': "Yuqoridan yoki yon tomondan berilgan ma'lumotlar asosida panajoy chuqurligini hisoblash."},
    {'num': 12, 'title': "Panajoy burchagini aniqlash", 'desc': "Panajoyning burchagini geometrik usullar orqali hisoblash."},
    {'num': 13, 'title': "Nishon o‘rni burchagini aniqlash", 'desc': "Ko‘rsatilgan yo‘nalishlar orqali nishon joylashgan burchakni topish."},
    {'num': 14, 'title': "To‘g‘ri burchakli koordinatalar orqali masofani o‘lchash", 'desc': "X va Y koordinatalari yordamida ikki nuqta orasidagi masofani aniqlash."},
    {'num': 15, 'title': "Uglomer bo‘laklaridan gradus o‘lchoviga o‘tish ", 'desc': "Uglomer bo‘linmalarini gradus ko‘rinishiga konvertatsiya qilish usuli."},
    {'num': 16, 'title': "Tekis to'g'ri burchakli koordinatalar orqali direksin burchakni topish", 'desc': "Koordinatalar farqi asosida direksion burchakni hisoblash."},
    {'num': 17, 'title': "Xaritalarning tasniflanishi, mo‘ljallanishi va geometrik mohiyati.", 'desc': "Xaritani vazifasi, ishlatilish sohasi va tuzilishiga qarab tasniflash."},
    {'num': 18, 'title': "QIYALIK BURCHAGINI ANIQLASH(ko'z bilan)", 'desc': "Vizual baholash asosida qiyalik darajasini taxminiy aniqlash usuli."},
    {'num': 19, 'title': "QIYALIK BURCHAGINI ANIQLASH (qadamlab)", 'desc': "Qadam soni va balandlik o‘zgarishi orqali qiyalik burchagini hisoblash."},
    {'num': 20, 'title': "Mutloq va nisbiy balandliklarni aniqlash.", 'desc': "Birinchi nuqta balandligiga nisbatan nisbiy va mutloq balandlikni hisoblash."},
    {'num': 21, 'title': "Qiyalikni 20°-25° dan oshmagan burchagini aniqlanish formulasi:", 'desc': "Qiyalik burchagini hisoblashda xavfsiz harakatlanish chegarasini belgilash."},
]
# Bosh sahifa
def home(request):
    return render(request, 'core/home.html', {'pages': pages})

# Dinamik sahifa view (1ta umumiy view)
def problem_page(request, num):
    page = next((p for p in pages if p["num"] == num), None)
    if not page:
        raise Http404("Bunday sahifa mavjud emas.")
    return render(request, f'core/index{num}.html', {
        'title': page["title"],
        'desc': page["desc"],
    })
