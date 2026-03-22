from setuptools import setup
setup(
    name='cli-anything-nextcloud',
    version='1.0.0',
    packages=['cli_anything.nextcloud'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-nextcloud=cli_anything.nextcloud:cli']},
)
