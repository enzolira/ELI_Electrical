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
-- Table `ELI_ELECTRICAL`.`tds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`tds` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `tag` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `proyect_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tds_proyects1_idx` (`proyect_id` ASC) VISIBLE,
  CONSTRAINT `fk_tds_proyects1`
    FOREIGN KEY (`proyect_id`)
    REFERENCES `ELI_ELECTRICAL`.`proyects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`circuits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`circuits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `td_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_circuits_tds1_idx` (`td_id` ASC) VISIBLE,
  CONSTRAINT `fk_circuits_tds1`
    FOREIGN KEY (`td_id`)
    REFERENCES `ELI_ELECTRICAL`.`tds` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`loads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`loads` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `ref` TEXT NOT NULL,
  `qty` INT NOT NULL,
  `load` INT NOT NULL,
  `total_load` INT NULL DEFAULT NULL,
  `voltage` INT NOT NULL,
  `fp` INT NULL DEFAULT '1',
  `total_current` INT NULL DEFAULT NULL,
  `lenght` INT NULL DEFAULT NULL,
  `min_secction` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `circuit_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_loads_circuits1_idx` (`circuit_id` ASC) VISIBLE,
  CONSTRAINT `fk_loads_circuits1`
    FOREIGN KEY (`circuit_id`)
    REFERENCES `ELI_ELECTRICAL`.`circuits` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
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
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`methods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`methods` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `methods` VARCHAR(45) NOT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT 'NOW()',
  `updated_at` VARCHAR(45) NULL DEFAULT 'NOW()',
  `wiresh07z_id` INT NOT NULL,
  `wiresthrv_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_methods_wiresh07z1_idx` (`wiresh07z_id` ASC) VISIBLE,
  INDEX `fk_methods_wiresthrv1_idx` (`wiresthrv_id` ASC) VISIBLE,
  CONSTRAINT `fk_methods_wiresh07z1`
    FOREIGN KEY (`wiresh07z_id`)
    REFERENCES `ELI_ELECTRICAL`.`wiresh07z` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_methods_wiresthrv1`
    FOREIGN KEY (`wiresthrv_id`)
    REFERENCES `ELI_ELECTRICAL`.`wiresthrv` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`wires`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`wires` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
