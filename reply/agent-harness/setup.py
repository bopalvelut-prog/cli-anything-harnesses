from setuptools import setup
setup(
    name='cli-anything-reply',
    version='1.0.0',
    packages=['cli_anything.reply'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reply=cli_anything.reply:cli']},
)
