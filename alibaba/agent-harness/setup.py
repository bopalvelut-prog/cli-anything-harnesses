from setuptools import setup
setup(
    name='cli-anything-alibaba',
    version='1.0.0',
    packages=['cli_anything.alibaba'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alibaba=cli_anything.alibaba:cli']},
)
