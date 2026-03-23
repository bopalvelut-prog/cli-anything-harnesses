from setuptools import setup
setup(
    name='cli-anything-zeabur',
    version='1.0.0',
    packages=['cli_anything.zeabur'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zeabur=cli_anything.zeabur:cli']},
)
