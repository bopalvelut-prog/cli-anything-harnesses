from setuptools import setup
setup(
    name='cli-anything-real_app_5468',
    version='1.0.0',
    packages=['cli_anything.real_app_5468'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_5468=cli_anything.real_app_5468:cli']},
)
