from setuptools import setup
setup(
    name='cli-anything-yourself',
    version='1.0.0',
    packages=['cli_anything.yourself'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yourself=cli_anything.yourself:cli']},
)
