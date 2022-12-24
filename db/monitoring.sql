-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Dec 24, 2022 at 10:52 AM
-- Server version: 10.6.10-MariaDB-log
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `monitoring`
--

-- --------------------------------------------------------

--
-- Table structure for table `disk_space`
--

CREATE TABLE `disk_space` (
  `id` bigint(20) NOT NULL,
  `host_id` varchar(64) NOT NULL,
  `mount_point` varchar(255) NOT NULL,
  `total_bytes` bigint(20) DEFAULT NULL,
  `used_bytes` bigint(20) DEFAULT NULL,
  `free_bytes` bigint(20) DEFAULT NULL,
  `creation_timestamp` timestamp NULL DEFAULT current_timestamp(),
  `update_timestamp` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `host`
--

CREATE TABLE `host` (
  `id` varchar(64) NOT NULL,
  `friendly_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `disk_space`
--
ALTER TABLE `disk_space`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idx_host_mount_point` (`host_id`,`mount_point`);

--
-- Indexes for table `host`
--
ALTER TABLE `host`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `friendly_name` (`friendly_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `disk_space`
--
ALTER TABLE `disk_space`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `disk_space`
--
ALTER TABLE `disk_space`
  ADD CONSTRAINT `disk_space_ibfk_1` FOREIGN KEY (`host_id`) REFERENCES `host` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
