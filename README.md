
THe spider will crawl data on: https://batdongsan.com.vn/


Dependency:

```
pip install scrapy
pip install scrapy-random-useragent
pip install beautifulsoup4
```

Quick start start:<br>
Open terminal and run following command

```
scrapy crawl bds -o output.json

```

setting.py

```
FEED_EXPORT_ENCODING = 'utf-8' # make output in json become human readable utf-8
# 0 is unlimit
CLOSESPIDER_PAGECOUNT = 0 # limit the number of page crawl
CLOSESPIDER_ITEMCOUNT = 100000 # limit number of item
```

### 'bds' spider
Only crawl summary page. Faster.

Run command: 
```
scrapy crawl bds -o output.json
```

Summary only. <br>
Sample output (JSON lines format)
```
{"body": "Ra mắt 18 lô đẹp nhất boutique shophose dự án Sun Premier Village Hạ Long Bay.+ + Vị trí trung tâm Bãi Cháy, View trực diện vịnh Hạ Long, kỳ quan thiên nhiên thế giới. + + Phù hợp kinh doanh khách sạn mini, nhà hàng, café tại vị trí ngay đầu dự án lối đi Đảo Rều, nơi bất kỳ du khách nào khi tới đều ...", "city": "\r\nHạ Long, Quảng Ninh\r\n", "title": "Cơ hội đầu tư xuất sắc - 18 lô đẹp nhất boutique shophouse dự án Premier Village Hạ Long Bay", "price": "Thỏa thuận", "area": "300 m²", "date": "02/09/2017"}
{"body": "Sở hữu ngay căn hộ Xuân Mai Complex, chỉ với 800 triệu/căn, full nội thất hoàn thiện, giá gốc trực tiếp chủ đầu tư.\r \r Liên hệ phòng KD CĐT: 098.191.5881 - 0919.746.959.\r \r - Chiết khấu trực tiếp 3% và giá gốc HĐMB.\r - Hỗ trợ lãi suất 0% trong vòng 1 năm đến khi nhận nhà.\r - Hỗ trợ vay vốn 70% tổng ...", "city": "\r\nHà Đông, Hà Nội\r\n", "title": "Xuân Mai Complex Dương Nội sở hữu căn hộ chỉ từ 800 triệu,LS 0% nhận ngay lộc vàng.LH: 098.191.5881", "price": "17 triệu/m²", "area": "47 m²", "date": "02/09/2017"}
{"body": "Bán nhà phố liền kề đường xe tải gần chợ Hưng Long, gần trạm y tế xã Hưng Long, gần chợ Bình Điền, giao thông thuận tiện đến bến xe Miền Tây, quận 6,7,8..... Nhà mới xây xong đẹp kiên cố, diện tích từ 40m2 - 70m2 (4mx8m; 4mx12m; 3.7mx10m; 3.8mx11m. 3.5mx16m...), gồm 1 trệt, 1 lầu, 2 phòng ngủ, 1 phò...", "city": "\r\nBình Chánh, Hồ Chí Minh\r\n", "title": "Bán nhà phố liền kề chợ Hưng Long, sổ hồng chính chủ bán giá từ 395 triệu đến 690 triệu", "price": "395 triệu", "area": "40 m²", "date": "02/09/2017"}
{"body": "- Mở bán phố thương mại thượng lưu đẳng cấp giá chỉ từ 336 triệu, hỗ trợ trả trước 50% góp 30 tháng không lãi suất.\r - Đô thị sở hữu KDL sinh thái rộng 15ha kênh DL sinh thái dài 1,7km đầu tiên phía Tây Bắc TP. HCM.\r - Diện tích đa dạng; 4x16m, 4x18m, 5x20m, 8x20m, 10x20m v. V.\r - Thanh toán linh ho...", "city": "\r\nĐức Hòa, Long An\r\n", "title": "- Cát Tường Phú Sinh mở bán khu vipland trả góp dài hạn không % LS. LH 0987583743 - 0936177594 Đạt", "price": "336 triệu", "area": "100 m²", "date": "02/09/2017"}
```

One item
```
{
	"body": "Ra mắt 18 lô đẹp nhất boutique shophose dự án Sun Premier Village Hạ Long Bay.+ + Vị trí trung tâm Bãi Cháy, View trực diện vịnh Hạ Long, kỳ quan thiên nhiên thế giới. + + Phù hợp kinh doanh khách sạn mini, nhà hàng, café tại vị trí ngay đầu dự án lối đi Đảo Rều, nơi bất kỳ du khách nào khi tới đều ...",
	"city": "\r\nHạ Long, Quảng Ninh\r\n",
	"title": "Cơ hội đầu tư xuất sắc - 18 lô đẹp nhất boutique shophouse dự án Premier Village Hạ Long Bay",
	"price": "Thỏa thuận",
	"area": "300 m²",
	"date": "02/09/2017"
}
```

### 'bdsdetail' spider
Click on each link on summary page for detail. Crawl much slower slower.

Command
```
scrapy crawl bdsdetail -o output.jl
```

One item
```
{
	"body": "Cho thuê và Bán chuyển nhượng căn hộ chung cư Times City và Times City Park Hill Mới Nhận Nhà, Các Căn Giá Rẻ Cạnh Tranh trên thị trường từ 100tr đến 800tr, Đã có sổ đỏ và phí dịch vụ 10 năm, vay ngân hàng tới 70% giá trị. Một số căn tính ra giá rất rẻ chỉ khoảng 30tr/m2 ( vd: căn T18 – 3 phòng ngủ ",
	"city": "\r\nHai Bà Trưng, Hà Nội\r\n",
	"title": "Bán chung cư Times City 30tr/m2 và Park HiLL mới nhận, giá rẻ 100tr đến 800tr, đã có sổ đỏ, vay 70%",
	"mobile": "0979229966",
	"price": "2.95 tỷ",
	"area": "95 m²",
	"phone": "0979229966",
	"link": "/ban-can-ho-chung-cu-duong-minh-khai-phuong-minh-khai-prj-times-city/30tr-m2-va-park-hill-moi-nhan-gia-re-100tr-den-800tr-da-co-so-do-vay-70-pr11220477",
	"bodyDetail": "Cho thuê và Bán chuyển nhượng căn hộ chung cư Times City và Times City Park Hill Mới Nhận Nhà, Các Căn Giá Rẻ Cạnh Tranh trên thị trường từ 100tr đến 800tr, Đã có sổ đỏ và phí dịch vụ 10 năm, vay ngân hàng tới 70% giá trị.Một số căn tính ra giá rất rẻ chỉ khoảng 30tr/m2 ( vd: căn T18 – 3 phòng ngủ - 95m2 đã có phí dịch vụ 10 năm, giá 2.95 tỷ )Các căn cho thuê từ ngăn hạn vài ngày đến dài hạn vài năm giá khởi điểm chỉ từ 7.5tr / 1 tháng đến 20tr căn hộ nội thất cao cấpMọi chi tiết Liên Hệ 24/7 Mrs Nga: 0903.060380 - 0979.229966Các căn đang bán:* Tòa từ T1 – T2 .. đến T11 và T18: ( đa phần đã có sổ đỏ và gói miễn phí dịch vụ 10 năm )Căn 1 phòng ngủ - 53m giá từ 1.8 tỷ đến 1.9 tỷCăn 2 phòng ngủ - từ 75m2 đến 108m2 – giá từ 2.55 tỷ đến 3.7 tỷCăn 3 phòng ngủ - căn góc – 110m2 – giá từ 4.050 tỷ đến 4.4 tỷCăn 4 phòng ngủ - Căn góc tòa T11 – 160m2 ( có căn rẻ nhất cắt lỗ đến 800tr so với gốc giá 5.7 tỷ ( view nhạc nước ) - đến 7.5 tỷ căn full nội thất đẹp )-      Tòa T1 – 2 phòng ngủ - 76m2 – tầng cao hướng Nam – giá 2.55 tỷ-      Tòa T2 – 2 phòng ngủ - 94.4m - hướng Bắc nhìn cầu Vĩnh Tuy - đầy đủ nội thất giá 3.1 tỷ-      Tòa T2 – 3 phòng ngủ - 119m2 – hướng Nam – giá 3.9 tỷ-      Tòa T3 - căn góc 2 phòng ngủ - 97.5m2 - nhìn nhạc nước - giá 3.45 tỷ vào thẳng tên hợp đồng.-      Tòa T4 - căn góc 3 phòng ngủ - 110.3m2 - view nhạc nước - giá 4.4 tỷ bao tên sổ đỏ.-      Tòa T4 - 2 phòng ngủ - 75m2 - ban công hướng Bắc - giá 2.6 tỷ.-      Tòa T6 căn 2 phòng ngủ đều sáng, diện tích 87.5m2 hướng Nam giá 3.3 tỷ.-      Tòa T6 căn góc 3 phòng ngủ sáng – 110m – ban công đông Nam – 4.2 tỷ-      Tòa T8 - 2 phòng ngủ, - 83m2 - hướng Bắc - view nhạc nước, cầu Vĩnh Tuy, nhà mới nguyên bản - giá 2.8 tỷ đã có sổ đỏ.-      Tòa T8 – 1 phòng ngủ - 53m2 – hướng Bắc view nhạc nước – 1.83 tỷ-      Tòa T9 - 2 phòng ngủ - 83m2 - hướng Nam - giá 2.7 tỷ.-      Tòa T9 – 1 phòng ngủ - 53m2 – hướng Nam view park hill – 1.8 tỷ-      Tòa T18 – 3 phòng ngủ - 95m2 hướng Đông view cầu Vĩnh Tuy giá 2.95 tỷ-      Tòa T18 – 3 phòng ngủ - 115m2 căn góc view quảng trường giá 4.2 tỷ•\tNhiều căn chuyển nhượng 1PN, 2PN và 3PN của Park Hill vào nhận nhà.: ( mới nhận bàn giao từ 20/11/2016, nhà mới nguyên bản của chủ đầu tư, điều hòa âm trần, v.v.. )Tiện ích: Miễn phí 10 năm dịch vụ, sân chơi thể thao, trung tâm thương mại….Ngoài ra nếu quý khách có nhu cầu mua nhà thanh toán theo tiến độ và hưởng ưu đãi từ chủ đầu tư, hãy liên hệ với chúng tôi để cập nhật bảng giá và chính sách cụ thể.Lưu ý:Trong ngày 28/12 Chủ đầu tư dự án Times City-Park Hill mở bán đợt mới các căn hộ từ 1 đến 4 phòng ngủ với diện tích từ 56.1m2 - 145m2 tại các tòa Park Hill Premium với chính sách siêu ưu đãi dành cho những khách hàng cuối cùng:- Chiết khấu 12% giá trị căn hộ khi khách hàng thanh toán sớm 95% giá trị căn hộ.- Nếu khách hàng không thanh toán sớm, vay ngân hàng sẽ được hỗ trợ vay vốn đến 75% GTCH với lãi suất 0% đến ngày 26/2/2019 (ân hạn nợ gốc trong 24 tháng).- Miễn phí 5 năm đỗ xe dành cho 1 oto hoặc trừ vào giá trị căn hộ 87 triệu.- Những căn nhận bàn giao thô được giảm trừ 4 triệu/m2 thông thủy.Hiện tại giá thuê căn hộ ở Times City đang rất hợp lý với mức giá từ 7.5tr 1 tháng, quý khách sở hữu căn hộ đầy đủ tiện nghi điều hòa, nóng lạnh, bếp từ, … với miễn phí dịch vụ 10 năm và tiện ích miễn phí như bể bơi 4 mùa, thể thao tennis, bóng rổ, cầu lông, …Mọi chi tiết Liên Hệ 24/7 Mrs Nga: 0903.060380 - 0979.229966",
	"contactName": "Mrs Nga",
	"address": "458 Minh Khai, Hai Bà Trưng, Hà Nội",
	"date": "03/09/2017",
	"type": "Bán căn hộ chung cư"
}
```


