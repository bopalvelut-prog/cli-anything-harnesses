from setuptools import setup
setup(
    name='cli-anything-thelounge',
    version='1.0.0',
    packages=['cli_anything.thelounge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thelounge=cli_anything.thelounge:cli']},
)
