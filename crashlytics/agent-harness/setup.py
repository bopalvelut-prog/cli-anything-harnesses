from setuptools import setup
setup(
    name='cli-anything-crashlytics',
    version='1.0.0',
    packages=['cli_anything.crashlytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crashlytics=cli_anything.crashlytics:cli']},
)
