from setuptools import setup
setup(
    name='cli-anything-real_app_1069',
    version='1.0.0',
    packages=['cli_anything.real_app_1069'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_1069=cli_anything.real_app_1069:cli']},
)
