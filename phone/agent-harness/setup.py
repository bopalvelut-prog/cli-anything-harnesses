from setuptools import setup
setup(
    name='cli-anything-phone',
    version='1.0.0',
    packages=['cli_anything.phone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phone=cli_anything.phone:cli']},
)
