from setuptools import setup
setup(
    name='cli-anything-phpfpm',
    version='1.0.0',
    packages=['cli_anything.phpfpm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phpfpm=cli_anything.phpfpm:cli']},
)
