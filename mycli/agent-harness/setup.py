from setuptools import setup
setup(
    name='cli-anything-mycli',
    version='1.0.0',
    packages=['cli_anything.mycli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mycli=cli_anything.mycli:cli']},
)
