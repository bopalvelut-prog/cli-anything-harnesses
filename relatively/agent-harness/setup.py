from setuptools import setup
setup(
    name='cli-anything-relatively',
    version='1.0.0',
    packages=['cli_anything.relatively'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relatively=cli_anything.relatively:cli']},
)
