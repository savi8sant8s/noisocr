from setuptools import setup, find_packages

setup(
    name='noisocr',
    version='0.2',
    description='Tools to simulate post-OCR noisy texts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sávio Santos',
    author_email='savi8sant8s@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'typo',
        'PyHyphen',
    ],
)