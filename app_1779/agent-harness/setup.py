from setuptools import setup
setup(
    name='cli-anything-app_1779',
    version='1.0.0',
    packages=['cli_anything.app_1779'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_1779=cli_anything.app_1779:cli']},
)
