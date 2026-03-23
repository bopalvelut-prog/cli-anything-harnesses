from setuptools import setup
setup(
    name='cli-anything-remind',
    version='1.0.0',
    packages=['cli_anything.remind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remind=cli_anything.remind:cli']},
)
