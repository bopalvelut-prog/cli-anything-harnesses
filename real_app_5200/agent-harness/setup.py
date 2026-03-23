from setuptools import setup
setup(
    name='cli-anything-real_app_5200',
    version='1.0.0',
    packages=['cli_anything.real_app_5200'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_5200=cli_anything.real_app_5200:cli']},
)
