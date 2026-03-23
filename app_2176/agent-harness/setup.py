from setuptools import setup
setup(
    name='cli-anything-app_2176',
    version='1.0.0',
    packages=['cli_anything.app_2176'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2176=cli_anything.app_2176:cli']},
)
