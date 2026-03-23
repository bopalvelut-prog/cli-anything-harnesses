from setuptools import setup
setup(
    name='cli-anything-ten',
    version='1.0.0',
    packages=['cli_anything.ten'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ten=cli_anything.ten:cli']},
)
