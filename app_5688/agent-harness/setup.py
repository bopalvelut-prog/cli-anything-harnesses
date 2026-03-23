from setuptools import setup
setup(
    name='cli-anything-app_5688',
    version='1.0.0',
    packages=['cli_anything.app_5688'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5688=cli_anything.app_5688:cli']},
)
