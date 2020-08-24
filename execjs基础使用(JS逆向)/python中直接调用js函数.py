import execjs


def addition(data1, data2):
    js = '''
        function add(a, b) {
            result = a + b;
            return result
        }
    '''
    # 编译JS
    resp = execjs.compile(js)
    # 调用js函数
    a = resp.call('add', data1, data2)
    return a
