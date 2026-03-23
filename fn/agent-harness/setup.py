from setuptools import setup
setup(
    name='cli-anything-fn',
    version='1.0.0',
    packages=['cli_anything.fn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fn=cli_anything.fn:cli']},
)
