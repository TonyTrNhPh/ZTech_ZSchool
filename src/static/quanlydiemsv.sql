DROP DATABASE IF EXISTS `ZSchool`;
CREATE DATABASE ZSchool CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ZSchool;

-- Table structure for table `users`
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `UserType` enum('Giáo viên','Sinh viên','Quản trị viên') NOT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `announcements`
DROP TABLE IF EXISTS `announcements`;
CREATE TABLE `announcements` (
  `AnnouncementID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) DEFAULT NULL,
  `Title` text NOT NULL,
  `Description` text NOT NULL,
  `Who` enum('Giáo viên','Sinh viên','Tất cả') NOT NULL,
  `Date` datetime NOT NULL,
  `Published` boolean NOT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`AnnouncementID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `announcements_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table structure for table `students`
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `StudentID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) DEFAULT NULL,
  `FullName` varchar(100) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Gender` enum('Nam','Nữ','Khác') NOT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`StudentID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `teachers`
DROP TABLE IF EXISTS `teachers`;
CREATE TABLE `teachers` (
  `TeacherID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) DEFAULT NULL,
  `FullName` varchar(100) NOT NULL,
  `Department` varchar(100) NOT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`TeacherID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `courses`
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `CourseID` int(11) NOT NULL AUTO_INCREMENT,
  `CourseName` varchar(100) NOT NULL,
  `TeacherID` int(11) DEFAULT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`CourseID`),
  KEY `TeacherID` (`TeacherID`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`TeacherID`) REFERENCES `teachers` (`TeacherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `grades`
DROP TABLE IF EXISTS `grades`;
CREATE TABLE `grades` (
  `GradeID` int(11) NOT NULL AUTO_INCREMENT,
  `StudentID` int(11) DEFAULT NULL,
  `CourseID` int(11) DEFAULT NULL,
  `Grade` float NOT NULL,
  `Status` boolean NOT NULL,
  PRIMARY KEY (`GradeID`),
  KEY `StudentID` (`StudentID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`StudentID`) REFERENCES `students` (`StudentID`),
  CONSTRAINT `grades_ibfk_2` FOREIGN KEY (`CourseID`) REFERENCES `courses` (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `course_documents`
DROP TABLE IF EXISTS `course_documents`;
CREATE TABLE `course_documents` (
    `DocumentID` INT(11) NOT NULL AUTO_INCREMENT,
    `DocumentName` VARCHAR(100) NOT NULL,
    `Supplier` VARCHAR(100) NOT NULL,
    `Year` INT(4) NOT NULL,
    `CourseID` INT(11) NOT NULL,
    PRIMARY KEY (`DocumentID`),
    KEY `CourseID` (`CourseID`),
    CONSTRAINT `fk_course_document_course` FOREIGN KEY (`CourseID`)
        REFERENCES `courses` (`CourseID`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE = UTF8MB4_GENERAL_CI;

-- Table structure for table `course_feedback`
DROP TABLE IF EXISTS `course_feedback`;
CREATE TABLE `course_feedback` (
  `FeedbackID` int(11) NOT NULL AUTO_INCREMENT,
  `CourseID` int(11) NOT NULL,
  `Rating` int(11) NOT NULL,
  `Comment` text,
  PRIMARY KEY (`FeedbackID`),
  CONSTRAINT `fk_course_feedback_course` FOREIGN KEY (`CourseID`) REFERENCES `courses` (`CourseID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `attendance`
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance` (
  `AttendanceID` INT(11) NOT NULL AUTO_INCREMENT,
  `CourseID` INT(11) NOT NULL,
  `Date` DATE NOT NULL,
  `Status` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`AttendanceID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `fk_attendance_course` FOREIGN KEY (`CourseID`)
        REFERENCES `courses` (`CourseID`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE = UTF8MB4_GENERAL_CI;

