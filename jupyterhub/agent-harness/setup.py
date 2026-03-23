from setuptools import setup
setup(
    name='cli-anything-jupyterhub',
    version='1.0.0',
    packages=['cli_anything.jupyterhub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jupyterhub=cli_anything.jupyterhub:cli']},
)
