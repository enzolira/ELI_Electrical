-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ELI_ELECTRICAL
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ELI_ELECTRICAL` ;

-- -----------------------------------------------------
-- Schema ELI_ELECTRICAL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ELI_ELECTRICAL` DEFAULT CHARACTER SET utf8mb3 ;
USE `ELI_ELECTRICAL` ;

-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `company` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(1024) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`proyects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`proyects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_proyects_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_proyects_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `ELI_ELECTRICAL`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`tgs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`tgs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `proyect_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `tag` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_tgs_proyects1_idx` (`proyect_id` ASC) VISIBLE,
  CONSTRAINT `fk_tgs_proyects1`
    FOREIGN KEY (`proyect_id`)
    REFERENCES `ELI_ELECTRICAL`.`proyects` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`tds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`tds` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tg_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `tag` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_tds_tgs1_idx` (`tg_id` ASC) VISIBLE,
  CONSTRAINT `fk_tds_tgs1`
    FOREIGN KEY (`tg_id`)
    REFERENCES `ELI_ELECTRICAL`.`tgs` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`circuits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`circuits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `ref` TEXT NULL DEFAULT NULL,
  `total_center` INT NULL DEFAULT NULL,
  `total_current_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_length_ct` VARCHAR(25) NULL DEFAULT NULL,
  `total_active_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_reactive_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_apparent_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_fp` DECIMAL(6,2) NULL DEFAULT NULL,
  `name_impedance` VARCHAR(255) NULL DEFAULT NULL,
  `elect_differencial` VARCHAR(45) NULL DEFAULT NULL,
  `secctionmm2` DECIMAL(6,2) NULL DEFAULT NULL,
  `method` VARCHAR(255) NULL DEFAULT NULL,
  `wires` VARCHAR(255) NULL DEFAULT NULL,
  `current_by_method` DECIMAL(5,2) NULL DEFAULT NULL,
  `type_circuit` VARCHAR(255) NULL DEFAULT NULL,
  `vp` DECIMAL(6,2) NULL DEFAULT NULL,
  `single_voltage` DECIMAL(4,3) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `breakers` VARCHAR(255) NULL DEFAULT NULL,
  `conduit` VARCHAR(45) NULL DEFAULT NULL,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tg_id` INT NOT NULL,
  `td_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_loads_tgs1_idx` (`tg_id` ASC) VISIBLE,
  INDEX `fk_loads_tds1_idx` (`td_id` ASC) VISIBLE,
  CONSTRAINT `fk_loads_tds1`
    FOREIGN KEY (`td_id`)
    REFERENCES `ELI_ELECTRICAL`.`tds` (`id`),
  CONSTRAINT `fk_loads_tgs1`
    FOREIGN KEY (`tg_id`)
    REFERENCES `ELI_ELECTRICAL`.`tgs` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`conduits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`conduits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nameconduit` VARCHAR(255) NULL DEFAULT NULL,
  `c1` INT NULL DEFAULT NULL,
  `c2` INT NULL DEFAULT NULL,
  `c3` INT NULL DEFAULT NULL,
  `c4` INT NULL DEFAULT NULL,
  `c5` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`conduitsubte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`conduitsubte` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `namesubte` VARCHAR(255) NULL DEFAULT NULL,
  `c1` INT NULL DEFAULT NULL,
  `c2` INT NULL DEFAULT NULL,
  `c3` INT NULL DEFAULT NULL,
  `c4` INT NULL DEFAULT NULL,
  `c5` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 31
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`jobs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`jobs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `title` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `start` DATETIME NULL DEFAULT NULL,
  `end` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `update_at` DATETIME NULL DEFAULT NULL,
  `proyect_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_jobs_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_jobs_proyects2_idx` (`proyect_id` ASC) VISIBLE,
  CONSTRAINT `fk_jobs_proyects2`
    FOREIGN KEY (`proyect_id`)
    REFERENCES `ELI_ELECTRICAL`.`proyects` (`id`),
  CONSTRAINT `fk_jobs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `ELI_ELECTRICAL`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`loads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`loads` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `qty` INT NULL DEFAULT NULL,
  `active_power` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_active_power` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_reactive_power` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_apparent_power` DECIMAL(6,2) NULL DEFAULT NULL,
  `voltage` DECIMAL(4,3) NULL DEFAULT NULL,
  `fp` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_current` DECIMAL(6,2) NULL DEFAULT NULL,
  `length` VARCHAR(45) NULL DEFAULT NULL,
  `nameloads` VARCHAR(255) NULL DEFAULT NULL,
  `impedance` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `circuit_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_loads_circuits1_idx` (`circuit_id` ASC) VISIBLE,
  CONSTRAINT `fk_loads_circuits1`
    FOREIGN KEY (`circuit_id`)
    REFERENCES `ELI_ELECTRICAL`.`circuits` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`singles_breakers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`singles_breakers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`singles_elect_diff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`singles_elect_diff` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`three_breakers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`three_breakers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `disyuntor` VARCHAR(255) NULL DEFAULT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 27
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`three_elect_diff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`three_elect_diff` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `diferencial` VARCHAR(255) NULL DEFAULT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`total_tds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`total_tds` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `ref` VARCHAR(255) NULL DEFAULT NULL,
  `tab_secondary` INT NULL DEFAULT NULL,
  `total_center` INT NULL DEFAULT NULL,
  `total_current_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_active_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_apparent_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `total_reactive_power_ct` DECIMAL(6,2) NULL DEFAULT NULL,
  `td_fp` DECIMAL(6,2) NULL DEFAULT NULL,
  `td_impedance` VARCHAR(255) NULL DEFAULT NULL,
  `single_voltage` DECIMAL(4,3) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `td_id` INT NOT NULL,
  `elect_differencial` VARCHAR(45) NULL,
  `secctionmm2` DECIMAL(6,2) NULL,
  `method` VARCHAR(255) NULL,
  `wires` VARCHAR(255) NULL,
  `current_by_method` DECIMAL(5,2) NULL,
  `type_circuit` VARCHAR(255) NULL,
  `vp` DECIMAL(6,2) NULL,
  `breakers` VARCHAR(255) NULL,
  `conduit` VARCHAR(45) NULL,
  `length_from_tg` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_total_circuits_tds_tds1_idx` (`td_id` ASC) VISIBLE,
  CONSTRAINT `fk_total_circuits_tds_tds1`
    FOREIGN KEY (`td_id`)
    REFERENCES `ELI_ELECTRICAL`.`tds` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`wires`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`wires` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`wiresh07z`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`wiresh07z` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `secction_mm2` DECIMAL(5,2) NULL DEFAULT NULL,
  `secction_awg` VARCHAR(20) NULL DEFAULT NULL,
  `a1` INT NULL DEFAULT NULL,
  `b1` INT NULL DEFAULT NULL,
  `e` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 35
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`wiresthrv`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`wiresthrv` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `secction_mm2` DECIMAL(5,2) NULL DEFAULT NULL,
  `secction_awg` VARCHAR(20) NULL DEFAULT NULL,
  `a1` INT NULL DEFAULT NULL,
  `a2` INT NULL DEFAULT NULL,
  `b1` INT NULL DEFAULT NULL,
  `b2` INT NULL DEFAULT NULL,
  `d1` INT NULL DEFAULT NULL,
  `d2` INT NULL DEFAULT NULL,
  `e` INT NULL DEFAULT NULL,
  `f` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 35
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
