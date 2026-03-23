from setuptools import setup
setup(
    name='cli-anything-clinic',
    version='1.0.0',
    packages=['cli_anything.clinic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clinic=cli_anything.clinic:cli']},
)
