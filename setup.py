import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='wingpy',
    version='0.1.0',
    author='Brennen Herbruck',
    author_email='brennen.herbruck@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bherbruck/wingpy',
    packages=['wingpy'],
    python_requires='>=3.6',
)
