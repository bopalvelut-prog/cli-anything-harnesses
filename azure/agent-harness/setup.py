from setuptools import setup
setup(
    name='cli-anything-azure',
    version='1.0.0',
    packages=['cli_anything.azure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure=cli_anything.azure:cli']},
)
