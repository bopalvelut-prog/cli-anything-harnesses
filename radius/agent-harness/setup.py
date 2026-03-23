from setuptools import setup
setup(
    name='cli-anything-radius',
    version='1.0.0',
    packages=['cli_anything.radius'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radius=cli_anything.radius:cli']},
)
