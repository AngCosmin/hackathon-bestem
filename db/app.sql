-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Gazdă: db
-- Timp de generare: apr. 08, 2019 la 08:58 AM
-- Versiune server: 5.7.25
-- Versiune PHP: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Bază de date: `app`
--

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `badges`
--

CREATE TABLE `badges` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `icon` varchar(300) DEFAULT 'https://icon2.kisspng.com/20180131/wye/kisspng-question-mark-icon-question-mark-5a7214f27444f6.1205009215174259064763.jpg',
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `badges`
--

INSERT INTO `badges` (`id`, `name`, `description`, `icon`, `points`) VALUES
(1, 'Recycle novice', 'First place cleaned', 'https://i.imgur.com/9AuUUB6.png', 10),
(3, 'Junior reported', 'Three dirty areas reported', 'https://i.imgur.com/dwoYaxA.png', 10),
(4, 'Inviter pro', 'Invited 5 friends to clean together', 'https://i.imgur.com/tjrU1kA.png', 10),
(5, 'Cleaner worrior', 'Clean 10 places', 'https://i.imgur.com/SepvR91.png', 20),
(6, 'Recycle master', 'Cleaned 20 places', 'https://i.imgur.com/uqhbBDL.png', 30),
(7, 'Reported master', 'Reported 20 dirty areas', 'https://i.imgur.com/BhMKqSQ.png', 30),
(8, 'Trash detective', 'Find 30 dirty places', 'https://i.imgur.com/J54WgyP.png', 40),
(9, 'City Superhero', 'Attended 50 events', 'https://i.imgur.com/jgZSku4.png', 50),
(10, 'Hero of the zone', 'Mark 30 places as cleaned', 'https://i.imgur.com/TeP44tC.png', 100);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `pin_id` int(11) DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `description` text,
  `time_start` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `time_end` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `events`
--

INSERT INTO `events` (`id`, `pin_id`, `lat`, `lng`, `title`, `description`, `time_start`, `time_end`) VALUES
(1, 1, 44.436164, 26.051749, 'Let\'s clean the Old Town', 'Trebuie stranse sticlele de plastic si duse la centrul de reciclare.', '2019-04-05 10:30:00', '2019-04-05 19:30:00'),
(2, 6, 44.472069, 26.084557, 'Sa curatam Parcul Herastrau dupa furtuna', NULL, '2019-04-08 10:00:00', '2019-04-08 16:00:00'),
(3, 5, NULL, NULL, 'Studentii curata campusul', 'Studentii de la Automatica si Calculatoare vor curata campusul UPB.', '2019-04-26 10:00:00', '2019-04-26 16:00:00'),
(4, 4, NULL, NULL, 'Coji de seminte in parc', 'Avem nevoie de 5 voluntari pentru a curata Parcul Tineretului de cojile de seminte.', '2019-04-10 06:00:00', '2019-04-10 11:00:00'),
(5, 7, NULL, NULL, 'event', 'gcfxc', '2019-04-12 07:38:00', '2019-04-16 07:37:00'),
(6, 6, NULL, NULL, 'Event', 'vgxcs`', '2019-04-18 07:58:00', '2019-04-19 07:58:00'),
(7, 5, NULL, NULL, 'Cleanup', 'ghfxchg`cs', '2019-04-18 08:11:00', '2019-04-27 08:11:00'),
(8, 10, NULL, NULL, 'hgxcvg`jc', 'vxgsvmca', '2019-04-11 09:56:00', '2019-04-13 09:58:00');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `pictures`
--

CREATE TABLE `pictures` (
  `id` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `pin_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `pictures`
--

INSERT INTO `pictures` (`id`, `url`, `pin_id`) VALUES
(2, 'https://i.imgur.com/Mgu5zmq.jpg', 4),
(3, 'https://i.imgur.com/rFiUHuG.jpg', 5),
(4, 'https://i.imgur.com/spBvYlQ.jpg', 1),
(5, 'https://i.imgur.com/vFVYVr7.jpg', 1),
(6, 'https://i.imgur.com/aaI5CEo.png', 7),
(7, 'https://i.imgur.com/oI4IKLj.png', 4),
(8, 'https://i.imgur.com/mabG7R8.jpg', 8),
(9, 'https://i.imgur.com/GpFAB64.jpg', 5),
(10, 'https://i.imgur.com/7xlZ4Eg.jpg', 9),
(11, 'https://i.imgur.com/NG2MqTU.jpg', 10),
(12, 'https://i.imgur.com/ZZG5yuf.jpg', 1);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `pins`
--

CREATE TABLE `pins` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `lat` double DEFAULT NULL,
  `lng` double DEFAULT NULL,
  `cleaned` tinyint(1) NOT NULL DEFAULT '0',
  `title` varchar(100) DEFAULT NULL,
  `description` text,
  `type` int(11) NOT NULL DEFAULT '1',
  `status` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `pins`
--

INSERT INTO `pins` (`id`, `user_id`, `lat`, `lng`, `cleaned`, `title`, `description`, `type`, `status`, `created_at`, `updated_at`) VALUES
(1, 1, 44.436164, 26.051749, 0, 'Centrul Vechi', 'Curatare pet-uri', 1, 2, '2019-04-06 09:39:41', '2019-04-06 09:39:41'),
(2, 4, 44.403356, 26.180167, 0, '', NULL, 2, 0, '2019-04-06 14:13:32', '2019-04-06 14:13:32'),
(3, 5, 44.409454, 26.088854, 0, NULL, NULL, 2, 0, '2019-04-06 14:26:25', '2019-04-06 14:26:25'),
(4, 3, 44.402576, 26.107389, 0, 'Parcul Tineretului ', 'Cosurile de gunoi din parc sunt pline si gunoiul este pe langa ele.', 1, 2, '2019-04-06 14:30:01', '2019-04-06 14:30:01'),
(5, 2, 44.435516, 26.047277, 0, 'Campus Universitatea Politehnica', 'Campusul Universitatii Politehnica este plin de pet-uri aruncate pe langa Facultatea de Automatica si Calculatoare.', 1, 0, '2019-04-06 14:31:44', '2019-04-06 14:31:44'),
(6, 1, 44.472069, 26.084557, 0, 'Crengi Parcul Herastrau', 'Sunt multe crengi rupte in parc de dupa furtuna de sambata.', 1, 0, '2019-04-06 14:32:46', '2019-04-06 14:32:46'),
(7, 2, 44.467494447139, 26.1277048897131, 0, 'vhgxdvaU', 'GXFHA', 1, 2, '2019-04-07 10:36:58', '2019-04-07 10:36:58'),
(8, 2, 44.4546605732423, 26.0131301564064, 0, 'Lacul morii', 'dac``a', 1, 2, '2019-04-07 11:11:04', '2019-04-07 11:11:04'),
(9, 2, 44.480983857448, 26.1025536638584, 0, 'Mihael;a', 'vgcxsmsa', 1, 0, '2019-04-07 12:56:15', '2019-04-07 12:56:15'),
(10, 2, 44.480983857448, 26.1025536638584, 0, 'Mihael;a', 'vgcxsmsa', 1, 0, '2019-04-07 12:56:23', '2019-04-07 12:56:23'),
(11, 2, 44.4425304882901, 26.0591212805811, 0, 'sadsada', '', 1, 0, '2019-04-08 11:48:56', '2019-04-08 11:48:56'),
(12, 2, 44.4425304882901, 26.0591212805811, 0, 'sadsada', '', 1, 0, '2019-04-08 11:49:06', '2019-04-08 11:49:06'),
(13, 2, 44.4425304882901, 26.0591212805811, 0, 'sadsada', '', 1, 1, '2019-04-08 11:49:20', '2019-04-08 11:49:20');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'volunteer'),
(2, 'collector'),
(3, 'administrator');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `info` varchar(300) DEFAULT NULL,
  `places_cleaned` int(11) NOT NULL DEFAULT '0',
  `places_reported` int(11) NOT NULL DEFAULT '0',
  `avatar` varchar(200) NOT NULL DEFAULT 'https://i.imgur.com/qfl54GP.png',
  `points` int(11) NOT NULL DEFAULT '0',
  `status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `users`
--

INSERT INTO `users` (`id`, `role_id`, `email`, `password`, `name`, `phone`, `info`, `places_cleaned`, `places_reported`, `avatar`, `points`, `status`) VALUES
(1, 1, 'ioanamoraru14@gmail.com', 'ioana123', 'Ioana Moraru', NULL, NULL, 7, 0, 'https://i.imgur.com/jFtGaa7.jpg', 210, 0),
(2, 1, 'cosminzorr@gmail.com', 'cosmin', 'Anghel Cosmin', NULL, NULL, 7, 8, 'https://i.imgur.com/Sb1f65J.jpg', 210, 1),
(3, 3, 'catrina.mihaela20@gmail.com', 'miha', 'Catrina Mihaela', NULL, NULL, 7, 0, 'https://i.imgur.com/sZr0qk5.jpg', 210, 2),
(4, 2, 'office@profisesreciclare.ro', 'centru1', 'PROFI SES RECICLARE', '0737 412 840', 'Program <br> L-V: 9-17', 7, 0, 'https://i.imgur.com/d4PYpjS.jpg', 210, 0),
(5, 2, 'bismark_solutions@gmail.com', 'centru2', 'Bismark Solutions', '0725698123', 'Program <br> L-S: 8:00-19:00 <br>\r\nD: inchis', 7, 0, 'https://i.imgur.com/54uSfZ3.jpg', 210, 0),
(6, 1, 'volunteer14@gmail.com', 'volunteer', 'Voluntar', NULL, NULL, 7, 0, 'https://i.imgur.com/qfl54GP.png', 210, 1);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `users_badges`
--

CREATE TABLE `users_badges` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `badge_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `users_badges`
--

INSERT INTO `users_badges` (`id`, `user_id`, `badge_id`) VALUES
(9, 2, 7),
(11, 3, 1),
(12, 3, 4),
(13, 2, 8),
(15, 2, 5),
(16, 2, 9),
(17, 2, 9);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `users_events`
--

CREATE TABLE `users_events` (
  `id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `invited_by_id` int(11) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `users_events`
--

INSERT INTO `users_events` (`id`, `event_id`, `user_id`, `invited_by_id`, `status`) VALUES
(15, 4, 2, NULL, 0),
(17, 1, 2, NULL, 0),
(18, 1, 1, NULL, 0),
(19, 8, 2, NULL, 0);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `users_friends`
--

CREATE TABLE `users_friends` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `users_friends`
--

INSERT INTO `users_friends` (`id`, `user_id`, `friend_id`) VALUES
(12, 2, 1);

--
-- Indexuri pentru tabele eliminate
--

--
-- Indexuri pentru tabele `badges`
--
ALTER TABLE `badges`
  ADD PRIMARY KEY (`id`);

--
-- Indexuri pentru tabele `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_event_pin` (`pin_id`);

--
-- Indexuri pentru tabele `pictures`
--
ALTER TABLE `pictures`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pict_pins` (`pin_id`);

--
-- Indexuri pentru tabele `pins`
--
ALTER TABLE `pins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pins_users` (`user_id`);

--
-- Indexuri pentru tabele `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexuri pentru tabele `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_users_roles` (`role_id`);

--
-- Indexuri pentru tabele `users_badges`
--
ALTER TABLE `users_badges`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_badge_user` (`badge_id`),
  ADD KEY `fk_user_badge` (`user_id`);

--
-- Indexuri pentru tabele `users_events`
--
ALTER TABLE `users_events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user` (`user_id`),
  ADD KEY `fk_event` (`event_id`);

--
-- Indexuri pentru tabele `users_friends`
--
ALTER TABLE `users_friends`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_users` (`user_id`),
  ADD KEY `fk_friends` (`friend_id`);

--
-- AUTO_INCREMENT pentru tabele eliminate
--

--
-- AUTO_INCREMENT pentru tabele `badges`
--
ALTER TABLE `badges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pentru tabele `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pentru tabele `pictures`
--
ALTER TABLE `pictures`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pentru tabele `pins`
--
ALTER TABLE `pins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pentru tabele `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pentru tabele `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pentru tabele `users_badges`
--
ALTER TABLE `users_badges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pentru tabele `users_events`
--
ALTER TABLE `users_events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT pentru tabele `users_friends`
--
ALTER TABLE `users_friends`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constrângeri pentru tabele eliminate
--

--
-- Constrângeri pentru tabele `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `fk_event_pin` FOREIGN KEY (`pin_id`) REFERENCES `pins` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `pictures`
--
ALTER TABLE `pictures`
  ADD CONSTRAINT `fk_pict_pins` FOREIGN KEY (`pin_id`) REFERENCES `pins` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `pins`
--
ALTER TABLE `pins`
  ADD CONSTRAINT `fk_pins_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `users_badges`
--
ALTER TABLE `users_badges`
  ADD CONSTRAINT `fk_badge_user` FOREIGN KEY (`badge_id`) REFERENCES `badges` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user_badge` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `users_events`
--
ALTER TABLE `users_events`
  ADD CONSTRAINT `fk_event` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constrângeri pentru tabele `users_friends`
--
ALTER TABLE `users_friends`
  ADD CONSTRAINT `fk_friends` FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
