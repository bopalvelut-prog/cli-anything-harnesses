from setuptools import setup
setup(
    name='cli-anything-snow',
    version='1.0.0',
    packages=['cli_anything.snow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snow=cli_anything.snow:cli']},
)
