-- MySQL dump 10.13  Distrib 5.7.26, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.7.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contents`
--
create database test;
use test;


DROP TABLE IF EXISTS `contents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contents`
--

LOCK TABLES `contents` WRITE;
/*!40000 ALTER TABLE `contents` DISABLE KEYS */;
INSERT INTO `contents` VALUES (1,'基础疾病','( 基础疾病：主要指三大类疾病。一是有基础代谢障碍，如内分泌失调、糖尿病；二是免疫功能低下：如艾滋病；三是有重大的慢性消耗性疾病：如肿瘤，高血压。',''),(15,'慢性胃炎','(概念]慢性胃炎系;指不同病因引起的各种慢性胃粘膜炎性病变。现已明确幽门螺旋杆菌感染为慢性胃炎的最主要的病因。但其他物理性、化学性及生物性有害因素长期反复作用于易感人体也可引起本病。病因持续存在或反复发生即可形成慢性病变\r\n[症状]慢性胃炎最常见的症状是上腹疼痛和饱胀，或其他消化道症状，如暖气、吞酸、烧心、恶心、呕吐、食欲不振、腹泻等。此外，出血也是慢性胃炎的症状之一，尤其是合并糜烂。腹时比较舒适，饭后不适，进食虽不多但觉过饱。常因冷食、硬食、辛辣或其他刺激性食物引起或加重症状。这些症状用抗酸药及解疼药不易缓解。另外，可伴随贫血症状\r\n','基础代谢障碍'),(18,'感冒','百姓所说的感冒是指“普通感冒”，又称“伤风”、急性鼻炎或上呼吸道感染。感冒是一种常见的急性上呼吸道病毒性感染性疾病，多由鼻病毒、副流感病毒、呼吸道合胞病毒、埃可病毒、柯萨奇病毒、冠状病毒、腺病毒等引起。临床表现为鼻塞、喷嚏、流涕、发热、咳嗽、头痛等，多呈自限性。大多散发，冬、春季节多发，季节交替时多发。','免疫功能低下'),(19,'免疫功能低下','消化性溃疡主要指发生于胃和十二指肠的慢性溃疡，是一多发病、常见病。溃疡的形成有各种因素，其中酸性胃液对黏膜的消化作用是溃疡形成的基本因素，因此得名。酸性胃液接触的任何部位，如食管下段、胃肠吻合术后吻合口、空肠以及具有异位胃黏膜的Meckel憩室。','免疫功能低下');
/*!40000 ALTER TABLE `contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friend`
--

DROP TABLE IF EXISTS `friend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `userid2` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friend`
--

LOCK TABLES `friend` WRITE;
/*!40000 ALTER TABLE `friend` DISABLE KEYS */;
INSERT INTO `friend` VALUES (15,27,26);
/*!40000 ALTER TABLE `friend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remain`
--

DROP TABLE IF EXISTS `remain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `remain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remain` varchar(5000) NOT NULL,
  `speekid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remain`
--

LOCK TABLES `remain` WRITE;
/*!40000 ALTER TABLE `remain` DISABLE KEYS */;
INSERT INTO `remain` VALUES (6,'hello',11,25,'2023-03-31 05:23:32'),(7,'嗯，请问该如何避免呢',12,27,'2023-03-31 05:30:12'),(8,'你好，我加了你的好友',11,27,'2023-03-31 05:30:40'),(9,'你好哦',13,30,'2023-06-10 14:49:22');
/*!40000 ALTER TABLE `remain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speak`
--

DROP TABLE IF EXISTS `speak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `speak` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(5000) NOT NULL,
  `date` datetime NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speak`
--

LOCK TABLES `speak` WRITE;
/*!40000 ALTER TABLE `speak` DISABLE KEYS */;
INSERT INTO `speak` VALUES (11,'hello my name is 往事','2023-03-31 05:23:01',25),(12,'慢性胃炎系;指不同病因引起的各种慢性胃粘膜炎性病变。现已明确幽门螺旋杆菌感染为慢性胃炎的最主要的病因。但其他物理性、化学性及生物性有害因素长期反复作用于易感人体也可引起本病。病因持续存在或反复发生即可形成慢性病变','2023-03-31 05:28:00',26),(13,'我认识了一个新朋友','2023-03-31 05:29:40',27),(14,'请问头痛怎么办','2023-06-10 14:43:47',29),(15,'我来了','2023-06-10 14:48:48',30);
/*!40000 ALTER TABLE `speak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authority` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `nick` varchar(20) DEFAULT NULL,
  `head` varchar(100) DEFAULT 'default.webp',
  `sex` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (21,0,'9ce62c6','qwe123','admin','default.webp',1),(22,0,'18c958d','qwe123','admin','default.webp',1),(23,0,'737019f','qwe123','admin','default.webp',1),(24,0,'d7fd15e','qqqqqq','q','default.webp',1),(25,0,'62329ae','qwe123','往事','1680211367.5541291微信图片_20221214174028.jpg',0),(26,0,'2199e57','qwe123','往事','1680211652.627365微信图片_20221214174028.jpg',0),(27,0,'3ec13e5','qwe123','成员2','default.webp',0),(28,0,'09c4c7b','qwe123','admin','1680249171.607264微信图片_20221214174028.jpg',1),(29,0,'3da10a0','123123','test','1686379399.9158692R-C.jpg',1),(30,0,'784c441','123123','hello','1686379709.785434R-C.jpg',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-10 15:09:19
