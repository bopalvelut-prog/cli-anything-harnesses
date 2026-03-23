from setuptools import setup
setup(
    name='cli-anything-stand',
    version='1.0.0',
    packages=['cli_anything.stand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stand=cli_anything.stand:cli']},
)
