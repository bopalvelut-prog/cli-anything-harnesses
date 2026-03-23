from setuptools import setup
setup(
    name='cli-anything-summer',
    version='1.0.0',
    packages=['cli_anything.summer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-summer=cli_anything.summer:cli']},
)
