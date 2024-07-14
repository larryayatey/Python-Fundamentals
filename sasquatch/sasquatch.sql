-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sasquatch
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sasquatch` ;

-- -----------------------------------------------------
-- Schema sasquatch
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sasquatch` DEFAULT CHARACTER SET utf8mb3 ;
-- -----------------------------------------------------
-- Schema sasquatch
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sasquatch` ;

-- -----------------------------------------------------
-- Schema sasquatch
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sasquatch` DEFAULT CHARACTER SET utf8mb3 ;
USE `sasquatch` ;
USE `sasquatch` ;

-- -----------------------------------------------------
-- Table `sasquatch`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sasquatch`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `sasquatch`.`quatch`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sasquatch`.`quatch` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `number` FLOAT NOT NULL,
  `happened` TEXT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sasquatch_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_sasquatch_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `sasquatch`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
