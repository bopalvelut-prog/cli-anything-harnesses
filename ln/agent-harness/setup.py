from setuptools import setup
setup(
    name='cli-anything-ln',
    version='1.0.0',
    packages=['cli_anything.ln'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ln=cli_anything.ln:cli']},
)
