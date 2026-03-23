from setuptools import setup
setup(
    name='cli-anything-real_app_1194',
    version='1.0.0',
    packages=['cli_anything.real_app_1194'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_1194=cli_anything.real_app_1194:cli']},
)
