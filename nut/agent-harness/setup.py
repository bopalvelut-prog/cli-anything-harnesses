from setuptools import setup
setup(
    name='cli-anything-nut',
    version='1.0.0',
    packages=['cli_anything.nut'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nut=cli_anything.nut:cli']},
)
