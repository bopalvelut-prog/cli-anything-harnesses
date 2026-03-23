from setuptools import setup
setup(
    name='cli-anything-personality',
    version='1.0.0',
    packages=['cli_anything.personality'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-personality=cli_anything.personality:cli']},
)
