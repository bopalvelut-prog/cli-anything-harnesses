from setuptools import setup
setup(
    name='cli-anything-look',
    version='1.0.0',
    packages=['cli_anything.look'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-look=cli_anything.look:cli']},
)
