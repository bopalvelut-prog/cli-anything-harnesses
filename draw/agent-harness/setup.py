from setuptools import setup
setup(
    name='cli-anything-draw',
    version='1.0.0',
    packages=['cli_anything.draw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-draw=cli_anything.draw:cli']},
)
