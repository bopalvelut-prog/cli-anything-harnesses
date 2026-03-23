from setuptools import setup
setup(
    name='cli-anything-app_1742',
    version='1.0.0',
    packages=['cli_anything.app_1742'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_1742=cli_anything.app_1742:cli']},
)
