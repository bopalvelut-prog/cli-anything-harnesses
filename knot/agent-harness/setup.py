from setuptools import setup
setup(
    name='cli-anything-knot',
    version='1.0.0',
    packages=['cli_anything.knot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knot=cli_anything.knot:cli']},
)
