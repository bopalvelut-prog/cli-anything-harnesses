from setuptools import setup
setup(
    name='cli-anything-destroy',
    version='1.0.0',
    packages=['cli_anything.destroy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-destroy=cli_anything.destroy:cli']},
)
