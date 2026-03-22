from setuptools import setup
setup(
    name='cli-anything-kali',
    version='1.0.0',
    packages=['cli_anything.kali'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kali=cli_anything.kali:cli']},
)
