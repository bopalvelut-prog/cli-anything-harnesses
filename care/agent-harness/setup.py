from setuptools import setup
setup(
    name='cli-anything-care',
    version='1.0.0',
    packages=['cli_anything.care'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-care=cli_anything.care:cli']},
)
