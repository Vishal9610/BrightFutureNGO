-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2026 at 02:16 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `brightfuture`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'vishal', 'vishal123');

-- --------------------------------------------------------

--
-- Table structure for table `analytics`
--

CREATE TABLE `analytics` (
  `id` int(11) NOT NULL,
  `page_name` varchar(100) NOT NULL,
  `element_name` varchar(150) DEFAULT NULL,
  `event_type` enum('view','click') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `analytics`
--

INSERT INTO `analytics` (`id`, `page_name`, `element_name`, `event_type`, `created_at`) VALUES
(1, 'Home', NULL, 'view', '2026-08-11 04:55:27'),
(2, 'Home', NULL, 'view', '2026-08-11 05:11:59'),
(3, 'Programs', NULL, 'view', '2026-08-11 05:12:10'),
(4, 'Team', NULL, 'view', '2026-08-11 05:12:12'),
(5, 'Gallery', NULL, 'view', '2026-08-11 05:12:13'),
(6, 'Donate', NULL, 'view', '2026-08-11 05:12:14'),
(7, 'Contact', NULL, 'view', '2026-08-11 05:12:17'),
(8, 'About', NULL, 'view', '2026-08-11 05:12:18'),
(9, 'Home', NULL, 'view', '2026-08-11 05:13:20'),
(10, 'Learn More', NULL, 'view', '2026-08-11 05:13:22'),
(11, 'About Details', NULL, 'view', '2026-08-11 05:14:40'),
(12, 'About Details', NULL, 'view', '2026-08-11 05:53:24'),
(13, 'Home', NULL, 'view', '2026-08-11 05:53:29'),
(14, 'Home', NULL, 'view', '2026-08-11 05:54:27'),
(15, 'Home', NULL, 'view', '2026-08-11 05:56:46'),
(16, 'Home', NULL, 'view', '2026-08-11 06:08:24'),
(17, 'Home', NULL, 'view', '2026-08-11 08:04:35'),
(18, 'About Details', NULL, 'view', '2026-08-11 08:04:53'),
(19, 'Home', 'Free Education', 'click', '2026-08-11 08:04:57'),
(20, 'Home', 'School Supplies', 'click', '2026-08-11 08:04:58'),
(21, 'Home', 'Nutrition', 'click', '2026-08-11 08:05:01'),
(22, 'Contact', NULL, 'view', '2026-08-11 08:05:16'),
(23, 'Contact', NULL, 'view', '2026-08-11 08:05:23'),
(24, 'Contact', NULL, 'view', '2026-08-11 08:05:27'),
(25, 'Home', 'Join Us', 'click', '2026-08-11 08:05:40'),
(26, 'Home', 'Learn More', 'click', '2026-08-11 08:05:43'),
(27, 'Learn More', NULL, 'view', '2026-08-11 08:05:43'),
(28, 'Programs', NULL, 'view', '2026-08-11 08:05:47'),
(29, 'Team', NULL, 'view', '2026-08-11 08:06:01'),
(30, 'Gallery', NULL, 'view', '2026-08-11 08:06:08'),
(31, 'Donate', NULL, 'view', '2026-08-11 08:06:14'),
(32, 'About', NULL, 'view', '2026-08-11 08:06:19'),
(33, 'Contact', NULL, 'view', '2026-08-11 08:06:24'),
(34, 'Contact', NULL, 'view', '2026-08-11 08:50:01'),
(35, 'Contact', NULL, 'view', '2026-08-11 08:50:02'),
(36, 'Home', NULL, 'view', '2026-08-11 08:50:13'),
(37, 'Home', 'Join Us', 'click', '2026-08-11 08:50:17'),
(38, 'Home', 'Learn More', 'click', '2026-08-11 08:50:19'),
(39, 'Learn More', NULL, 'view', '2026-08-11 08:50:19'),
(40, 'Home', 'Learn More', 'click', '2026-08-11 08:50:24'),
(41, 'Learn More', NULL, 'view', '2026-08-11 08:50:24'),
(42, 'Donate', NULL, 'view', '2026-08-11 08:50:25'),
(43, 'Home', 'Free Education', 'click', '2026-08-11 08:50:44'),
(44, 'Home', 'School Supplies', 'click', '2026-08-11 08:50:44'),
(45, 'Home', 'Nutrition', 'click', '2026-08-11 08:50:45'),
(46, 'Home', 'Health & Hygiene', 'click', '2026-08-11 08:50:45'),
(47, 'About Details', NULL, 'view', '2026-08-11 08:50:47'),
(48, 'Programs', NULL, 'view', '2026-08-11 08:50:54'),
(49, 'Team', NULL, 'view', '2026-08-11 08:50:55'),
(50, 'Gallery', NULL, 'view', '2026-08-11 08:50:56'),
(51, 'Donate', NULL, 'view', '2026-08-11 08:50:57'),
(52, 'Contact', NULL, 'view', '2026-08-11 08:50:58'),
(53, 'About', NULL, 'view', '2026-08-11 08:50:59'),
(54, 'Home', NULL, 'view', '2026-08-11 08:51:01'),
(55, 'Home', NULL, 'view', '2026-08-11 09:03:38'),
(56, 'Gallery', NULL, 'view', '2026-08-11 09:04:50'),
(57, 'Gallery', NULL, 'view', '2026-08-11 09:05:15'),
(58, 'Gallery', NULL, 'view', '2026-08-11 09:05:16'),
(59, 'Gallery', NULL, 'view', '2026-08-11 09:09:17'),
(60, 'Gallery', NULL, 'view', '2026-08-11 09:13:38'),
(61, 'Gallery', NULL, 'view', '2026-08-11 09:18:19'),
(62, 'Gallery', NULL, 'view', '2026-08-11 09:18:28'),
(63, 'Gallery', NULL, 'view', '2026-08-11 09:19:49'),
(64, 'Gallery', NULL, 'view', '2026-08-11 09:19:59'),
(65, 'Home', NULL, 'view', '2026-08-11 14:31:27'),
(66, 'Gallery', NULL, 'view', '2026-08-11 14:32:59'),
(67, 'Gallery', NULL, 'view', '2026-08-11 14:33:15'),
(68, 'Gallery', NULL, 'view', '2026-08-11 14:52:13'),
(69, 'Gallery', NULL, 'view', '2026-08-11 14:52:25'),
(70, 'Gallery', NULL, 'view', '2026-08-11 14:52:25'),
(71, 'Gallery', NULL, 'view', '2026-08-11 14:52:25'),
(72, 'Gallery', NULL, 'view', '2026-08-11 14:52:25'),
(73, 'Gallery', NULL, 'view', '2026-08-11 14:52:25'),
(74, 'Gallery', NULL, 'view', '2026-08-11 14:52:26'),
(75, 'Gallery', NULL, 'view', '2026-08-11 14:53:13'),
(76, 'Gallery', NULL, 'view', '2026-08-11 14:53:14'),
(77, 'Gallery', NULL, 'view', '2026-08-11 14:53:15'),
(78, 'Gallery', NULL, 'view', '2026-08-11 14:53:29'),
(79, 'Gallery', NULL, 'view', '2026-08-11 14:55:49'),
(80, 'Gallery', NULL, 'view', '2026-08-11 15:07:44'),
(81, 'Gallery', NULL, 'view', '2026-08-11 15:07:45'),
(82, 'Gallery', NULL, 'view', '2026-08-11 15:07:47'),
(83, 'Gallery', NULL, 'view', '2026-08-11 15:07:51'),
(84, 'Gallery', NULL, 'view', '2026-08-11 15:07:51'),
(85, 'Gallery', NULL, 'view', '2026-08-11 15:08:46'),
(86, 'Gallery', NULL, 'view', '2026-08-11 15:18:00'),
(87, 'Gallery', NULL, 'view', '2026-08-11 15:18:02'),
(88, 'Gallery', NULL, 'view', '2026-08-11 15:18:03'),
(89, 'Gallery', NULL, 'view', '2026-08-11 15:18:06'),
(90, 'Gallery', NULL, 'view', '2026-08-11 15:18:06'),
(91, 'Gallery', NULL, 'view', '2026-08-11 15:22:17'),
(92, 'Gallery', NULL, 'view', '2026-08-11 15:25:42'),
(93, 'Gallery', NULL, 'view', '2026-08-11 15:26:10'),
(94, 'Gallery', NULL, 'view', '2026-08-11 15:26:48'),
(95, 'Gallery', NULL, 'view', '2026-08-11 15:26:48'),
(96, 'Gallery', NULL, 'view', '2026-08-11 15:26:48'),
(97, 'Gallery', NULL, 'view', '2026-08-11 15:29:00'),
(98, 'Gallery', NULL, 'view', '2026-08-11 15:29:01'),
(99, 'Gallery', NULL, 'view', '2026-08-11 15:29:09'),
(100, 'Gallery', NULL, 'view', '2026-08-11 15:29:15'),
(101, 'Gallery', NULL, 'view', '2026-08-11 15:29:16'),
(102, 'Gallery', NULL, 'view', '2026-08-11 15:32:13'),
(103, 'Gallery', NULL, 'view', '2026-08-11 15:32:13'),
(104, 'Gallery', NULL, 'view', '2026-08-11 15:33:31'),
(105, 'Gallery', NULL, 'view', '2026-08-11 15:33:32'),
(106, 'Gallery', NULL, 'view', '2026-08-11 15:33:33'),
(107, 'Gallery', NULL, 'view', '2026-08-11 15:56:52'),
(108, 'Gallery', NULL, 'view', '2026-08-11 16:14:35'),
(109, 'Gallery', NULL, 'view', '2026-08-11 16:14:39'),
(110, 'Gallery', NULL, 'view', '2026-08-11 16:14:39'),
(111, 'Gallery', NULL, 'view', '2026-08-11 16:15:13'),
(112, 'Home', NULL, 'view', '2026-08-11 16:15:36'),
(113, 'Home', NULL, 'view', '2026-08-11 16:15:39'),
(114, 'Home', NULL, 'view', '2026-08-11 16:15:39'),
(115, 'Home', NULL, 'view', '2026-08-11 16:15:41'),
(116, 'Programs', NULL, 'view', '2026-08-11 16:15:42'),
(117, 'Team', NULL, 'view', '2026-08-11 16:15:43'),
(118, 'Gallery', NULL, 'view', '2026-08-11 16:15:49'),
(119, 'Donate', NULL, 'view', '2026-08-11 16:15:53'),
(120, 'About', NULL, 'view', '2026-08-11 16:15:54'),
(121, 'Contact', NULL, 'view', '2026-08-11 16:15:56'),
(122, 'Home', NULL, 'view', '2026-08-11 16:16:01'),
(123, 'Home', 'Learn More', 'click', '2026-08-11 16:16:04'),
(124, 'Learn More', NULL, 'view', '2026-08-11 16:16:04'),
(125, 'Donate', NULL, 'view', '2026-08-11 16:16:05'),
(126, 'Home', 'Join Us', 'click', '2026-08-11 16:16:08'),
(127, 'About Details', NULL, 'view', '2026-08-11 16:16:18'),
(128, 'Home', 'Free Education', 'click', '2026-08-11 16:16:21'),
(129, 'Contact', NULL, 'view', '2026-08-11 16:16:26'),
(130, 'Home', 'Donate', 'click', '2026-08-11 16:16:30'),
(131, 'Donate', NULL, 'view', '2026-08-11 16:16:30'),
(132, 'Home', 'Free Education Program', 'click', '2026-08-11 16:16:36'),
(133, 'Home', 'Free Education Program', 'click', '2026-08-11 16:16:37'),
(134, 'Home', 'School Admission', 'click', '2026-08-11 16:16:37'),
(135, 'Home', 'Book Distribution', 'click', '2026-08-11 16:16:38'),
(136, 'Home', 'Career Guidline', 'click', '2026-08-11 16:16:40'),
(137, 'Home', 'Free Education', 'click', '2026-08-11 16:16:42'),
(138, 'Home', 'School Supplies', 'click', '2026-08-11 16:16:43'),
(139, 'Home', 'Nutrition', 'click', '2026-08-11 16:16:43'),
(140, 'Home', 'Health & Hygiene', 'click', '2026-08-11 16:16:43'),
(141, 'Home', NULL, 'view', '2026-08-11 16:21:47'),
(142, 'Gallery', NULL, 'view', '2026-08-11 16:21:53'),
(143, 'Gallery', NULL, 'view', '2026-08-11 16:21:59'),
(144, 'Gallery', NULL, 'view', '2026-08-11 16:22:04'),
(145, 'Gallery', NULL, 'view', '2026-08-11 16:22:13'),
(146, 'Gallery', NULL, 'view', '2026-08-11 16:26:20'),
(147, 'Gallery', NULL, 'view', '2026-08-11 16:26:22'),
(148, 'Gallery', NULL, 'view', '2026-08-11 16:26:22'),
(149, 'Gallery', NULL, 'view', '2026-08-11 16:26:29'),
(150, 'Gallery', NULL, 'view', '2026-08-11 16:28:18'),
(151, 'Gallery', NULL, 'view', '2026-08-11 16:31:46'),
(152, 'Gallery', NULL, 'view', '2026-08-11 16:33:45'),
(153, 'Gallery', NULL, 'view', '2026-08-11 16:34:47'),
(154, 'Gallery', NULL, 'view', '2026-08-11 16:35:42'),
(155, 'Gallery', NULL, 'view', '2026-08-11 16:37:20'),
(156, 'Gallery', NULL, 'view', '2026-08-11 16:37:42'),
(157, 'Gallery', NULL, 'view', '2026-08-11 16:39:44'),
(158, 'Home', NULL, 'view', '2026-08-11 16:40:03'),
(159, 'Home', NULL, 'view', '2026-08-11 16:40:03'),
(160, 'Home', NULL, 'view', '2026-08-11 16:40:03'),
(161, 'Gallery', NULL, 'view', '2026-08-11 16:40:05'),
(162, 'Gallery', NULL, 'view', '2026-08-11 16:40:31'),
(163, 'Home', NULL, 'view', '2026-08-11 16:43:24'),
(164, 'Home', NULL, 'view', '2026-08-11 16:43:24'),
(165, 'Home', 'Join Us', 'click', '2026-08-11 16:43:26'),
(166, 'Home', 'Join Us', 'click', '2026-08-11 16:44:01'),
(167, 'About Details', NULL, 'view', '2026-08-11 16:47:35'),
(168, 'About', NULL, 'view', '2026-08-11 16:47:38'),
(169, 'About Details', NULL, 'view', '2026-08-11 16:48:28'),
(170, 'About Details', NULL, 'view', '2026-08-11 16:49:12'),
(171, 'About Details', NULL, 'view', '2026-08-11 16:49:14'),
(172, 'Home', NULL, 'view', '2026-08-11 16:49:16'),
(173, 'Home', NULL, 'view', '2026-08-11 17:04:18'),
(174, 'Home', NULL, 'view', '2026-08-11 17:04:55'),
(175, 'Home', NULL, 'view', '2026-08-11 17:07:02'),
(176, 'Home', NULL, 'view', '2026-08-11 17:09:14'),
(177, 'Home', NULL, 'view', '2026-08-11 17:09:15'),
(178, 'Home', NULL, 'view', '2026-08-11 17:14:31'),
(179, 'Programs', NULL, 'view', '2026-08-11 17:14:42'),
(180, 'Home', NULL, 'view', '2026-08-11 17:17:35'),
(181, 'Contact', NULL, 'view', '2026-08-11 17:19:50'),
(182, 'Home', NULL, 'view', '2026-08-11 17:20:18'),
(183, 'Home', NULL, 'view', '2026-08-11 17:20:52');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `subject` varchar(200) DEFAULT NULL,
  `message` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `message`) VALUES
(5, 'Vishal Prajapati', 'vishalkumar12@gmail.com', 'Bright Future NGO it is a trust for street child', 'it good work for poor child');

-- --------------------------------------------------------

--
-- Table structure for table `donation`
--

CREATE TABLE `donation` (
  `id` int(11) NOT NULL,
  `upi_id` varchar(100) DEFAULT NULL,
  `account_name` varchar(100) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `account_number` varchar(50) DEFAULT NULL,
  `ifsc_code` varchar(20) DEFAULT NULL,
  `qr_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donation`
--

INSERT INTO `donation` (`id`, `upi_id`, `account_name`, `bank_name`, `account_number`, `ifsc_code`, `qr_code`) VALUES
(1, 'ngobrightfuture@upi', 'NGO Bright Future Foundation', 'State Bank of India SBI', '234324433344224', 'SBIN0004324', 'qr.png'),
(2, 'brightfuture@upi', 'Bright Future Foundation', 'State Bank of India', '123456789012', 'SBIN0001234', 'qr.png');

-- --------------------------------------------------------

--
-- Table structure for table `gallery`
--

CREATE TABLE `gallery` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `image` varchar(255) NOT NULL,
  `upload_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gallery`
--

INSERT INTO `gallery` (`id`, `title`, `image`, `upload_date`) VALUES
(28, 'Solar panel distribution drive', 'WhatsApp_Image_3.jpeg', '2026-08-11 16:28:18'),
(29, 'Solar panel distribution drive', 'WhatsApp_Image_4.jpeg', '2026-08-11 16:28:18'),
(30, 'Solar panel distribution drive', 'WhatsApp_Image_5.jpeg', '2026-08-11 16:28:18'),
(31, 'Solar panel distribution drive', 'WhatsApp_Image_2026-08-10_at_4.09.36_PM.jpeg', '2026-08-11 16:28:18'),
(32, 'Solar panel distribution drive', 'WhatsApp_Image2.jpeg', '2026-08-11 16:28:18'),
(33, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.37_PM.jpeg', '2026-08-11 16:31:46'),
(34, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.38_PM_1.jpeg', '2026-08-11 16:31:46'),
(35, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.38_PM_2.jpeg', '2026-08-11 16:31:46'),
(36, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.38_PM.jpeg', '2026-08-11 16:31:46'),
(37, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.39_PM_1.jpeg', '2026-08-11 16:31:46'),
(38, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.39_PM_2.jpeg', '2026-08-11 16:31:46'),
(39, 'Education drive- Marine life', 'WhatsApp_Image_2026-08-10_at_4.09.39_PM.jpeg', '2026-08-11 16:31:46'),
(40, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.40_PM_1.jpeg', '2026-08-11 16:33:45'),
(41, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.40_PM_2.jpeg', '2026-08-11 16:33:45'),
(42, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.40_PM.jpeg', '2026-08-11 16:33:45'),
(43, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.41_PM_1.jpeg', '2026-08-11 16:33:45'),
(44, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.41_PM_2.jpeg', '2026-08-11 16:33:45'),
(45, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.41_PM_3.jpeg', '2026-08-11 16:33:45'),
(46, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.41_PM.jpeg', '2026-08-11 16:33:45'),
(47, 'Education drive- Learning to read and write', 'WhatsApp_Image_2026-08-10_at_4.09.42_PM.jpeg', '2026-08-11 16:33:45'),
(48, 'Gupshap Mandali Week1', 'WhatsApp_Image_2026-08-10_at_4.09.42_PM_1.jpeg', '2026-08-11 16:34:47'),
(49, 'Gupshap Mandali Week1', 'WhatsApp_Image_2026-08-10_at_4.09.42_PM.jpeg', '2026-08-11 16:34:47'),
(50, 'Gupshap Mandali Week1', 'WhatsApp_Image_2026-08-10_at_4.09.43_PM_1.jpeg', '2026-08-11 16:34:47'),
(51, 'Gupshap Mandali Week1', 'WhatsApp_Image_2026-08-10_at_4.09.43_PM_2.jpeg', '2026-08-11 16:34:47'),
(52, 'Gupshap Mandali Week1', 'WhatsApp_Image_2026-08-10_at_4.09.43_PM.jpeg', '2026-08-11 16:34:47'),
(58, 'Gupshap Mandali Week2', 'WhatsApp_Image_2026-08-10_at_4.09.44_PM_1.jpeg', '2026-08-11 16:39:44'),
(59, 'Gupshap Mandali Week2', 'WhatsApp_Image_2026-08-10_at_4.09.44_PM.jpeg', '2026-08-11 16:39:44'),
(60, 'Gupshap Mandali Week2', 'WhatsApp_Image_2026-08-10_at_4.09.45_PM_1.jpeg', '2026-08-11 16:39:44'),
(61, 'Gupshap Mandali Week2', 'WhatsApp_Image_2026-08-10_at_4.09.45_PM_2.jpeg', '2026-08-11 16:39:44'),
(62, 'Gupshap Mandali Week2', 'WhatsApp_Image_2026-08-10_at_4.09.45_PM.jpeg', '2026-08-11 16:39:44');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `news_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `title`, `description`, `news_date`) VALUES
(4, 'sds', 'sdasfa', '2026-08-12');

-- --------------------------------------------------------

--
-- Table structure for table `partners`
--

CREATE TABLE `partners` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `partners`
--

INSERT INTO `partners` (`id`, `name`, `image`) VALUES
(2, 'vishal', 'vishal_photo_2.jpg'),
(3, 'vishal2', 'vishal_photo_2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `team`
--

CREATE TABLE `team` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `team`
--

INSERT INTO `team` (`id`, `name`, `designation`, `image`, `description`) VALUES
(1, 'Monika maam', 'Founder', 'founder.jpg', 'Founder of Bright Future Foundation.'),
(2, 'Anjali Sharma', 'Education Coordinator', 'teacher.jpg', 'Manages education programs.'),
(3, 'Vishal Prajapati', 'Volunteer', 'vishal_photo_2.jpg', 'Helps children with daily classes.'),
(5, 'Ravi', 'Volunteer', '', 'help education');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `analytics`
--
ALTER TABLE `analytics`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `donation`
--
ALTER TABLE `donation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gallery`
--
ALTER TABLE `gallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `partners`
--
ALTER TABLE `partners`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics`
--
ALTER TABLE `analytics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=184;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `donation`
--
ALTER TABLE `donation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `gallery`
--
ALTER TABLE `gallery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `partners`
--
ALTER TABLE `partners`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `team`
--
ALTER TABLE `team`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
