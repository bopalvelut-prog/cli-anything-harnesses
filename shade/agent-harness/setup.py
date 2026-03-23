from setuptools import setup
setup(
    name='cli-anything-shade',
    version='1.0.0',
    packages=['cli_anything.shade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shade=cli_anything.shade:cli']},
)
