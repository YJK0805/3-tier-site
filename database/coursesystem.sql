-- 建立課程表格
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
(1272, '班級活動', '資訊', '一', '資訊一甲', 0, 'R', 60, 60, '劉怡芬'),
(1274, '現代公民與社會實踐', '資訊', '一', '資訊一甲', 2, 'R', 60, 60, '陳迪暉'),
(1279, '微積分(二)', '資訊', '一', '資訊一甲', 3, 'R', 60, 60, '王志雄'),
(1280, '線性代數', '資訊', '一', '資訊一甲', 3, 'R', 60, 60, '林佩君'),
(1283, '班級活動', '資訊', '一', '資訊一乙', 0, 'R', 60, 54, '劉明機'),
(1285, '現代公民與社會實踐', '資訊', '一', '資訊一乙', 2, 'R', 60, 57, '王謙'),
(1290, '微積分(二)', '資訊', '一', '資訊一乙', 3, 'R', 60, 57, '林佩君'),
(1294, '班級活動', '資訊', '一', '資訊一丙', 0, 'R', 60, 60, '郭崇韋'),
(1295, '體育(二)', '資訊', '一', '資訊一丙', 1, 'R', 60, 59, '張宜正'),
(1297, '程式設計', '資訊', '一', '資訊一丙', 2, 'R', 60, 60, '郭崇韋'),
(1305, '程式設計', '資訊', '一', '資訊一合', 2, 'R', 30, 30, '林佩蓉'),
(1308, '系統程式', '資訊', '二', '資訊二甲', 3, 'R', 60, 60, '周兆龍'),
(1309, '資料庫系統', '資訊', '二', '資訊二甲', 3, 'R', 60, 60, '林明言'),
(1310, '機率與統計', '資訊', '二', '資訊二甲', 3, 'R', 60, 60, '劉怡芬'),
(1312, '系統程式', '資訊', '二', '資訊二乙', 3, 'R', 60, 60, '劉宗杰'),
(1313, '資料庫系統', '資訊', '二', '資訊二乙', 3, 'R', 60, 60, '許懷中'),
(1314, '機率與統計', '資訊', '二', '資訊二乙', 3, 'R', 60, 60, '游景盛'),
(1316, '系統程式', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '劉宗杰'),
(1317, '資料庫系統', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '林明言'),
(1318, '機率與統計', '資訊', '二', '資訊二丙', 3, 'R', 60, 60, '游景盛'),
(1320, '系統程式', '資訊', '二', '資訊二丁', 3, 'R', 60, 60, '周兆龍'),
(1321, '資料庫系統', '資訊', '二', '資訊二丁', 3, 'R', 60, 60, '葉春秀'),
(1322, '機率與統計', '資訊', '二', '資訊二丁', 3, 'R', 60, 60, '劉怡芬'),
(1329, '電子商務安全', '資訊', '二', '資訊二乙', 3, 'E', 60, 60, '魏國瑞'),
(1348, '人工智慧導論', '資訊', '三', '資訊三乙', 3, 'E', 60, 58, '林峰正'),
(1351, '人工智慧自然語言導論', '資訊', '三', '資訊三甲', 3, 'E', 60, 50, '林哲維'),
(1352, '行動應用程式開發', '資訊', '三', '資訊三丙', 3, 'E', 60, 48, '陳錫民'),
(1356, '嵌入式系統', '資訊', '三', '資訊三丙', 3, 'E', 60, 47, '蔡明峰'),
(1359, '程式語言', '資訊', '三', '資訊三乙', 3, 'E', 60, 57, '吳育倫'),
(1361, '資訊實務案例探討', '資訊', '三', '資訊三丁', 2, 'E', 60, 53, '吳上玄'),
(1362, '資訊安全管理', '資訊', '三', '資訊三甲', 3, 'E', 60, 28, '陳星百');

-- 建立課程時間表格
CREATE TABLE IF NOT EXISTS coursetime (
    course_code INT,
    day_of_week VARCHAR(255),
    start_period INT,
    end_period INT,
    FOREIGN KEY (course_code) REFERENCES course(course_code)
);

-- 將課程時間資料寫入課程時間表格
INSERT INTO coursetime (course_code, day_of_week, start_period, end_period)
VALUES
(1272, '一', 8, 9),
(1274, '一', 3, 4),
(1279, '一', 6, 7),
(1279, '三', 8, 8),
(1280, '一', 10, 10),
(1280, '三', 9, 10),
(1283, '一', 8, 9),
(1285, '一', 3, 4),
(1290, '一', 6, 7),
(1290, '四', 6, 6),
(1294, '一', 8, 9),
(1295, '一', 6, 7),
(1297, '一', 3, 4),
(1297, '二', 1, 4),
(1305, '一', 11, 14),
(1305, '三', 6, 7),
(1308, '一', 8, 9),
(1308, '三', 4, 4),
(1309, '一', 6, 7),
(1309, '二', 3, 3),
(1310, '一', 3, 4),
(1310, '二', 4, 4),
(1312, '一', 3, 4),
(1312, '三', 4, 4),
(1313, '一', 8, 9),
(1313, '二', 3, 3),
(1314, '一', 6, 7),
(1314, '二', 4, 4),
(1316, '一', 6, 7),
(1316, '三', 3, 3),
(1317, '一', 3, 4),
(1317, '二', 4, 4),
(1318, '一', 8, 9),
(1318, '二', 3, 3),
(1320, '一', 3, 4),
(1320, '三', 3, 3),
(1321, '一', 8, 9),
(1321, '五', 6, 6),
(1322, '一', 6, 7),
(1322, '五', 2, 2),
(1329, '一', 11, 13),
(1348, '一', 2, 4),
(1351, '一', 6, 8),
(1352, '一', 6, 8),
(1356, '一', 2, 4),
(1359, '一', 11, 13),
(1361, '一', 8, 9),
(1362, '一', 11, 13);

-- 建立關注表格
CREATE TABLE IF NOT EXISTS focus (
    student_class VARCHAR(255),
    student_id VARCHAR(255),
    student_name VARCHAR(255),
    focused_course_code INT,
    FOREIGN KEY (focused_course_code) REFERENCES course(course_code)
);

-- 將關注資料寫入關注表格
-- INSERT INTO focus (student_class, student_id, student_name, focused_course_code)
-- VALUES
-- 插入關注資料，注意格式

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
-- INSERT INTO selected_course (student_id, student_name, student_class, credits_selected, selected_course_code)
-- VALUES
-- 插入選課資料，注意格式

-- 建立學生表格
CREATE TABLE IF NOT EXISTS students (
    student_name VARCHAR(255),
    student_id VARCHAR(255) PRIMARY KEY,
    student_class VARCHAR(255),
    credits_selected INT,
    password VARCHAR(255)
);

-- 將學生資料寫入學生表格
INSERT INTO students (student_name, student_id, student_class, credits_selected, password)
VALUES
('admin', 'D0000000', '資訊四乙', 0, 'password');

