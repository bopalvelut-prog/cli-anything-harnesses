from setuptools import setup
setup(
    name='cli-anything-app_5799',
    version='1.0.0',
    packages=['cli_anything.app_5799'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5799=cli_anything.app_5799:cli']},
)
