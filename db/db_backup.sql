-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: ELI_ELECTRICAL
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `circuits`
--

DROP TABLE IF EXISTS `circuits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `circuits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `ref` text,
  `total_center` int DEFAULT NULL,
  `total_current_ct` decimal(6,2) DEFAULT NULL,
  `total_length_ct` varchar(25) DEFAULT NULL,
  `total_active_power_ct` decimal(6,2) DEFAULT NULL,
  `total_reactive_power_ct` decimal(6,2) DEFAULT NULL,
  `total_apparent_power_ct` decimal(6,2) DEFAULT NULL,
  `total_fp` decimal(6,2) DEFAULT NULL,
  `name_impedance` varchar(255) DEFAULT NULL,
  `elect_differencial` varchar(45) DEFAULT NULL,
  `secctionmm2` decimal(6,2) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `wires` varchar(255) DEFAULT NULL,
  `current_by_method` decimal(5,2) DEFAULT NULL,
  `type_circuit` varchar(255) DEFAULT NULL,
  `vp` decimal(6,2) DEFAULT NULL,
  `single_voltage` decimal(4,3) DEFAULT NULL,
  `current_r` decimal(6,2) DEFAULT NULL,
  `current_s` decimal(6,2) DEFAULT NULL,
  `current_t` decimal(6,2) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `breakers` varchar(255) DEFAULT NULL,
  `conduit` varchar(45) DEFAULT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tg_id` int NOT NULL,
  `td_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_loads_tgs1_idx` (`tg_id`),
  KEY `fk_loads_tds1_idx` (`td_id`),
  CONSTRAINT `fk_loads_tds1` FOREIGN KEY (`td_id`) REFERENCES `tds` (`id`),
  CONSTRAINT `fk_loads_tgs1` FOREIGN KEY (`tg_id`) REFERENCES `tgs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `circuits`
--

LOCK TABLES `circuits` WRITE;
/*!40000 ALTER TABLE `circuits` DISABLE KEYS */;
INSERT INTO `circuits` VALUES (23,'1','Oficina',6,10.05,'50',2.10,-0.69,2.21,0.95,'capacitance','2X25 30mA',5.26,'a2','RZ1-K',35.00,'feeder',3.44,0.220,10.05,NULL,NULL,'2024-05-23 23:34:41','1X16 \'C\' 10KA','32','2024-05-23 23:34:41',3,NULL),(24,'2','Cocina',1,5.18,'20',3.00,1.18,3.41,0.88,'inductance','4X25 300mA',1.50,'a2','RV',17.00,'subfeeder',1.24,0.380,5.18,5.18,5.18,'2024-06-07 17:44:33','3X10 \'C\' 10KA','25','2024-06-07 17:44:33',3,NULL),(25,'3','Taller',4,20.92,'36.5',8.98,0.17,9.94,0.90,'capacitance','4X40 300mA',3.31,'b1','THHN',33.00,'feeder',4.15,0.380,20.92,20.92,20.92,'2024-06-07 17:46:54','3X32 \'C\' 10KA','40','2024-06-07 17:46:54',3,NULL),(26,'4','Ascensor',4,22.03,'40',11.60,6.48,14.50,0.80,'inductance','4X40 300mA',4.00,'a2','RV-K',30.00,'subfeeder',3.97,0.380,22.03,22.03,22.03,'2024-06-07 18:00:11','3X32 \'C\' 10KA','40','2024-06-07 18:00:11',3,NULL),(27,'5','Bodega',2,9.57,'30',2.00,-0.66,2.11,0.95,'capacitance','2X25 30mA',2.50,'b1','H07Z1',28.00,'feeder',4.13,0.220,NULL,9.57,NULL,'2024-06-07 18:02:11','1X16 \'C\' 10KA','20','2024-06-07 18:02:11',3,NULL),(28,'6','Presurizacion',2,13.51,'50',8.00,2.81,8.89,0.90,'inductance','4X25 300mA',3.31,'a2','H07Z1',17.00,'subfeeder',3.67,0.380,13.51,13.51,13.51,'2024-06-07 18:05:42','3X20 \'C\' 10KA','40','2024-06-07 18:05:42',3,NULL),(29,'7','Taller 2',5,20.30,'55',8.94,4.00,10.54,0.85,'inductance','4X25 300mA',5.26,'a2','RZ1-K',35.00,'subfeeder',3.82,0.380,20.30,20.30,20.30,'2024-06-07 18:07:36','3X25 \'C\' 10KA','40','2024-06-07 18:07:36',3,NULL),(30,'8','Duchas',3,12.78,'40',2.67,-0.88,2.81,0.95,'capacitance','2X25 30mA',5.26,'a1','RV-K',37.00,'subfeeder',3.50,0.220,NULL,NULL,12.78,'2024-06-07 18:12:32','1X16 \'C\' 10KA','32','2024-06-07 18:12:32',3,NULL),(32,'9','Portones de acceso',4,19.14,'40',4.00,-1.31,4.21,0.95,'capacitance','2X25 30mA',8.37,'b1','H07V',59.00,'subfeeder',3.29,0.220,19.14,NULL,NULL,'2024-06-07 18:17:13','1X25 \'C\' 10KA','32','2024-06-07 18:17:13',3,NULL),(33,'10','Sala de bombas',4,18.44,'40',10.80,4.02,12.13,0.89,'inductance','4X25 300mA',3.31,'a2','RZ1',26.00,'subfeeder',4.01,0.380,18.44,18.44,18.44,'2024-06-07 18:22:30','3X25 \'C\' 10KA','40','2024-06-07 18:22:30',3,NULL),(34,'11','Cortinas metalicas',4,21.66,'50',12.40,5.14,14.25,0.87,'inductance','4X40 300mA',5.26,'b1','RZ1-K',28.00,'feeder',3.71,0.380,21.66,21.66,21.66,'2024-06-07 18:25:28','3X32 \'C\' 10KA','40','2024-06-07 18:25:28',3,NULL),(35,'12','Parking',4,14.86,'37.9',8.80,-4.26,9.78,0.90,'capacitance','4X25 300mA',2.50,'e','H07Z1',23.00,'subfeeder',4.05,0.380,14.86,14.86,14.86,'2024-06-07 18:57:41','3X20 \'C\' 10KA','32','2024-06-07 18:57:41',3,NULL),(36,'13','Piscina',1,9.78,'20',2.00,0.79,2.15,0.93,'inductance','2X25 30mA',2.50,'b1','RV-K',28.00,'subfeeder',2.82,0.220,NULL,9.78,NULL,'2024-06-07 18:58:43','1X16 \'C\' 10KA','20','2024-06-07 18:58:43',3,NULL),(38,'1','Baños',2,19.14,'40',4.00,-1.31,4.21,0.95,'capacitance','2X25 30mA',8.37,'a2','RV',46.00,'feeder',3.29,0.220,19.14,NULL,NULL,'2024-06-10 21:30:54','1X25 \'C\' 10KA','32','2024-06-10 21:30:54',3,3),(39,'2','Taller',2,13.12,'20',7.60,2.99,8.64,0.88,'inductance','4X25 300mA',1.50,'a2','RV',17.00,'feeder',3.15,0.380,13.12,13.12,13.12,'2024-06-10 21:49:30','3X20 \'C\' 10KA','25','2024-06-10 21:49:30',3,3),(40,'16','Oficinas',12,6.32,'50',1.32,-0.43,1.39,0.95,'capacitance','2X25 30mA',3.31,'a2','H07Z1',26.00,'feeder',3.44,0.220,6.32,NULL,NULL,'2024-06-12 09:21:00','1X10 \'C\' 10KA','25','2024-06-12 09:21:00',3,NULL),(41,'3','Casa Vecino',20,1.73,'50',1.00,0.39,1.14,0.88,'inductance','4X25 300mA',1.50,'b1','RV-K',20.00,'feeder',1.04,0.380,1.73,1.73,1.73,'2024-06-14 09:26:54','3X6 \'C\' 10KA','25','2024-06-14 09:26:54',3,3),(42,'4','Techumbre',4,2.73,'15',1.62,-0.78,1.80,0.90,'capacitance','4X25 300mA',1.50,'a2','RV',17.00,'subfeeder',0.49,0.380,2.73,2.73,2.73,'2024-06-14 19:03:07','3X6 \'C\' 10KA','25','2024-06-14 19:03:07',3,3);
/*!40000 ALTER TABLE `circuits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conduits`
--

DROP TABLE IF EXISTS `conduits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conduits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nameconduit` varchar(255) DEFAULT NULL,
  `c1` int DEFAULT NULL,
  `c2` int DEFAULT NULL,
  `c3` int DEFAULT NULL,
  `c4` int DEFAULT NULL,
  `c5` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conduits`
--

LOCK TABLES `conduits` WRITE;
/*!40000 ALTER TABLE `conduits` DISABLE KEYS */;
INSERT INTO `conduits` VALUES (1,'1.5',16,16,16,20,25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'2.5',16,20,20,32,32,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'4',16,25,25,32,40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'6',16,25,32,32,40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'10',20,32,32,40,50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'16',25,32,40,50,50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'25',25,40,50,50,63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'35',32,40,50,63,63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,'50',32,50,63,63,75,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,'70',40,50,63,75,75,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(11,'95',40,63,75,100,100,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(12,'120',50,63,75,100,100,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(13,'150',50,75,100,100,125,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(14,'185',63,75,100,125,125,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(15,'240',63,100,125,125,150,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `conduits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conduitsubte`
--

DROP TABLE IF EXISTS `conduitsubte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conduitsubte` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `namesubte` varchar(255) DEFAULT NULL,
  `c1` int DEFAULT NULL,
  `c2` int DEFAULT NULL,
  `c3` int DEFAULT NULL,
  `c4` int DEFAULT NULL,
  `c5` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conduitsubte`
--

LOCK TABLES `conduitsubte` WRITE;
/*!40000 ALTER TABLE `conduitsubte` DISABLE KEYS */;
INSERT INTO `conduitsubte` VALUES (1,'1.5',25,25,25,32,32,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'2.5',25,25,32,32,40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'4',25,32,40,40,40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'6',32,32,50,50,50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'10',40,50,63,63,63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'16',50,50,63,63,63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'25',63,63,75,75,75,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'35',63,75,75,90,90,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,'50',75,75,90,90,110,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,'70',90,90,110,110,110,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(11,'95',110,110,110,140,140,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(12,'120',140,140,160,160,160,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(13,'150',160,160,180,180,180,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(14,'185',180,180,180,180,200,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(15,'240',225,225,225,225,250,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `conduitsubte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `update_at` datetime DEFAULT NULL,
  `proyect_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_jobs_users1_idx` (`user_id`),
  KEY `fk_jobs_proyects2_idx` (`proyect_id`),
  CONSTRAINT `fk_jobs_proyects2` FOREIGN KEY (`proyect_id`) REFERENCES `proyects` (`id`),
  CONSTRAINT `fk_jobs_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loads`
--

DROP TABLE IF EXISTS `loads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loads` (
  `id` int NOT NULL AUTO_INCREMENT,
  `qty` int DEFAULT NULL,
  `active_power` decimal(6,2) DEFAULT NULL,
  `total_active_power` decimal(6,2) DEFAULT NULL,
  `total_reactive_power` decimal(6,2) DEFAULT NULL,
  `total_apparent_power` decimal(6,2) DEFAULT NULL,
  `voltage` decimal(4,3) DEFAULT NULL,
  `fp` decimal(6,2) DEFAULT NULL,
  `total_current` decimal(6,2) DEFAULT NULL,
  `length` varchar(45) DEFAULT NULL,
  `nameloads` varchar(255) DEFAULT NULL,
  `impedance` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `circuit_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_loads_circuits1_idx` (`circuit_id`),
  CONSTRAINT `fk_loads_circuits1` FOREIGN KEY (`circuit_id`) REFERENCES `circuits` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loads`
--

LOCK TABLES `loads` WRITE;
/*!40000 ALTER TABLE `loads` DISABLE KEYS */;
INSERT INTO `loads` VALUES (21,6,350.00,2.10,-0.69,2.21,0.220,0.95,10.05,'50','Computador','capacitance','2024-05-23 23:34:41','2024-05-23 23:34:41',23),(22,1,3000.00,3.00,1.18,3.41,0.380,0.88,5.18,'20','Calenfont','inductance','2024-06-07 17:44:33','2024-06-07 17:44:33',24),(23,2,1990.00,3.98,1.81,4.68,0.380,0.85,7.11,'11.50','Motor azul','inductance','2024-06-07 17:46:55','2024-06-07 17:46:55',25),(24,2,2500.00,5.00,-1.64,5.26,0.220,0.95,13.81,'25','Fresadora','capacitance','2024-06-07 17:47:45','2024-06-07 17:47:45',25),(25,4,2900.00,11.60,6.48,14.50,0.380,0.80,22.03,'40','Cabinas','inductance','2024-06-07 18:00:11','2024-06-07 18:00:11',26),(26,2,1000.00,2.00,-0.66,2.11,0.220,0.95,9.57,'30','Computadores','capacitance','2024-06-07 18:02:11','2024-06-07 18:02:11',27),(27,2,4000.00,8.00,2.81,8.89,0.380,0.90,13.51,'50','Motores','inductance','2024-06-07 18:05:42','2024-06-07 18:05:42',28),(28,3,1780.00,5.34,2.98,6.67,0.380,0.80,10.14,'25','Compresor','inductance','2024-06-07 18:07:36','2024-06-07 18:07:36',29),(29,2,1800.00,3.60,1.02,3.87,0.220,0.93,10.16,'30','Motor 4','inductance','2024-06-07 18:10:32','2024-06-07 18:10:32',29),(30,3,890.00,2.67,-0.88,2.81,0.220,0.95,12.78,'40','Termoelectrico','capacitance','2024-06-07 18:12:32','2024-06-07 18:12:32',30),(32,4,1000.00,4.00,-1.31,4.21,0.220,0.95,19.14,'40','Chapa electrica','capacitance','2024-06-07 18:17:13','2024-06-07 18:17:13',32),(33,4,2700.00,10.80,4.02,12.13,0.380,0.89,18.44,'40','Bombas de agua','inductance','2024-06-07 18:22:30','2024-06-07 18:22:30',33),(34,4,3100.00,12.40,5.14,14.25,0.380,0.87,21.66,'50','Motor cortinas','inductance','2024-06-07 18:25:28','2024-06-07 18:25:28',34),(35,4,2200.00,8.80,-4.26,9.78,0.380,0.90,14.86,'37.90','Cobradores electricos','capacitance','2024-06-07 18:57:41','2024-06-07 18:57:41',35),(36,1,2000.00,2.00,0.79,2.15,0.220,0.93,9.78,'20','Bomba piscina','inductance','2024-06-07 18:58:43','2024-06-07 18:58:43',36),(38,2,2000.00,4.00,-1.31,4.21,0.220,0.95,19.14,'40','Calenfot','capacitance','2024-06-10 21:30:54','2024-06-10 21:30:54',38),(39,2,3800.00,7.60,2.99,8.64,0.380,0.88,13.12,'20','Motor trifasico','inductance','2024-06-10 21:49:30','2024-06-10 21:49:30',39),(40,12,110.00,1.32,-0.43,1.39,0.220,0.95,6.32,'50','Computadores','capacitance','2024-06-12 09:21:01','2024-06-12 09:21:01',40),(41,20,50.00,1.00,0.39,1.14,0.380,0.88,1.73,'50','Casa','inductance','2024-06-14 09:26:54','2024-06-14 09:26:54',41),(42,4,405.00,1.62,-0.78,1.80,0.380,0.90,2.73,'15','Chiller','capacitance','2024-06-14 19:03:07','2024-06-14 19:03:07',42);
/*!40000 ALTER TABLE `loads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyects`
--

DROP TABLE IF EXISTS `proyects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_proyects_users_idx` (`user_id`),
  CONSTRAINT `fk_proyects_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyects`
--

LOCK TABLES `proyects` WRITE;
/*!40000 ALTER TABLE `proyects` DISABLE KEYS */;
INSERT INTO `proyects` VALUES (1,'Empresa Verde',1,'2024-05-10 17:27:38','2024-05-10 17:27:38'),(2,'Empresa Azul',1,'2024-06-10 19:47:48','2024-06-10 19:47:48');
/*!40000 ALTER TABLE `proyects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `singles_breakers`
--

DROP TABLE IF EXISTS `singles_breakers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `singles_breakers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `singles_breakers`
--

LOCK TABLES `singles_breakers` WRITE;
/*!40000 ALTER TABLE `singles_breakers` DISABLE KEYS */;
INSERT INTO `singles_breakers` VALUES (1,'1X6 \'C\' 10KA',6,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'1X10 \'C\' 10KA',10,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'1X16 \'C\' 10KA',16,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'1X20 \'C\' 10KA',20,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'1X25 \'C\' 10KA',25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'1X32 \'C\' 10KA',32,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'1X40 \'C\' 10KA',40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'1X50 \'C\' 10KA',50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,'1X100 \'C\' 10KA',100,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `singles_breakers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `singles_elect_diff`
--

DROP TABLE IF EXISTS `singles_elect_diff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `singles_elect_diff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `singles_elect_diff`
--

LOCK TABLES `singles_elect_diff` WRITE;
/*!40000 ALTER TABLE `singles_elect_diff` DISABLE KEYS */;
INSERT INTO `singles_elect_diff` VALUES (1,'2X25 30mA',25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'2X40 30mA',40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'2X100 30mA',100,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `singles_elect_diff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tds`
--

DROP TABLE IF EXISTS `tds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tds` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tg_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `tag` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_tds_tgs1_idx` (`tg_id`),
  CONSTRAINT `fk_tds_tgs1` FOREIGN KEY (`tg_id`) REFERENCES `tgs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tds`
--

LOCK TABLES `tds` WRITE;
/*!40000 ALTER TABLE `tds` DISABLE KEYS */;
INSERT INTO `tds` VALUES (3,3,'Tablero 1er piso','TD1','2024-06-10 21:30:20','2024-06-10 21:30:20'),(4,3,'Tablero 2do piso','P2','2024-06-12 09:10:43','2024-06-12 09:10:43');
/*!40000 ALTER TABLE `tds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tgs`
--

DROP TABLE IF EXISTS `tgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tgs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `proyect_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `tag` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_tgs_proyects1_idx` (`proyect_id`),
  CONSTRAINT `fk_tgs_proyects1` FOREIGN KEY (`proyect_id`) REFERENCES `proyects` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tgs`
--

LOCK TABLES `tgs` WRITE;
/*!40000 ALTER TABLE `tgs` DISABLE KEYS */;
INSERT INTO `tgs` VALUES (3,1,'Tablero Principal 1','P1','2024-05-23 23:33:55','2024-05-23 23:33:55'),(4,1,'Tablero Principal 2','P2','2024-06-10 21:37:00','2024-06-10 21:37:00');
/*!40000 ALTER TABLE `tgs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `three_breakers`
--

DROP TABLE IF EXISTS `three_breakers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `three_breakers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `disyuntor` varchar(255) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `three_breakers`
--

LOCK TABLES `three_breakers` WRITE;
/*!40000 ALTER TABLE `three_breakers` DISABLE KEYS */;
INSERT INTO `three_breakers` VALUES (1,'3X6 \'C\' 10KA',6,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'3X10 \'C\' 10KA',10,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'3X16 \'C\' 10KA',16,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'3X20 \'C\' 10KA',20,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'3X25 \'C\' 10KA',25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'3X32 \'C\' 10KA',32,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'3X40 \'C\' 10KA',40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'3X50 \'C\' 10KA',50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,'3X63 \'C\' 10KA',63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,'3X80 \'C\' 10KA',80,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(11,'3X100 \'C\' 10KA',100,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(12,'3X125 \'C\' 10KA',125,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(13,'3X160 \'C\' 10KA',160,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `three_breakers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `three_elect_diff`
--

DROP TABLE IF EXISTS `three_elect_diff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `three_elect_diff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `diferencial` varchar(255) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `three_elect_diff`
--

LOCK TABLES `three_elect_diff` WRITE;
/*!40000 ALTER TABLE `three_elect_diff` DISABLE KEYS */;
INSERT INTO `three_elect_diff` VALUES (1,'4X25 300mA',25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'4X40 300mA',40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'4X50 300mA',50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'4X63 300mA',63,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'4X80 300mA',80,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'4X100 300mA',100,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'4X125 300mA',125,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'4X160 300mA',160,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `three_elect_diff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `total_tds`
--

DROP TABLE IF EXISTS `total_tds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `total_tds` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `ref` varchar(255) DEFAULT NULL,
  `tab_secondary` int DEFAULT NULL,
  `total_center` int DEFAULT NULL,
  `total_current_ct` decimal(6,2) DEFAULT NULL,
  `total_active_power_ct` decimal(6,2) DEFAULT NULL,
  `total_apparent_power_ct` decimal(6,2) DEFAULT NULL,
  `total_reactive_power_ct` decimal(6,2) DEFAULT NULL,
  `td_fp` decimal(6,2) DEFAULT NULL,
  `td_impedance` varchar(255) DEFAULT NULL,
  `single_voltage` decimal(4,3) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `td_id` int NOT NULL,
  `elect_differencial` varchar(45) DEFAULT NULL,
  `secctionmm2` decimal(6,2) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `wires` varchar(255) DEFAULT NULL,
  `current_by_method` decimal(5,2) DEFAULT NULL,
  `type_circuit` varchar(255) DEFAULT NULL,
  `vp` decimal(6,2) DEFAULT NULL,
  `breakers` varchar(255) DEFAULT NULL,
  `conduit` varchar(45) DEFAULT NULL,
  `length_from_tg` varchar(45) DEFAULT NULL,
  `current_r` decimal(6,2) DEFAULT NULL,
  `current_s` decimal(6,2) DEFAULT NULL,
  `current_t` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_total_circuits_tds_tds1_idx` (`td_id`),
  CONSTRAINT `fk_total_circuits_tds_tds1` FOREIGN KEY (`td_id`) REFERENCES `tds` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `total_tds`
--

LOCK TABLES `total_tds` WRITE;
/*!40000 ALTER TABLE `total_tds` DISABLE KEYS */;
INSERT INTO `total_tds` VALUES (3,'14','Tablero 1er piso',3,28,36.72,14.22,15.79,1.29,0.90,'capacitance',0.380,'2024-06-10 21:30:20','2024-06-10 21:30:20',3,'4X50 300mA',8.37,'a2','RV',46.00,'feeder',0.83,'3X50 \'C\' 10KA','50','10.50',36.72,36.72,36.72),(4,'15','Tablero 2do piso',3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-06-12 09:10:43','2024-06-12 09:10:43',4,NULL,NULL,'a2','RV-K',NULL,'feeder',NULL,NULL,NULL,'15.20',NULL,NULL,NULL);
/*!40000 ALTER TABLE `total_tds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `company` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(1024) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Enzo','Muñoz','Casa','enzo@email.com','$2b$12$wowmTgXyYtPvH9.nC/Er6eF5ryOTAlkrIRtWcZg8TYRL3K8F9AbVe','2024-05-10 17:27:19','2024-05-10 17:27:19'),(2,'Eli','Muñoz','Casa','eli@email.com','$2b$12$P9/M3zWlDz37TOcMGSkXv.oruE6qrOIhskf2kjYRMQL3N8fMQrs.K','2024-05-20 22:57:36','2024-05-20 22:57:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wires`
--

DROP TABLE IF EXISTS `wires`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wires` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wires`
--

LOCK TABLES `wires` WRITE;
/*!40000 ALTER TABLE `wires` DISABLE KEYS */;
INSERT INTO `wires` VALUES (1,'THHN','2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,'RV','2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,'RV-K','2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,'RZ1','2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,'RZ1-K','2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,'H07V','2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,'H07Z1','2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,'THWN','2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,'NYIFY','2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,'ACOMETIDA','2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `wires` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wiresh07z`
--

DROP TABLE IF EXISTS `wiresh07z`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wiresh07z` (
  `id` int NOT NULL AUTO_INCREMENT,
  `secction_mm2` decimal(5,2) DEFAULT NULL,
  `secction_awg` varchar(20) DEFAULT NULL,
  `a1` int DEFAULT NULL,
  `b1` int DEFAULT NULL,
  `e` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wiresh07z`
--

LOCK TABLES `wiresh07z` WRITE;
/*!40000 ALTER TABLE `wiresh07z` DISABLE KEYS */;
INSERT INTO `wiresh07z` VALUES (1,1.50,NULL,14,16,19,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,2.50,NULL,18,21,25,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,3.31,'12',21,25,30,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,4.00,NULL,24,28,34,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,5.26,'10',28,34,40,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,6.00,NULL,31,36,43,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,8.37,'8',38,45,53,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,10.00,NULL,42,50,60,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,13.30,'6',50,60,71,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,16.00,NULL,56,68,80,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(11,21.10,'4',66,80,91,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(12,25.00,NULL,73,89,101,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(13,26.70,'3',76,93,106,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(14,33.60,'2',87,108,122,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(15,35.00,NULL,89,110,126,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(16,42.40,'1',100,125,142,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(17,50.00,NULL,108,134,153,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(18,53.50,'1/0',116,144,165,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(19,67.40,'2/0',133,167,191,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(20,70.00,NULL,136,171,196,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(21,85.00,'3/0',153,193,222,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(22,95.00,NULL,164,207,238,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(23,107.20,'4/0',176,223,257,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(24,120.00,NULL,188,239,276,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(25,126.70,'250',195,248,286,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(26,150.00,NULL,216,262,319,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(27,152.00,'300',217,264,321,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(28,177.30,'350',239,289,355,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(29,185.00,NULL,245,296,364,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(30,202.70,'400',259,315,386,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(31,240.00,NULL,286,346,430,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(32,253.30,'500',296,356,446,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(33,300.00,NULL,328,394,497,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `wiresh07z` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wiresthrv`
--

DROP TABLE IF EXISTS `wiresthrv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wiresthrv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `secction_mm2` decimal(5,2) DEFAULT NULL,
  `secction_awg` varchar(20) DEFAULT NULL,
  `a1` int DEFAULT NULL,
  `a2` int DEFAULT NULL,
  `b1` int DEFAULT NULL,
  `b2` int DEFAULT NULL,
  `d1` int DEFAULT NULL,
  `d2` int DEFAULT NULL,
  `e` int DEFAULT NULL,
  `f` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wiresthrv`
--

LOCK TABLES `wiresthrv` WRITE;
/*!40000 ALTER TABLE `wiresthrv` DISABLE KEYS */;
INSERT INTO `wiresthrv` VALUES (1,1.50,NULL,17,17,20,20,25,35,23,NULL,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(2,2.50,NULL,23,22,28,26,33,45,32,NULL,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(3,3.31,'12',28,26,33,31,38,53,38,NULL,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(4,4.00,NULL,31,30,37,35,42,59,42,42,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(5,5.26,'10',37,35,44,41,48,69,50,50,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(6,6.00,NULL,40,38,48,44,52,74,54,55,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(7,8.37,'8',49,46,59,54,63,89,67,68,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(8,10.00,NULL,54,51,66,60,68,98,75,77,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(9,13.30,'6',65,61,79,72,80,114,89,93,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(10,16.00,NULL,73,68,88,80,89,126,100,105,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(11,21.10,'4',86,80,105,95,103,147,114,126,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(12,25.00,NULL,95,89,117,105,113,161,127,141,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(13,26.70,'3',99,92,122,109,117,167,133,147,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(14,33.60,'2',114,106,141,125,132,189,154,172,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(15,35.00,NULL,117,109,144,128,136,194,158,176,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(16,42.40,'1',132,122,163,144,150,216,178,200,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(17,50.00,NULL,141,130,175,154,159,230,192,216,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(18,53.50,'1/0',152,140,188,165,170,245,207,234,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(19,67.40,'2/0',175,161,217,190,192,278,240,273,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(20,70.00,NULL,179,164,222,194,197,282,246,279,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(21,85.00,'3/0',201,185,251,218,218,315,278,318,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(22,95.00,NULL,216,197,269,233,232,339,298,342,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(23,107.20,'4/0',232,212,290,251,248,362,322,371,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(24,120.00,NULL,249,227,312,268,263,386,346,400,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(25,126.70,'250',257,234,322,277,270,396,358,415,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(26,150.00,NULL,285,259,342,300,296,431,399,464,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(27,152.00,'300',287,261,344,302,299,437,402,468,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(28,177.30,'350',316,287,374,331,325,474,444,518,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(29,185.00,NULL,324,295,384,340,332,486,456,533,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(30,202.70,'400',342,312,405,358,349,510,483,567,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(31,240.00,NULL,380,346,450,398,382,563,538,634,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(32,253.30,'500',392,357,464,410,393,576,557,657,'2024-05-10 17:27:59','2024-05-10 17:27:59'),(33,300.00,NULL,435,396,514,455,431,629,621,736,'2024-05-10 17:27:59','2024-05-10 17:27:59');
/*!40000 ALTER TABLE `wiresthrv` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-04 18:34:11
