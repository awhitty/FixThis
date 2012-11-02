create table `users` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR (100) NOT NULL,
  `email` VARCHAR (100),
  `image` VARCHAR (200),
  `hash` CHAR (64) NOT NULL,
  `salt` CHAR (64) NOT NULL
) engine = InnoDB;

create table `requests` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` UNSIGNED NOT NULL,
  `desc` VARCHAR (255),
  `image` VARCHAR (200),
  `longitude` double,
  `latitude` double,
  `timestamp` timestamp
) engine = InnoDB;

create table `interest_areas` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` UNSIGNED NOT NULL,
  `area_name` VARCHAR (255),
) engine = InnoDB;
