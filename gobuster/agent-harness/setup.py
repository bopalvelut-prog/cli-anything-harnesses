from setuptools import setup
setup(
    name='cli-anything-gobuster',
    version='1.0.0',
    packages=['cli_anything.gobuster'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gobuster=cli_anything.gobuster:cli']},
)
