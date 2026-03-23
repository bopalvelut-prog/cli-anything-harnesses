from setuptools import setup
setup(
    name='cli-anything-real_app_5053',
    version='1.0.0',
    packages=['cli_anything.real_app_5053'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_5053=cli_anything.real_app_5053:cli']},
)
