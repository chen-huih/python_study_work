import os


def dfs(path, width):
    local_path = os.listdir(path)
    for i in local_path:
        print(' '*width+i)
        if os.path.isdir(path + '/' + i):  # 如果是目录文件，递归调用
            dfs(path + '/' + i, width+4)


if __name__ == '__main__':
    dfs('.', 0)
    print(os.listdir("./dir1/dir1_1"))
