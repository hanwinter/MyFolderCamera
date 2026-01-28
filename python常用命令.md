创建Python虚拟环境  python -m venv myenv
激活虚拟机 .\camera\Scripts\Activate
-----------------------------------------------------------------
在激活时提示“无法加载文件因为在此系统上禁止运行脚本”  使用以下命令
-------------------
检查当前的执行策略，命令：
Get-ExecutionPolicy。
如果返回 Restricted 或 AllSigned 说明不允许脚本执行。

可以临时修改执行策略，允许当前会话运行脚本。运行以下命令：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
这个命令将仅在当前 PowerShell 会话中允许执行签名脚本和本地脚本，不会改变系统的全局设置。

如果你希望永久允许脚本执行，可以运行以下命令，将执行策略更改为 RemoteSigned 或 Unrestricted(不推荐完全解除限制)：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
这样做会在当前用户的范围内永久允许执行本地脚本和来自可信源的远程脚本
------------------------------------------------------------
py支持中字符么：Python 完全支持中文字符，而且支持得非常好。
一、Python 对中文的支持范围
变量、函数名可以写中文
名字 = "韩枫"
def 打印名字():
    print(名字)
字符串当然可以是中文
msg = "合并照片集合"
print(msg)
文件内容读写中文没问题
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write("韩姓照片清单")
中文路径、中文文件名可以正常使用
folder = r"D:\图片\家庭照片"
print(os.listdir(folder))
Python 内部使用 Unicode，能包含所有语言字符。
-----------------------------------------------------

CMD: 在 Windows 系统里，CMD = Command Prompt（命令提示符）
CMD 是 Windows 自带的命令行接口，允许用户通过键盘输入指令来操作电脑，而不是只靠鼠标点来点去。
它属于：Shell（命令解释器）,用来执行命令、运行程序、管理文件系统等.
Windows 有两个类似的终端：
CMD（cmd.exe）              	历史最久，功能基础，兼容旧系统
PowerShell（powershell.exe）	功能强大，支持脚本、对象处理，更现代