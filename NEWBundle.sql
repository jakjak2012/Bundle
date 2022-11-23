-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Bundle
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Bundle` ;

-- -----------------------------------------------------
-- Schema Bundle
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Bundle` DEFAULT CHARACTER SET utf8mb3 ;
USE `Bundle` ;

-- -----------------------------------------------------
-- Table `Bundle`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bundle`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(30) NULL DEFAULT NULL,
  `last_name` VARCHAR(30) NULL DEFAULT NULL,
  `username` VARCHAR(60) NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `password` VARCHAR(60) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Bundle`.`transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bundle`.`transactions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `amount` INT NULL DEFAULT NULL,
  `category` VARCHAR(45) NULL DEFAULT NULL,
  `comment` VARCHAR(100) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_transactions_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_transactions_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `Bundle`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Bundle`.`budget`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bundle`.`budget` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `budget_amt` INT NULL,
  `budget_cat` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_budget_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_budget_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `Bundle`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
