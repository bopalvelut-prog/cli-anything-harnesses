from setuptools import setup
setup(
    name='cli-anything-ultralytics',
    version='1.0.0',
    packages=['cli_anything.ultralytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ultralytics=cli_anything.ultralytics:cli']},
)
