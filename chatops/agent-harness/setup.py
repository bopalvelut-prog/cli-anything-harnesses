from setuptools import setup
setup(
    name='cli-anything-chatops',
    version='1.0.0',
    packages=['cli_anything.chatops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chatops=cli_anything.chatops:cli']},
)
