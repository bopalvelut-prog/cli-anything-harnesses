from setuptools import setup
setup(
    name='cli-anything-unicorn',
    version='1.0.0',
    packages=['cli_anything.unicorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unicorn=cli_anything.unicorn:cli']},
)
