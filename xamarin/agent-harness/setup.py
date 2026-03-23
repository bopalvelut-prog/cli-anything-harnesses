from setuptools import setup
setup(
    name='cli-anything-xamarin',
    version='1.0.0',
    packages=['cli_anything.xamarin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xamarin=cli_anything.xamarin:cli']},
)
