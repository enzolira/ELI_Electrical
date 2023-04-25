-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ELI_ELECTRICAL
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ELI_ELECTRICAL` ;

-- -----------------------------------------------------
-- Schema ELI_ELECTRICAL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ELI_ELECTRICAL` DEFAULT CHARACTER SET utf8 ;
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
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`proyects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`proyects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `uodated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_proyects_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_proyects_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `ELI_ELECTRICAL`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`tgs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`tgs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `proyect_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `tag` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_tgs_proyects1_idx` (`proyect_id` ASC) VISIBLE,
  CONSTRAINT `fk_tgs_proyects1`
    FOREIGN KEY (`proyect_id`)
    REFERENCES `ELI_ELECTRICAL`.`proyects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`tds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`tds` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tg_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `tag` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_tds_tgs1_idx` (`tg_id` ASC) VISIBLE,
  CONSTRAINT `fk_tds_tgs1`
    FOREIGN KEY (`tg_id`)
    REFERENCES `ELI_ELECTRICAL`.`tgs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`circuits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`circuits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `tds_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_circuits_tds1_idx` (`tds_id` ASC) VISIBLE,
  CONSTRAINT `fk_circuits_tds1`
    FOREIGN KEY (`tds_id`)
    REFERENCES `ELI_ELECTRICAL`.`tds` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ELI_ELECTRICAL`.`loads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ELI_ELECTRICAL`.`loads` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `circuit_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `ref` TEXT NOT NULL,
  `qty` INT NOT NULL,
  `load` INT NOT NULL,
  `total_load` INT NULL,
  `single_voltage` INT NOT NULL,
  `fp` INT NULL DEFAULT 1,
  `total_current` INT NULL,
  `lenght` INT NULL,
  `min_secction` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_loads_circuits1_idx` (`circuit_id` ASC) VISIBLE,
  CONSTRAINT `fk_loads_circuits1`
    FOREIGN KEY (`circuit_id`)
    REFERENCES `ELI_ELECTRICAL`.`circuits` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
