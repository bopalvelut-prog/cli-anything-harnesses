from setuptools import setup
setup(
    name='cli-anything-android',
    version='1.0.0',
    packages=['cli_anything.android'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-android=cli_anything.android:cli']},
)
