-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2022 at 11:05 PM
-- Server version: 5.7.17
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `people`
--

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

CREATE TABLE `people` (
  `NIN` varchar(9) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `email` varchar(64) NOT NULL,
  `tel` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `people`
--

INSERT INTO `people` (`NIN`, `nom`, `prenom`, `email`, `tel`) VALUES
('1', 'Herouini', 'Mohamed', 'mohamed.herouini@univ-constantine2.dz', '0779701922'),
('2', 'Bouzenzana', 'Abdeldjalil', 'abdeldjalil.bouzenzana@univ-constantine2.dz', '0551916821'),
('3', 'Chenafi', 'seif', 'seifeddine.chenafi@univ-constantine2.dz', '0778791500'),
('4', 'Bouregbi', 'seif', 'seifeddine.bouragbi@univ-constantine2.dz', '078645321'),
('5', 'Benarab', 'islem', 'islem.benarab@univ-constantine2.dz', '056705432'),
('6', 'Boubiasli', 'mohamed', 'mohamed.boubiasli@univ-constantine2.dz', '072321567');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `people`
--
ALTER TABLE `people`
  ADD PRIMARY KEY (`NIN`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
