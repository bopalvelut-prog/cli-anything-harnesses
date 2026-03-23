from setuptools import setup
setup(
    name='cli-anything-mybatis',
    version='1.0.0',
    packages=['cli_anything.mybatis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mybatis=cli_anything.mybatis:cli']},
)
