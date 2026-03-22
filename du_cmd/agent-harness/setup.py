from setuptools import setup
setup(
    name='cli-anything-du_cmd',
    version='1.0.0',
    packages=['cli_anything.du_cmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-du_cmd=cli_anything.du_cmd:cli']},
)
