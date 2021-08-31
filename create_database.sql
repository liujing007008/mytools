DROP TABLE IF EXISTS oa;
CREATE TABLE IF NOT EXISTS `oa`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

#--创建测试表
DROP TABLE IF EXISTS test;
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modify_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
#--检测默认值，插入测试数据
INSERT INTO `test` (name) VALUES ('11'),('22'),('33');
 
#--检测自动更新，更新某条数据
UPDATE `test` SET name = '12' WHERE id = 1;
	commit;


/*类型	大小	范围（有符号）	范围（无符号）	用途
TINYINT	1byte	(-128，127)	(0，255)	小整数值
SMALLINT	2bytes	(-32768，32767)	(0，65535)	大整数值
MEDIUMINT	3bytes	(-8388608，8388607)	(0，16777215)	大整数值
INT或INTEGER	4bytes	(-2147483648，2147483647)	(0，4294967295)	大整数值
BIGINT	8bytes	(-9,223,372,036,854,775,808，9223372036854775807)	(0，18446744073709551615)	极大整数值
FLOAT	4bytes	(-3.402823466E+38，-1.175494351E-38)，0，(1.175494351E-38，3.402823466351E+38)	0，(1.175494351E-38，3.402823466E+38)	单精度
浮点数值
DOUBLE	8bytes	(-1.7976931348623157E+308，-2.2250738585072014E-308)，0，(2.2250738585072014E-308，1.7976931348623157E+308)	0，(2.2250738585072014E-308，1.7976931348623157E+308)	双精度
浮点数值
DECIMAL	对DECIMAL(M,D)，如果M>D，为M+2否则为D+2	依赖于M和D的值	依赖于M和D的值	小数值
DATE	3	1000-01-01/9999-12-31	YYYY-MM-DD	日期值
TIME	3	'-838:59:59'/'838:59:59'	HH:MM:SS	时间值或持续时间
YEAR	1	1901/2155	YYYY	年份值
DATETIME	8	1000-01-0100:00:00/9999-12-3123:59:59	YYYY-MM-DDHH:MM:SS	混合日期和时间值
TIMESTAMP	4	
1970-01-0100:00:00/2038

结束时间是第2147483647秒，北京时间2038-1-1911:14:07，格林尼治时间2038年1月19日凌晨03:14:07

YYYYMMDDHHMMSS	混合日期和时间值，时间戳
CHAR	0-255bytes	定长字符串
VARCHAR	0-65535bytes	变长字符串
TINYBLOB	0-255bytes	不超过255个字符的二进制字符串
TINYTEXT	0-255bytes	短文本字符串
BLOB	0-65535bytes	二进制形式的长文本数据
TEXT	0-65535bytes	长文本数据
MEDIUMBLOB	0-16777215bytes	二进制形式的中等长度文本数据
MEDIUMTEXT	0-16777215bytes	中等长度文本数据
LONGBLOB	0-4294967295bytes	二进制形式的极大文本数据
LONGTEXT	0-4294967295bytes	极大文本数据
注意：char(n)和varchar(n)中括号中n代表字符的个数，并不代表字节个数，比如CHAR(30)就可以存储30个字符。CHAR和VARCHAR类型类似，但它们保存和检索的方式不同。它们的最大长度和是否尾部空格被保留等方面也不同。在存储或检索过程中不进行大小写转换。BINARY和VARBINARY类似于CHAR和VARCHAR，不同的是它们包含二进制字符串而不要非二进制字符串。也就是说，它们包含字节字符串而不是字符字符串。这说明它们没有字符集，并且排序和比较基于列值字节的数值值。BLOB是一个二进制大对象，可以容纳可变数量的数据。有4种BLOB类型：TINYBLOB、BLOB、MEDIUMBLOB和LONGBLOB。它们区别在于可容纳存储范围不同。有4种TEXT类型：TINYTEXT、TEXT、MEDIUMTEXT和LONGTEXT。对应的这4种BLOB类型，可存储的最大长度不同，可根据实际情况选择。
*/