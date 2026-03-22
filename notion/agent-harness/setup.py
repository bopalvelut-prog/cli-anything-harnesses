from setuptools import setup
setup(
    name='cli-anything-notion',
    version='1.0.0',
    packages=['cli_anything.notion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-notion=cli_anything.notion:cli']},
)
