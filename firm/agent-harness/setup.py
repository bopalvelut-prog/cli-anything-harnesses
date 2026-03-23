from setuptools import setup
setup(
    name='cli-anything-firm',
    version='1.0.0',
    packages=['cli_anything.firm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firm=cli_anything.firm:cli']},
)
