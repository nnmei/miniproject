CREATE TABLE `losts` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `detail` varchar(500) NOT NULL,
  `coverimage` varchar(100) NOT NULL,
  `latitude` decimal(11,7) NOT NULL,
  `longitude` decimal(11,7) NOT NULL
);

INSERT INTO `losts` (`id`, `name`, `detail`, `coverimage`, `latitude`, `longitude`) VALUES
(1, 'แพนเค้ก', 'แมว พันธุ์ไทย สีขาว', 'https://www.melivecode.com/attractions/1.jpg', '7.7376190', '98.7068755'),
(2, 'แดง', 'แมว เปอร์เซีย สีส้ม', 'https://www.melivecode.com/attractions/2.jpg', '48.8583736', '2.2922926'),
(3, 'นปโป๊ะ', 'สุนัข ลายวัว', 'https://www.melivecode.com/attractions/3.jpg', '40.7589652', '-73.9893574'),
(4, 'วันใหม่', 'แมว ขี้อ้อน อายุ 2 เดือน', 'https://www.melivecode.com/attractions/4.jpg', '35.3606422', '138.7186086'),
(5, 'มะลิ', 'สุนัข ไซบีเรียน ขาวล้วน', 'https://www.melivecode.com/attractions/5.jpg', '51.5007325', '-0.1268141');

ALTER TABLE `losts`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `losts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

CREATE TABLE `founds` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `detail` varchar(500) NOT NULL,
  `coverimage` varchar(100) NOT NULL,
  `latitude` decimal(11,7) NOT NULL,
  `longitude` decimal(11,7) NOT NULL
);

INSERT INTO `founds` (`id`, `name`, `detail`, `coverimage`, `latitude`, `longitude`) VALUES
(1, 'ปีโป้', 'แมว พันธุ์ไทย', 'https://www.melivecode.com/attractions/1.jpg', '7.7376190', '98.7068755'),
(2, 'ไม่รู้', 'แมว สีเปรอะ', 'https://www.melivecode.com/attractions/2.jpg', '48.8583736', '2.2922926'),
(3, 'ไม่แน่ใจ', 'สุนัข ลายวัว', 'https://www.melivecode.com/attractions/3.jpg', '40.7589652', '-73.9893574'),
(4, 'ปลาทู', 'แมว สีส้ม', 'https://www.melivecode.com/attractions/4.jpg', '35.3606422', '138.7186086'),
(5, 'ไม่รู้', 'สุนัข สีดำ', 'https://www.melivecode.com/attractions/5.jpg', '51.5007325', '-0.1268141');

ALTER TABLE `founds`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `founds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;