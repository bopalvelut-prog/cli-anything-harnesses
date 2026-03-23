from setuptools import setup
setup(
    name='cli-anything-app_1545',
    version='1.0.0',
    packages=['cli_anything.app_1545'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_1545=cli_anything.app_1545:cli']},
)
