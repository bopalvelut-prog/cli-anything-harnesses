from setuptools import setup
setup(
    name='cli-anything-rage',
    version='1.0.0',
    packages=['cli_anything.rage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rage=cli_anything.rage:cli']},
)
