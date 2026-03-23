from setuptools import setup
setup(
    name='cli-anything-shall',
    version='1.0.0',
    packages=['cli_anything.shall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shall=cli_anything.shall:cli']},
)
