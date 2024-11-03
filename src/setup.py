from setuptools import setup, find_packages

setup(
    name='mypackage',  # 包的名称
    version='0.1.0',  # 版本号
    packages=find_packages(),  # 自动找到包
    install_requires=open('requirements.txt').read().splitlines(),  # 依赖
    author='awser124',  # 作者名
    author_email='awser124@hotmail.com',  # 作者邮箱
    description='python StringFormatterPlus',  # 描述
    long_description=open('README.md').read(),  # 详细描述
    long_description_content_type='text/markdown',  # 描述类型
    url='https://github.com/awser124/StringFormatterPlus',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
