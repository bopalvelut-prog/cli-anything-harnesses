from setuptools import setup
setup(
    name='cli-anything-nghttp2',
    version='1.0.0',
    packages=['cli_anything.nghttp2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nghttp2=cli_anything.nghttp2:cli']},
)
