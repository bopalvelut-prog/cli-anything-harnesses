from setuptools import setup
setup(
    name='cli-anything-tawk_to',
    version='1.0.0',
    packages=['cli_anything.tawk_to'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tawk_to=cli_anything.tawk_to:cli']},
)
