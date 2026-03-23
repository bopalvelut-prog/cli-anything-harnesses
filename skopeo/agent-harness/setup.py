from setuptools import setup
setup(
    name='cli-anything-skopeo',
    version='1.0.0',
    packages=['cli_anything.skopeo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skopeo=cli_anything.skopeo:cli']},
)
