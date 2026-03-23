from setuptools import setup
setup(
    name='cli-anything-fill',
    version='1.0.0',
    packages=['cli_anything.fill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fill=cli_anything.fill:cli']},
)
