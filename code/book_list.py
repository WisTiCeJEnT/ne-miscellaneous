import requests as rq
import time
import json
s = """
<a href="/t/books/english-books">English Books</a>
        <li><a href="/t/books/english-books/animals-and-pets">Animals and Pets</a></li>
        <li><a href="/t/books/english-books/art-and-design">Art and Design</a></li>
        <li><a href="/t/books/english-books/biography">Biography</a></li>
        <li><a href="/t/books/english-books/business-and-economics">Business and Economics</a></li>
        <li><a href="/t/books/english-books/childrens-books">Children&#39;s Books</a></li>
        <li><a href="/t/books/english-books/comics-and-graphic-novels">Comics and Graphic Novels</a></li>
        <li><a href="/t/books/english-books/computers-and-internet">Computers and Internet</a></li>
        <li><a href="/t/books/english-books/english-as-a-foreign-language">English as a Foreign Language</a></li>
        <li><a href="/t/books/english-books/family-and-relationships">Family and Relationships</a></li>
        <li><a href="/t/books/english-books/food-and-drink">Food and Drink</a></li>
        <li><a href="/t/books/english-books/health-and-well-being">Health and Well-Being</a></li>
        <li><a href="/t/books/english-books/history-and-politics">History and Politics</a></li>
        <li><a href="/t/books/english-books/hobbies-and-collectibles">Hobbies and Collectibles</a></li>
        <li><a href="/t/books/english-books/languages">Languages</a></li>
        <li><a href="/t/books/english-books/literature-and-fiction">Literature and Fiction</a></li>
        <li><a href="/t/books/english-books/military-and-war">Military and War</a></li>
        <li><a href="/t/books/english-books/new-age">New Age</a></li>
        <li><a href="/t/books/english-books/performing-arts">Performing Arts</a></li>
        <li><a href="/t/books/english-books/philosophy-and-psychology">Philosophy and Psychology</a></li>
        <li><a href="/t/books/english-books/religion">Religion</a></li>
        <li><a href="/t/books/english-books/science">Science</a></li>
        <li><a href="/t/books/english-books/self-enrichment">Self-Enrichment</a></li>
        <li><a href="/t/books/english-books/social-science">Social Science</a></li>
        <li><a href="/t/books/english-books/sports">Sports</a></li>
        <li><a href="/t/books/english-books/study-guide">Study Guide</a></li>
        <li><a href="/t/books/english-books/travel">Travel</a></li>
        <li><a href="/t/books/english-books/young-adult">Young Adult</a></li>
<a href="/t/books/chinese-books">Chinese Books</a>
        <li><a href="/t/books/chinese-books/wen-xue">文学</a></li>
        <li><a href="/t/books/chinese-books/man-hua">漫画</a></li>
        <li><a href="/t/books/chinese-books/sheng-huo-shi-shang">生活时尚</a></li>
        <li><a href="/t/books/chinese-books/xin-li-li-zhi">心理励志</a></li>
        <li><a href="/t/books/chinese-books/qi-ye-guan-li">企业管理</a></li>
        <li><a href="/t/books/chinese-books/lu-you">旅游</a></li>
        <li><a href="/t/books/chinese-books/yu-yan-star-ci-shu">语言·辞书</a></li>
        <li><a href="/t/books/chinese-books/yi-zhu">艺术</a></li>
        <li><a href="/t/books/chinese-books/shi-pu-star-yin-liao">食谱·饮料</a></li>
        <li><a href="/t/books/chinese-books/zong-jiao">宗教</a></li>
        <li><a href="/t/books/chinese-books/ming-li-shu-zhu">命理数术</a></li>
        <li><a href="/t/books/chinese-books/li-shi">历史</a></li>
        <li><a href="/t/books/chinese-books/zhe-xue-star-xin-li-xue">哲学·心理学</a></li>
        <li><a href="/t/books/chinese-books/she-hui-ke-xue">社会科学</a></li>
        <li><a href="/t/books/chinese-books/dian-nao">电脑</a></li>
        <li><a href="/t/books/chinese-books/ke-xue">科学</a></li>
        <li><a href="/t/books/chinese-books/ti-yu-yun-dong">体育运动</a></li>
        <li><a href="/t/books/chinese-books/qi-ta">其他</a></li>
        <li><a href="/t/books/chinese-books/er-tong-du-wu">儿童读物</a></li>
        <li><a href="/t/books/chinese-books/qin-zi-jiao-yu-star-jia-ting-star-qin-zi-guan-xi">亲子教育·家庭·亲子关系</a></li>
<a href="/t/books/japanese-books">Japanese Books</a>
        <li><a href="/t/books/japanese-books/wen-ku-xin-shu">文庫・新書</a></li>
        <li><a href="/t/books/japanese-books/komituku">コミック</a></li>
        <li><a href="/t/books/japanese-books/wen-yun">文芸</a></li>
        <li><a href="/t/books/japanese-books/bizinesu">ビジネス</a></li>
        <li><a href="/t/books/japanese-books/ren-wen-she-hui">人文・社会</a></li>
        <li><a href="/t/books/japanese-books/qu-wei-shi-yong">趣味・実用</a></li>
        <li><a href="/t/books/japanese-books/yun-shu">芸術</a></li>
        <li><a href="/t/books/japanese-books/konpiyutazi-ran-ke-xue">コンピュータ・自然科学</a></li>
        <li><a href="/t/books/japanese-books/yu-xue-ci-shu">語学・辞書</a></li>
        <li><a href="/t/books/japanese-books/xue-xi-can-kao-shu">学習参考書</a></li>
        <li><a href="/t/books/japanese-books/er-tong-shu">児童書</a></li>
        <li><a href="/t/books/japanese-books/lu-xing-shu">旅行書</a></li>
<a href="/t/books/thai-books">Thai Books</a>
        <li><a href="/t/books/thai-books/obraanwatthuaelakhngsasm">โบราณวัตถุและของสะสม</a></li>
        <li><a href="/t/books/thai-books/kaarcchadkaaraelakaarbrihaarthurkicch">การจัดการและการบริหารธุรกิจ</a></li>
        <li><a href="/t/books/thai-books/edkaelaeyaawchn">เด็กและเยาวชน</a></li>
        <li><a href="/t/books/thai-books/kaartuun">การ์ตูน</a></li>
        <li><a href="/t/books/thai-books/khmphiwetr">คอมพิวเตอร์</a></li>
        <li><a href="/t/books/thai-books/aahaaraelaekhruuengduuem">อาหารและเครื่องดื่ม</a></li>
        <li><a href="/t/books/thai-books/khrbkhrawaelakhwaamsamphanth">ครอบครัวและความสัมพันธ์</a></li>
        <li><a href="/t/books/thai-books/prawatisaastraelakaaremuueng">ประวัติศาสตร์และการเมือง</a></li>
        <li><a href="/t/books/thai-books/sukhphaaph">สุขภาพ</a></li>
        <li><a href="/t/books/thai-books/phaasaaaelaphaasaasaastr">ภาษาและภาษาศาสตร์</a></li>
        <li><a href="/t/books/thai-books/wrrnkrrm">วรรณกรรม</a></li>
        <li><a href="/t/books/thai-books/saarabanethingaelasilpa">สาระบันเทิงและศิลปะ</a></li>
        <li><a href="/t/books/thai-books/prachyaaaelasaasnaa">ปรัชญาและศาสนา</a></li>
        <li><a href="/t/books/thai-books/lueklabaelaohraasaastr">ลึกลับและโหราศาสตร์</a></li>
        <li><a href="/t/books/thai-books/phuuechaelasatw">พืชและสัตว์</a></li>
        <li><a href="/t/books/thai-books/cchitwithyaaaelakaarphathnaatneng">จิตวิทยาและการพัฒนาตนเอง</a></li>
        <li><a href="/t/books/thai-books/hnangsuue%60aangingaelaphcchnaanukrm">หนังสืออ้างอิงและพจนานุกรม</a></li>
        <li><a href="/t/books/thai-books/withyaasaastr">วิทยาศาสตร์</a></li>
        <li><a href="/t/books/thai-books/kiilaa">กีฬา</a></li>
        <li><a href="/t/books/thai-books/sangkhmsaastr">สังคมศาสตร์</a></li>
        <li><a href="/t/books/thai-books/thngethiiyw">ท่องเที่ยว</a></li>
"""

l = s.split("\n")
l = [line.strip() for line in l]
book = {}
cat = ""
for line in l:
    if line == "":
        continue
    if(line[:2] == "<a"):
        book[line[line.index('>')+1:-4]] = {}
        cat = line[line.index('>')+1:-4]
    else:
        book[cat][line[line.index('">')+2:-9]] = []
print(json.dumps(book, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))