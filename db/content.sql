/*
Navicat MySQL Data Transfer

Source Server         : @localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : nihaowua

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-03-06 14:49:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for content
-- ----------------------------
DROP TABLE IF EXISTS `content`;
CREATE TABLE `content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;
