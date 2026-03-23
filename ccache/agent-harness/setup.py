from setuptools import setup
setup(
    name='cli-anything-ccache',
    version='1.0.0',
    packages=['cli_anything.ccache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ccache=cli_anything.ccache:cli']},
)
