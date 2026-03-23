from setuptools import setup
setup(
    name='cli-anything-real_app_1216',
    version='1.0.0',
    packages=['cli_anything.real_app_1216'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_1216=cli_anything.real_app_1216:cli']},
)
