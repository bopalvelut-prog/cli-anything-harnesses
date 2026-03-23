from setuptools import setup
setup(
    name='cli-anything-real_app_5401',
    version='1.0.0',
    packages=['cli_anything.real_app_5401'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_5401=cli_anything.real_app_5401:cli']},
)
