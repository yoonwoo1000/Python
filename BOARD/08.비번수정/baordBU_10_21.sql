-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: boardEX
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `board`
--

DROP TABLE IF EXISTS `board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `board` (
  `bIDX` int NOT NULL AUTO_INCREMENT COMMENT '게시글번호',
  `bTitle` varchar(255) NOT NULL COMMENT '제목',
  `bContent` text NOT NULL COMMENT '내용',
  `bType` varchar(2) NOT NULL COMMENT '게시판종류 : fb, nb',
  `wDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '작성일자',
  `mDate` datetime DEFAULT NULL COMMENT '수정일자',
  `hits` int DEFAULT '0' COMMENT '조회수',
  `uIDX` int NOT NULL COMMENT '작성자회원번호',
  PRIMARY KEY (`bIDX`),
  KEY `uIDX` (`uIDX`),
  CONSTRAINT `board_ibfk_1` FOREIGN KEY (`uIDX`) REFERENCES `userlist` (`uIDX`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='게시글목록';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board`
--

LOCK TABLES `board` WRITE;
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT INTO `board` VALUES (1,'첫번째 게시글입니다','내용내용내용','fb','2025-10-15 12:06:47',NULL,3,1),(3,'두번째 게시글입니다','내용내용내용','fb','2025-10-15 12:15:04',NULL,4,2),(4,'세번째 게시글입니다','내용내용내용','fb','2025-10-15 12:15:19',NULL,0,4),(5,'[필독] 커뮤니티 이용 규칙 안내','안녕하세요. 커뮤니티를 이용하실 때 지켜주셔야 할 규칙들을 안내드립니다.\n\n1. 타인에 대한 비방, 욕설은 금지됩니다.\n2. 상업적 광고는 삭제 조치됩니다.\n3. 불법 정보 공유 시 법적 책임을 지실 수 있습니다.\n\n모두가 즐거운 커뮤니티를 만들어주세요.','nb','2024-01-05 10:00:00',NULL,324,1),(6,'2024년 1월 정기 점검 안내','서비스 안정화를 위한 정기 점검이 진행됩니다.\n\n점검 일시: 2024년 1월 10일 오전 2시 ~ 6시\n점검 내용: 데이터베이스 최적화, 보안 업데이트\n\n점검 중에는 서비스 이용이 제한될 수 있습니다.','nb','2024-01-08 15:30:00',NULL,156,1),(7,'신규 기능 업데이트 안내','다음 주 목요일, 새로운 기능들이 추가됩니다!\n\n- 게시글 임시저장 기능\n- 댓글 좋아요 기능\n- 다크모드 지원\n\n많은 이용 부탁드립니다.','nb','2024-01-12 14:20:00',NULL,293,1),(8,'개인정보 처리방침 개정 안내','개인정보 보호법 개정에 따라 당사 개인정보 처리방침이 변경됩니다.\n\n시행일: 2024년 2월 1일\n주요 변경사항: 정보 보유기간, 제3자 제공 내역\n\n자세한 내용은 공지사항을 참고해주세요.','nb','2024-01-18 11:00:00',NULL,100,1),(9,'[이벤트] 설날 맞이 출석 이벤트','설날을 맞아 출석 이벤트를 진행합니다!\n\n기간: 2024년 2월 5일 ~ 2월 15일\n보상: 매일 출석 시 포인트 적립\n\n많은 참여 바랍니다!','nb','2024-01-25 10:30:00',NULL,413,1),(10,'회원 등급제 도입 안내','활동에 따라 회원 등급이 부여됩니다.\n\n등급: 새싹 → 일반 → 우수 → VIP\n혜택: 등급별 포인트 적립률 차등\n\n열심히 활동해주세요!','nb','2024-01-30 16:00:00','2025-10-16 15:57:08',210,1),(11,'2024년 2월 정기 점검 완료','정기 점검이 성공적으로 완료되었습니다.\n\n주요 작업 내역:\n- 서버 성능 개선\n- 버그 수정\n- 보안 패치 적용\n\n원활한 서비스 이용이 가능합니다.','nb','2024-02-07 07:00:00',NULL,87,1),(12,'[긴급] 일시적 접속 장애 복구 완료','오늘 오전 발생한 접속 장애가 복구되었습니다.\n\n장애 시간: 09:00 ~ 09:45\n원인: 트래픽 급증\n조치: 서버 증설\n\n불편을 드려 죄송합니다.','nb','2024-02-09 10:30:00',NULL,267,1),(13,'모바일 앱 출시 예정 안내','커뮤니티 모바일 앱이 3월에 출시됩니다!\n\nOS: Android, iOS\n주요 기능: 푸시 알림, 빠른 댓글 작성\n\n베타 테스터를 모집할 예정이니 많은 관심 부탁드립니다.','nb','2024-02-14 13:00:00',NULL,345,1),(14,'오늘 날씨 정말 좋네요!','아침부터 햇살이 따뜻해서 기분이 좋습니다.\n산책하기 딱 좋은 날씨인 것 같아요.\n\n여러분도 좋은 하루 보내세요!','fb','2024-01-10 08:30:00',NULL,45,2),(15,'맛있는 파스타 레시피 공유합니다','어제 만든 크림 파스타가 정말 맛있어서 레시피를 공유합니다.\n\n재료: 스파게티면, 생크림, 베이컨, 마늘, 파마산 치즈\n\n1. 면을 삶는다\n2. 베이컨과 마늘을 볶는다\n3. 생크림을 넣고 졸인다\n4. 면과 함께 볶고 치즈를 뿌린다\n\n간단하지만 맛있어요!','fb','2024-01-12 19:45:00',NULL,128,3),(16,'주말에 등산 가실 분?','이번 주말에 북한산 등산 계획 중입니다.\n\n일시: 1월 14일(일) 오전 9시\n집합 장소: 북한산 입구\n\n함께 가실 분 댓글 남겨주세요!','fb','2024-01-11 14:20:00',NULL,67,4),(17,'노트북 구매 추천 부탁드립니다','대학생인데 노트북을 새로 사려고 합니다.\n\n용도: 문서 작업, 동영상 편집\n예산: 100만원 내외\n\n추천해주시면 감사하겠습니다!','fb','2024-01-15 16:00:00',NULL,93,5),(18,'오늘 본 영화 후기','어제 개봉한 액션 영화를 봤는데 정말 재미있었어요!\n\nCG도 화려하고 스토리도 탄탄했습니다.\n배우들 연기도 훌륭했구요.\n\n강력 추천합니다!','fb','2024-01-16 21:30:00',NULL,156,6),(19,'퇴근 후 운동 루틴 공유','헬스장 3개월째 다니고 있는데 효과가 있는 것 같아요.\n\n루틴:\n- 월수금: 웨이트 트레이닝\n- 화목: 유산소 운동\n- 주말: 휴식\n\n꾸준히 하는 게 중요한 것 같습니다.','fb','2024-01-18 22:00:00',NULL,84,7),(20,'고양이 키우시는 분들께 질문','처음 고양이를 입양했는데 잘 적응을 못하는 것 같아요.\n\n숨어만 있고 밥도 잘 안먹네요.\n어떻게 하면 좋을까요?','fb','2024-01-20 11:30:00',NULL,113,2),(21,'강남 맛집 추천해주세요','다음 주에 강남에서 친구 만나기로 했는데\n좋은 식당 있으면 추천 부탁드립니다.\n\n한식이면 더 좋겠습니다!','fb','2024-01-22 15:45:00',NULL,76,3),(22,'취미로 시작한 그림 그리기','3개월 전부터 유튜브 보면서 그림 연습 중입니다.\n\n처음에는 선 긋기도 힘들었는데\n이제는 간단한 캐릭터 정도는 그릴 수 있어요.\n\n취미 생활 정말 좋네요!','fb','2024-01-24 18:20:00',NULL,134,4),(23,'겨울 여행지 추천 부탁드려요','2월에 2박 3일로 국내 여행 가려고 합니다.\n\n겨울에 가기 좋은 곳 있을까요?\n눈 구경하고 온천도 즐기고 싶습니다.','fb','2024-01-26 13:00:00',NULL,98,5),(24,'오늘 아침에 만든 샌드위치','재료가 많이 없어서 간단하게 만들었는데\n의외로 맛있더라구요.\n\n통밀빵, 계란, 치즈, 토마토\n건강한 한 끼 식사 완성!','fb','2024-01-28 09:15:00',NULL,54,6),(25,'책 추천 받습니다','요즘 독서에 빠져있는데\n추천할만한 소설 있으면 알려주세요.\n\n장르는 상관없습니다!','fb','2024-01-30 20:00:00',NULL,89,7),(26,'이직 고민 중입니다','현재 직장에서 3년째 근무 중인데\n이직을 고민하고 있습니다.\n\n연봉은 오르는데 업무가 너무 반복적이에요.\n여러분이라면 어떻게 하시겠어요?','fb','2024-02-01 17:30:00',NULL,167,2),(27,'피아노 배우고 싶은데','30대인데 피아노를 배워보고 싶습니다.\n\n너무 늦은 나이일까요?\n성인 취미반 다니시는 분 계신가요?','fb','2024-02-03 14:00:00',NULL,121,3),(28,'점심 메뉴 추천 좀...','매일 점심 메뉴 고르는 게 너무 힘드네요.\n\n여러분은 오늘 뭐 드셨나요?\n추천 좀 부탁드립니다!','fb','2024-02-05 12:00:00',NULL,73,4),(29,'재택근무 장단점','회사에서 재택근무를 시작한 지 한 달 됐습니다.\n\n장점: 출퇴근 시간 절약, 편한 복장\n단점: 집중력 저하, 운동 부족\n\n여러분은 어떠신가요?','fb','2024-02-07 16:30:00',NULL,145,5),(30,'최근 넷플릭스 추천작','요즘 넷플릭스에서 재미있게 본 드라마 추천합니다.\n\n스토리 전개가 빠르고 연기가 훌륭해요.\n주말에 정주행 각입니다!','fb','2024-02-09 19:00:00',NULL,198,6),(31,'새벽 러닝 시작했어요','오늘부터 새벽 러닝을 시작했습니다.\n\n아침 공기가 정말 상쾌하네요.\n건강해지는 느낌이에요!','fb','2024-02-11 06:30:00',NULL,67,7),(32,'핸드드립 커피 입문','집에서 커피를 내려 마시기 시작했습니다.\n\n원두 선택부터 물 온도까지\n신경 쓸 게 많지만 재미있어요.\n\n카페 부럽지 않아요!','fb','2024-02-13 10:00:00',NULL,112,2),(33,'혼자 여행 다녀왔어요','처음으로 혼자 제주도 여행을 다녀왔습니다.\n\n처음엔 걱정했는데 정말 자유롭더라구요.\n제 속도에 맞춰 여행할 수 있어서 좋았어요.','fb','2024-02-15 22:00:00',NULL,188,3);
/*!40000 ALTER TABLE `board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `boardlist`
--

DROP TABLE IF EXISTS `boardlist`;
/*!50001 DROP VIEW IF EXISTS `boardlist`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `boardlist` AS SELECT 
 1 AS `bIDX`,
 1 AS `bTitle`,
 1 AS `uName`,
 1 AS `wDate`,
 1 AS `hits`,
 1 AS `reply_count`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `replys`
--

DROP TABLE IF EXISTS `replys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `replys` (
  `rIDX` int NOT NULL AUTO_INCREMENT COMMENT '댓글번호',
  `rText` varchar(255) NOT NULL COMMENT '댓글내용',
  `wDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '작성일자',
  `bIDX` int NOT NULL COMMENT '게시글번호',
  `uIDX` int NOT NULL COMMENT '댓글작성회원번호',
  PRIMARY KEY (`rIDX`),
  KEY `uIDX` (`uIDX`),
  KEY `bIDX` (`bIDX`),
  CONSTRAINT `replys_ibfk_1` FOREIGN KEY (`uIDX`) REFERENCES `userlist` (`uIDX`),
  CONSTRAINT `replys_ibfk_2` FOREIGN KEY (`bIDX`) REFERENCES `board` (`bIDX`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='댓글목록';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replys`
--

LOCK TABLES `replys` WRITE;
/*!40000 ALTER TABLE `replys` DISABLE KEYS */;
INSERT INTO `replys` VALUES (10,'4번글, 댓글1','2025-10-15 15:20:28',4,3),(11,'4번글, 댓글2','2025-10-15 15:20:28',4,4),(12,'4번글, 댓글3','2025-10-15 15:20:28',4,2),(13,'8번글, 댓글1','2025-10-15 15:20:28',8,6),(14,'8번글, 댓글2','2025-10-15 15:20:28',8,4),(15,'8번글, 댓글3','2025-10-15 15:20:28',8,2),(16,'10번글, 댓글1','2025-10-15 15:20:28',10,2),(17,'10번글, 댓글2','2025-10-15 15:20:28',10,2),(18,'10번글, 댓글3','2025-10-15 15:20:28',10,5),(19,'10번글, 댓글4','2025-10-15 15:20:28',10,7),(20,'10번글, 댓글5','2025-10-15 15:20:28',10,3),(21,'10번글, 댓글6','2025-10-15 15:20:28',10,2),(22,'10번글, 댓글7','2025-10-15 15:20:28',10,1);
/*!40000 ALTER TABLE `replys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlist`
--

DROP TABLE IF EXISTS `userlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userlist` (
  `uIDX` int NOT NULL AUTO_INCREMENT COMMENT '회원번호',
  `uName` varchar(30) NOT NULL COMMENT '회원성명',
  `uID` varchar(30) NOT NULL COMMENT '아이디',
  `uPW` varchar(30) NOT NULL COMMENT '비밀번호',
  `uEmail` varchar(64) NOT NULL COMMENT '회원이메일',
  `joinDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '가입일자',
  `level` char(1) NOT NULL DEFAULT 'U' COMMENT '회원등급 : U, A, D',
  `isActivate` tinyint(1) NOT NULL DEFAULT '1' COMMENT '활성상태',
  PRIMARY KEY (`uIDX`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='회원목록';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlist`
--

LOCK TABLES `userlist` WRITE;
/*!40000 ALTER TABLE `userlist` DISABLE KEYS */;
INSERT INTO `userlist` VALUES (1,'홍길동','honggd','ezen','honggd@example.com','2024-01-03 00:00:00','A',1),(2,'전우치','junwoo','ezen','ezen@ezen.com','2024-01-08 00:00:00','A',0),(3,'임꺽정','imkj','pw$im789','imkj@example.com','2024-01-15 00:00:00','U',1),(4,'성춘향','seongch','pw$sc012','ezen@ezen.com','2024-01-20 00:00:00','U',0),(5,'이몽룡','leemr','pw$lm345','ezen@ezen.com','2024-01-25 00:00:00','U',0),(6,'콩쥐','kongj','pw$kj678','ezen@ezen.com','2025-10-15 11:03:36','U',0),(7,'팥쥐','patj','pw$pj901','patj@example.com','2025-10-15 11:03:36','A',1),(11,'홍길동','honggildong','hongpw','hong@ezen.com','2025-10-16 17:12:22','U',1),(12,'이젠11','ezen11','1234','ezen11@ezen.com','2025-10-20 09:50:47','U',1),(13,'이젠','ezen','1234','ezen@ezen.com','2025-10-20 10:03:37','U',1),(14,'이젠2','ezen2','1234','ezen2@ezen.com','2025-10-20 11:03:36','U',1),(15,'이젠','ezen3','1234','ezen@ezen.co.kr','2025-10-21 14:39:09','U',1);
/*!40000 ALTER TABLE `userlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uIDX` int NOT NULL AUTO_INCREMENT COMMENT '회원번호',
  `uName` varchar(30) NOT NULL COMMENT '회원성명',
  `uID` varchar(30) NOT NULL COMMENT '아이디',
  `uPW` varchar(32) NOT NULL COMMENT '비밀번호',
  PRIMARY KEY (`uIDX`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='회원목록';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'팥쥐','ezen','8caa00964ae95ccfe3cffd0d631fb39e'),(2,'콩쥐','kong','dfc8f6e990da95b88ca8df3b577a68b0');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `boardlist`
--

/*!50001 DROP VIEW IF EXISTS `boardlist`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = euckr */;
/*!50001 SET character_set_results     = euckr */;
/*!50001 SET collation_connection      = euckr_korean_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `boardlist` AS select `b`.`bIDX` AS `bIDX`,`b`.`bTitle` AS `bTitle`,`u`.`uName` AS `uName`,`b`.`wDate` AS `wDate`,`b`.`hits` AS `hits`,count(`r`.`rIDX`) AS `reply_count` from ((`board` `b` left join `userlist` `u` on((`b`.`uIDX` = `u`.`uIDX`))) left join `replys` `r` on((`b`.`bIDX` = `r`.`bIDX`))) group by `b`.`bIDX`,`b`.`bTitle`,`u`.`uName`,`b`.`wDate`,`b`.`hits` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-21 17:24:12
