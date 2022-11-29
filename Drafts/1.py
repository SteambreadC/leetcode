import pymysql

if __name__ == '__main__':
    # 打开数据库连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="1234", db="adbs")
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 通过open（）方法以只读的方式打开文件，编码格式为UTF-8
    file = open("E:\\OneDrive - nyu.edu\\文档\\2022 Fall\\Adbs\\HW2\\friends.txt", 'r', encoding='UTF-8')
    # 通过readlines（）方法读取文件的每一行赋值给lines
    lines = file.readlines()[1:]
    # 如果lines为真，执行循环的内容
    if lines:
        for line in lines:  # lines是一个列表，列表中的每隔元素就是txt文件中的一行数据
            print(line)  # 这一步是为了验证是否能如期获取到列表
            line = line.strip('\n').split(',')  # strip（）去掉字符串头尾的符号，通过","将每行数据拆分
            a = line[0]
            b = line[1]
            sql = "insert into friends values(%s,%s)"  # 数据库数据插入语句
            param = (a, b)  # param参数是要输入的数据
            cursor.execute(sql, param)  # cursor.execute(sql,param)方法执行插入语句
    conn.commit()  # 提交
    file.close()  # 关闭所有的连接
    cursor.close()
    conn.close()