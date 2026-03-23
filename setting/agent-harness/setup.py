from setuptools import setup
setup(
    name='cli-anything-setting',
    version='1.0.0',
    packages=['cli_anything.setting'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-setting=cli_anything.setting:cli']},
)
