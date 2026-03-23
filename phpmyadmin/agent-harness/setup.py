from setuptools import setup
setup(
    name='cli-anything-phpmyadmin',
    version='1.0.0',
    packages=['cli_anything.phpmyadmin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phpmyadmin=cli_anything.phpmyadmin:cli']},
)
