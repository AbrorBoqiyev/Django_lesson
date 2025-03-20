from django.shortcuts import render
from django.http import HttpResponse


def myapp_view(request):
    html = """
        <h1>Main page</h1>
        <p>Bu asosiy bo'lim</p>
        <a href="second"> Second page >> </a><br>
        <a href="pages/computers"> Kompyuterlar bo'limi >> </a><br>
        <a href="pages/telephones"> Telefonlar bo'limi >> </a>
    """
    return HttpResponse(html)


def second_page(request):
    html = """
        <h1>This is the Second page</h1>
        <a href="../"> << Main page </a>
    """
    return HttpResponse(html)


def pages(request, page):
    if page == "computers":
        html = f"""
            <h1> Kompyuterlar </h1>
            <p> 
                Kompyuter (inglizcha: computer – ,,kodlar bilan ishlamayman'') – oldindan berilgan dastur boʻyicha ishlaydigan avtomatik qurilma. Elektron hisoblash mashinasi (EHM) bilan bir xildagi atama. Biroq, kompyuter hisoblash ishlarini bajarishdan tashqari uning funksiyasi ancha keng. EHMlarning rivojlanishida kompyuterning bir necha avlodlarini koʻrsatish mumkin. Bu avlodlar element turlari, konstruktiv-texnologik xususiyatlari, mantiqiy tuzilishi, dastur taʼminoti, texnik tafsilotlari, texnikadan foydalanishning qulaylik darajasi bilan bir-biridan farq qiladi. Kompyuterning dastlabki avlodida (Ural-1, Minsk-2, BSEM-2) asosiy element elektron lampa boʻlgani uchun u juda katta joyni egallagan edi. Soʻngra bu lampa oʻrnida tranzistorlar ishlatilgan kompyuter (Razdan-2, M-220, Minsk-22 va boshqalar), integral mikrosxemalar ishlatilgan kompyuter (IBM-360, 1BM-370, (AQSh), YESEVM (Rossiya) va boshqalar, integratsiya darajasi katta boʻlgan integral sxemalar oʻrnatilgan shaxsiy kompyuterlar paydo boʻldi. Shaxsiy kompyuter (mikro va mikro EHM) tushunchasi XX asr 70-yillar oxiridan boshlab keng tarqala boshladi. Shaxsiy kompyuterning keyingi avlodlarida mikroelektron va biosxemalardan foydalanildi; ularning hajmi kitob kattaligidek hajmga kichraydi, massasi esa 3,5 kg gacha kamaydi. 1981-yil IBM shirkati shaxsiy kompyuterning yanada takomillashgan modellarini ishlab chiqara boshladi.            
            </p>
            <img
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Personal_computer%2C_exploded_4.svg/220px-Personal_computer%2C_exploded_4.svg.png',
                width='200'
            ></br>
            <a href=".."> Main page </a>
        """
    elif page == "telephones":
        html = f"""
            <h1> Telefonlar </h1>
            <p> 
                Telefon — tovush uzatish va qabul qilish uchun moʻljallangan telekommunikatsiyalar qurilmasidir. Odatda, tovushning mexanik energiyasini elektrik signallar energiyasiga aylantirish, masofadan uzatish va uni qaytadan tovushga aylantirish prinsipi bilan ishlaydi.
                Telefon (tele... olis va fon un = olisun) — 1) elektr signallarini tovush signallariga aylantirib beradigan elektrakustik asbob. Elektromagnitli, elektrodinamik va pyezoelektr turlariga bo'linadi. Elektromagnitli T. eng keng tarqalgan bo`lib, uning asosiy elementlari doimiy magnit, chulgʻamli qutblar va membranadan iborat. Abonent "telefon qilganida" T. signalining oʻzgaruvchan elektr toki taʼsirida membrana tebranib, tovush hosil qiladi. T. telefon apparati, turli radiotexnika asboblari va boshqa qurilmalarda ishlatiladi; 2) telefon apparatining qisqa nomi; 3) telefon aloqasining qisqa nomi.
            </p>
            <img 
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/ATTtelephone-large.jpg/222px-ATTtelephone-large.jpg",
                width="200"
            ><br>
            <a href=".."> Main page </a>
        """
    else:
        html = f"""
            <h1> Page {page} </h1>
            <h3> Bu {page} bo'limi </h3>
            <a href=".."> Main page </a>
        """
    return HttpResponse(html)