from setuptools import setup
setup(
    name='cli-anything-peft',
    version='1.0.0',
    packages=['cli_anything.peft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peft=cli_anything.peft:cli']},
)
