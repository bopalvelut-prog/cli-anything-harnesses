from setuptools import setup
setup(
    name='cli-anything-ufw',
    version='1.0.0',
    packages=['cli_anything.ufw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ufw=cli_anything.ufw:cli']},
)
