## 注意事项

- 测速及解锁测试仅供参考，不代表实际使用情况，由于网络情况变化、Netflix封锁及ip更换，测速具有时效性
- 本项目使用 [Python](https://www.python.org/) 编写，使用前请完成环境安装
- 首次运行前请安装pip及相关依赖，也可使用 `pip install -r requirements.txt` 命令自行安装
- Netflix 解锁测速结果说明:

~~~~text
Full Unlock             全解锁
Only original           仅解锁自制剧
None                    未解锁
~~~~

## 特性

- 使用 clash-core，原生支持 Shadowsocks，Trojan，V2Ray
- 支持普通/快速测试，可以反映解锁状态（快速测试只检查全解锁，其他状态为无解锁）
- 支持 Netflix 解锁测试，分为 全解锁 / 仅解锁自制剧 / 无解锁 三档
- 可上传 Gist 方便后续使用

## 相关依赖

Python第三方库 见 `requirements.txt`

## 支持平台

### 已测试平台

1. Windows 10 x64
2. Debian 10 x64
3. Ubuntu 20 x64

## 致谢

- [Dreamacro](https://github.com/Dreamacro/clash)
- [PauperZ](https://github.com/PauperZ/SSRSpeedN)

## 使用说明

1. 配置文件说明

~~~~json
{
  "localAddress": "127.0.0.1",
  //clash的监听地址
  "mixPort": 7890,
  //clash的代理端口
  "controlPort": 9090,
  //clash的api端口
  "fastMode": true,
  //快速模式，只测试全解锁
  "converterAPI": "https://subcon.dlj.tf",
  //subconverter 服务器地址
  "subURL": "",
  //订阅地址
  "include": "",
  //节点包含关键字，支持正则
  "exclude": "IPV6|本站|剩余|过期|用户|官网",
  //排除节点关键字，支持正则
  "localFile": true,
  //true为导出到 list.yaml 文件，false为上传到Gist。若上传Gist，需申请github的token
  "token": ""
  //github token
}
~~~~

2. 安装第三方库:

~~~~bash
pip install -r requirements.txt
~~~~

3. 运行程序：

~~~~bash
python3 ./main.py
~~~~

4. 命令参数：

~~~~bash
usage: main.py [-h] [-u SUBURL] [-t TOKEN] [-g GISTURL]

optional arguments:
  -h, --help            show this help message and exit
  -u SUBURL, --url SUBURL
                        Load config from subscription url
  -t TOKEN, --token TOKEN
                        The github token
  -g GISTURL, --gist GISTURL
                        The gist api URL

~~~~