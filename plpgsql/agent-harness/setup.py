from setuptools import setup
setup(
    name='cli-anything-plpgsql',
    version='1.0.0',
    packages=['cli_anything.plpgsql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plpgsql=cli_anything.plpgsql:cli']},
)
