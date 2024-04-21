﻿-- 建立課程表格
CREATE TABLE IF NOT EXISTS course (
    course_code INT PRIMARY KEY,
    course_name VARCHAR(255),
    department VARCHAR(255),
    grade VARCHAR(255),
    class_name VARCHAR(255),
    credits INT,
    compulsory VARCHAR(255),
    total_students INT,
    enrolled_students INT,
    instructor VARCHAR(255)
);

-- 將課程資料寫入課程表格
INSERT INTO course (course_code, course_name, department, grade, class_name, credits, compulsory, total_students, enrolled_students, instructor)
VALUES
(108, '經濟學(二)', '會計', '一', '會計一乙', 3, 'R', 65, 47, '彭德昭'),
(125, '租稅法', '會計', '二', '會計二甲', 3, 'R', 65, 63, '黃鋒榮'),
(218, '管理學', '國貿', '一', '國貿一丙', 3, 'R', 80, 69, '劉世慶'),
(268, '國際市場開發與管理', '國貿', '四', '國貿四乙', 3, 'E', 60, 23, '黃秀英'),
(307, '保險學', '財金', '二', '財金二甲', 3, 'R', 80, 80, '吳仰哲'),
(376, '金融資訊系統', '風保', '二', '風保二甲', 3, 'R', 60, 60, '宮可倫'),
(1272, '班級活動', '資訊', '一', '資訊一甲', 0, 'R', 30, 28, '劉怡芬'),
(1273, '體育(二)', '資訊', '一', '資訊一甲', 1, 'R', 30, 29, '黃嘉君'),
(1274, '現代公民與社會實踐', '資訊', '一', '資訊一甲', 2, 'R', 30, 28, '陳迪暉'),
(1275, '程式設計', '資訊', '一', '資訊一甲', 2, 'R', 60, 58, '蔡國裕'),
(1277, '普通物理-電、磁、光實驗', '資訊', '一', '資訊一甲', 1, 'R', 60, 58, '蔡雅芝'),
(1278, '微積分(二)實習', '資訊', '一', '資訊一甲', 0, 'R', 60, 56, '張志偉'),
(1279, '微積分(二)', '資訊', '一', '資訊一甲', 3, 'R', 60, 56, '王志雄'),
(1280, '線性代數', '資訊', '一', '資訊一甲', 3, 'R', 60, 56, '林佩君'),
(1281, '邏輯設計', '資訊', '一', '資訊一甲', 3, 'R', 60, 60, '陳德生'),
(1282, '邏輯設計實習', '資訊', '一', '資訊一甲', 1, 'R', 60, 60, '陳德生'),
(1283, '班級活動', '資訊', '一', '資訊一乙', 0, 'R', 60, 58, '劉明機'),
(1284, '體育(二)', '資訊', '一', '資訊一乙', 1, 'R', 60, 56, '黃嘉君'),
(1285, '現代公民與社會實踐', '資訊', '一', '資訊一乙', 2, 'R', 60, 60, '陳迪暉'),
(1286, '程式設計', '資訊', '一', '資訊一乙', 2, 'R', 60, 58, '劉明機'),
(1288, '普通物理-電、磁、光實驗', '資訊', '一', '資訊一乙', 1, 'R', 60, 58, '蔡雅芝'),
(1289, '微積分(二)實習', '資訊', '一', '資訊一乙', 0, 'R', 30, 30, '張志偉'),
(1290, '微積分(二)', '資訊', '一', '資訊一乙', 3, 'R', 30, 30, '王志雄'),
(1291, '線性代數', '資訊', '一', '資訊一乙', 3, 'R', 30, 30, '林佩君'),
(1292, '邏輯設計', '資訊', '一', '資訊一乙', 3, 'R', 30, 30, '陳德生'),
(1293, '邏輯設計實習', '資訊', '一', '資訊一乙', 1, 'R', 30, 30, '陳德生'),
(1294, '班級活動', '資訊', '一', '資訊一丙', 0, 'R', 60, 60, '郭崇韋'),
(1295, '體育(二)', '資訊', '一', '資訊一丙', 1, 'R', 60, 59, '張宜正'),
(1296, '現代公民與社會實踐', '資訊', '一', '資訊一丙', 2, 'R', 60, 60, '秦俊'),
(1297, '程式設計', '資訊', '一', '資訊一丙', 2, 'R', 60, 58, '郭崇韋'),
(1299, '普通物理-電、磁、光實驗', '資訊', '一', '資訊一丙', 1, 'R', 65, 62, '方淳民'),
(1300, '微積分(二)實習', '資訊', '一', '資訊一丙', 0, 'R', 60, 58, '張志偉'),
(1301, '微積分(二)', '資訊', '一', '資訊一丙', 3, 'R', 60, 60, '黃新峰'),
(1302, '線性代數', '資訊', '一', '資訊一丙', 3, 'R', 60, 60, '林佩君'),
(1303, '邏輯設計', '資訊', '一', '資訊一丙', 3, 'R', 60, 60, '王益文'),
(1304, '邏輯設計實習', '資訊', '一', '資訊一丙', 1, 'R', 60, 60, '王益文'),
(1305, '程式設計', '資訊', '一', '資訊一合', 2, 'R', 60, 54, '林佩蓉'),
(1307, '班級活動', '資訊', '二', '資訊二甲', 0, 'R', 60, 64, '林佩君'),
(1308, '系統程式', '資訊', '二', '資訊二甲', 3, 'R', 60, 55, '周兆龍'),
(1309, '資料庫系統', '資訊', '二', '資訊二甲', 3, 'R', 60, 58, '林明言'),
(1310, '機率與統計', '資訊', '二', '資訊二甲', 3, 'R', 60, 55, '劉怡芬'),
(1311, '班級活動', '資訊', '二', '資訊二乙', 0, 'R', 60, 60, '洪振偉'),
(1312, '系統程式', '資訊', '二', '資訊二乙', 3, 'R', 60, 58, '劉宗杰'),
(1313, '資料庫系統', '資訊', '二', '資訊二乙', 3, 'R', 60, 60, '許懷中'),
(1314, '機率與統計', '資訊', '二', '資訊二乙', 3, 'R', 60, 60, '游景盛'),
(1315, '班級活動', '資訊', '二', '資訊二丙', 0, 'R', 60, 58, '李俊宏'),
(1316, '系統程式', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '劉宗杰'),
(1317, '資料庫系統', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '林明言'),
(1318, '機率與統計', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '游景盛'),
(1319, '班級活動', '資訊', '二', '資訊二丁', 0, 'R', 60, 60, '葉春秀'),
(1320, '系統程式', '資訊', '三', '資訊二丁', 3, 'R', 60, 58, '周兆龍'),
(1321, '資料庫系統', '資訊', '三', '資訊二丁', 3, 'R', 60, 58, '葉春秀'),
(1322, '機率與統計', '資訊', '三', '資訊二丁', 3, 'R', 60, 57, '劉怡芬'),
(1323, '互連網路', '資訊', '三', '資訊二合', 3, 'E', 60, 39, '劉宗杰'),
(1324, 'Web程式設計', '資訊', '三', '資訊二合', 3, 'E', 60, 54, '劉明機'),
(1325, 'Web程式設計', '資訊', '三', '資訊二合', 3, 'E', 60, 59, '薛念林'),
(1326, '系統分析與設計', '資訊', '三', '資訊二合', 3, 'E', 60, 36, '洪振偉'),
(1327, '系統分析與設計', '資訊', '三', '資訊二合', 3, 'E', 60, 55, '洪振偉'),
(1328, '多媒體系統', '資訊', '三', '資訊二合', 3, 'E', 60, 56, '葉春秀'),
(1329, '電子商務安全', '資訊', '三', '資訊二合', 3, 'E', 60, 58, '魏國瑞'),
(1330, '電子商務安全', '資訊', '三', '資訊二合', 3, 'E', 60, 55, '周澤捷'),
(1331, '數位信號處理導論', '資訊', '三', '資訊二合', 3, 'E', 60, 24, '陳啟鏘'),
(1332, '數位系統設計', '資訊', '三', '資訊二合', 3, 'E', 55, 54, '陳德生'),
(1333, '數位系統設計實驗', '資訊', '三', '資訊二合', 1, 'E', 55, 54, '陳德生'),
(1334, 'UNIX應用與實務', '資訊', '二', '資訊二合', 2, 'E', 60, 60, '林佩蓉'),
(1335, 'UNIX應用與實務', '資訊', '二', '資訊二合', 2, 'E', 60, 58, '劉明機'),
(1336, '計算機結構學', '資訊', '三', '資訊三甲', 3, 'R', 60, 55, '陳青文'),
(1337, '計算機演算法', '資訊', '三', '資訊三甲', 3, 'R', 60, 60, '陳烈武'),
(1339, '計算機結構學', '資訊', '三', '資訊三乙', 3, 'R', 60, 60, '陳青文'),
(1340, '計算機演算法', '資訊', '三', '資訊三乙', 3, 'R', 60, 60, '黃秀芬'),
(1342, '計算機結構學', '資訊', '三', '資訊三丙', 3, 'R', 60, 60, '李俊宏'),
(1343, '計算機演算法', '資訊', '三', '資訊三丙', 3, 'R', 60, 60, '黃秀芬'),
(1345, '計算機結構學', '資訊', '三', '資訊三丁', 3, 'R', 60, 60, '郭崇韋'),
(1346, '計算機演算法', '資訊', '三', '資訊三丁', 3, 'R', 60, 60, '許芳榮'),
(1348, '人工智慧導論', '資訊', '三', '資訊三合', 3, 'E', 60, 55, '林峰正'),
(1349, '人工智慧導論', '資訊', '三', '資訊三合', 3, 'E', 60, 56, '張哲誠'),
(1350, '人工智慧導論', '資訊', '三', '資訊三合', 3, 'E', 60, 60, '林哲維'),
(1351, '人工智慧自然語言導論', '資訊', '三', '資訊三丁', 3, 'E', 60, 50, '林哲維'),
(1352, '行動應用程式開發', '資訊', '三', '資訊三合', 3, 'E', 60, 48, '陳錫民'),
(1353, '安全程式設計', '資訊', '三', '資訊三合', 3, 'E', 40, 39, '蔡國裕'),
(1354, '系統安全', '資訊', '三', '資訊三合', 3, 'E', 60, 32, '周兆龍'),
(1356, '嵌入式系統', '資訊', '三', '資訊三合', 3, 'E', 60, 47, '蔡明峰'),
(1357, '嵌入式系統', '資訊', '三', '資訊三合', 3, 'E', 60, 29, '陳啟鏘'),
(1358, '資訊系統實習', '資訊', '三', '資訊三合', 1, 'E', 60, 46, '王志雄'),
(1359, '資訊系統實習', '資訊', '三', '資訊三合', 1, 'E', 60, 37, '王志雄'),
(1360, '半導體製程導論', '資訊', '三', '資訊三合', 3, 'E', 60, 23, '鄭文宏'),
(1361, '半導體製程導論', '資訊', '三', '資訊三合', 3, 'E', 60, 24, '鄭文宏'),
(1362,'資訊安全管理','資訊','三','資訊三合',3,'E',60,28,'陳星百'),
(1363,'資訊安全管理','資訊','三','資訊三合',3,'E',60,34,'陳映親'),
(1365,'程式設計與問題解決','資訊','四','資訊四合',2,'E',60,58,'葉春秀'),
(1366,'智慧物聯網實務應用','資訊','四','資訊四合',3,'E',60,49,'何丞堯');

-- 建立課程時間表格
CREATE TABLE IF NOT EXISTS coursetime (
    course_code INT,
    day_of_week INT,
    start_period INT,
    end_period INT,
    FOREIGN KEY (course_code) REFERENCES course(course_code)
);

-- 將課程時間資料寫入課程時間表格
INSERT INTO coursetime (course_code, day_of_week, start_period, end_period)
VALUES
(108, '2', 2, 4),
(125, '4', 6, 8),
(218, '3', 6, 8),
(268, '3', 6, 8),
(307, '3', 6, 8),
(376, '5', 6, 8),
(1272, '1', 8, 9),
(1273, '4', 8, 9),
(1274, '1', 3, 4),
(1275, '2', 8, 9),
(1275, '5', 2, 5),
(1277, '3', 2, 4),
(1278, '4', 6, 7),
(1279, '1', 6, 7),
(1279, '3', 8, 8),
(1280, '1', 10, 10),
(1280, '3', 9, 10),
(1281, '2', 1, 1),
(1281, '3', 6, 7),
(1282, '2', 2, 4),
(1283, '1', 8, 9),
(1284, '2', 8, 9),
(1285, '1', 3, 4),
(1286, '3', 6, 7),
(1286, '4', 1, 4),
(1288, '3', 2, 4),
(1289, '4', 7, 8),
(1290, '1', 6, 7),
(1290, '4', 6, 6),
(1291, '5', 2, 4),
(1292, '4', 9, 10),
(1292, '5', 7, 7),
(1293, '5', 8, 10),
(1294, '1', 8, 9),
(1295, '1', 6, 7),
(1296, '3', 3, 4),
(1297, '1', 3, 4),
(1297, '2', 1, 4),
(1299, '2', 8, 10),
(1300, '4', 8, 9),
(1301, '3', 6, 6),
(1301, '4', 6, 7),
(1302, '3', 7, 8),
(1302, '4', 10, 10),
(1303, '3', 9, 10),
(1303, '4', 1, 1),
(1304, '4', 2, 4),
(1305, '1', 11, 14),
(1305, '3', 6, 7),
(1307, '2', 9, 9),
(1308, '1', 8, 9),
(1308, '3', 4, 4),
(1309, '1', 6, 7),
(1309, '2', 3, 3),
(1310, '1', 3, 4),
(1310, '2', 4, 4),
(1311, '2', 9, 9),
(1312, '1', 3, 4),
(1312, '3', 4, 4),
(1313, '1', 8, 9),
(1313, '2', 3, 3),
(1314, '1', 6, 7),
(1314, '2', 4, 4),
(1315, '2', 9, 9),
(1316, '1', 6, 7),
(1316, '3', 3, 3),
(1317, '1', 3, 4),
(1317, '2', 4, 4),
(1318, '1', 8, 9),
(1318, '2', 3, 3),
(1319, '2', 9, 9),
(1320, '1', 3, 4),
(1320, '3', 3, 3),
(1321, '1', 8, 9),
(1321, '5', 6, 6),
(1322, '1', 6, 7),
(1322, '5', 2, 2),
(1323, '3', 6, 8),
(1324, '3', 1, 3),
(1325, '2', 6, 7),
(1326, '3', 3, 3),
(1327, '3', 4, 4),
(1328, '2', 6, 8),
(1329, '1', 11, 13),
(1330, '3', 8, 10),
(1331, '2', 2, 2),
(1331, '4', 3, 4),
(1332, '2', 6, 7),
(1332, '4', 8, 8),
(1333, '4', 9, 10),
(1334, '5', 6, 7),
(1335, '4', 6, 7),
(1336, '2', 8, 8),
(1337, '2', 6, 7),
(1337, '5', 6, 6),
(1339, '3', 6, 6),
(1339, '5', 6, 7),
(1340, '2', 8, 9),
(1340, '3', 7, 7),
(1342, '2', 6, 6),
(1342, '3', 6, 7),
(1343, '2', 7, 7),
(1343, '3', 8, 9),
(1345, '2', 6, 7),
(1345, '3', 9, 9),
(1346, '3', 6, 8),
(1348, '1', 2, 4),
(1349, '5', 2, 4),
(1350, '5', 8, 10),
(1351, '1', 6, 8),
(1352, '1', 6, 8),
(1353, '4', 2, 4),
(1354, '4', 6, 6),
(1354, '5', 8, 9),
(1356, '1', 2, 4),
(1357, '4', 11, 13),
(1358, '2', 9, 10),
(1358, '3', 10, 10),
(1359, '1', 11, 13),
(1360, '4', 6, 8),
(1361, '1', 8, 9),
(1362, '1', 11, 13),
(1363, '5', 11, 13),
(1365, '4', 6, 7),
(1366, '2', 11, 13);

-- 建立關注表格
CREATE TABLE IF NOT EXISTS focus (
    student_class VARCHAR(255),
    student_id VARCHAR(255),
    student_name VARCHAR(255),
    focused_course_code INT,
    FOREIGN KEY (focused_course_code) REFERENCES course(course_code)
);

-- 將關注資料寫入關注表格

-- 建立選課表格
CREATE TABLE IF NOT EXISTS selected_course (
    student_id VARCHAR(255),
    student_name VARCHAR(255),
    student_class VARCHAR(255),
    credits_selected INT,
    selected_course_code INT,
    FOREIGN KEY (selected_course_code) REFERENCES course(course_code)
);

-- 將選課資料寫入選課表格

-- 建立學生表格
CREATE TABLE IF NOT EXISTS students (
    student_name VARCHAR(255),
    student_id VARCHAR(255) PRIMARY KEY,
    department VARCHAR(255),
    student_class VARCHAR(255),
    credits_selected INT,
    password VARCHAR(255)
);

-- 將學生資料寫入學生表格
