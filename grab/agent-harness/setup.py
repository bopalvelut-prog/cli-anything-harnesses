from setuptools import setup
setup(
    name='cli-anything-grab',
    version='1.0.0',
    packages=['cli_anything.grab'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grab=cli_anything.grab:cli']},
)
