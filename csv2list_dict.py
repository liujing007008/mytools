import csv
import xlrd


class ReaderFile:
    """
        读取csv文件
        filePath:文件路径
    """

    def getCsvValue(self, filepath):
        # 用于存放返回dict的list
        dict_list = []
        # 打开指定路径的文件
        with open(filepath) as f:
            # 读取csv文件
            datareader = csv.reader(f)
            # 读取的csv文件内容转换成list
            csv_list = list(datareader)
            # 获取csv的第一列为dict的key值
            key_list = csv_list[0]
            # 将csv取出的数据处理成dict形式
            for value in range(1, len(csv_list)):
                # dict必须声明在此位置,后面的dictList.append()时里面的dict是不同的对象,若声明全局变量,那dictList中的dict的指针全是指向同一个对象,值完全一致
                csv_dict = {}
                for item in range(0, len(key_list)):
                    # 向dict中添加key和value
                    csv_dict[key_list[item]] = csv_list[value][item]
                # 将处理完成的dict追加到dictList中
                dict_list.append(csv_dict)
        return dict_list

    """
        读取excel文件
        filePath:文件路径
        sheetName:要读取的sheet工作表的名称
    """

    def getExcelValue(self, filepath, sheetname):
        # 用于存放获取封装的dict的list
        all_list = []
        # 读取excel文件
        workbook = xlrd.open_workbook(filepath)
        # 根据sheet名称读取sheet内容
        sheet_book = workbook.sheet_by_name(sheetname)
        # 获取第一行的内容作为key
        keylist = sheet_book.row_values(0)
        # 对第二行及之后的内容进行遍历,与keyList组合并封装成dict
        for value in range(1, sheet_book.nrows):
            list_dict = {}
            for key in range(0, len(keylist)):
                list_dict[keylist[key]] = sheet_book.row_values(value)[key]
            all_list.append(list_dict)
        return all_list


if __name__ == "__main__":
    file = ReaderFile()
    li = file.getCsvValue('2019.csv')
    print(type(li[0]))
