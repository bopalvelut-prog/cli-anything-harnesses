from setuptools import setup
setup(
    name='cli-anything-real_app_1180',
    version='1.0.0',
    packages=['cli_anything.real_app_1180'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_1180=cli_anything.real_app_1180:cli']},
)
