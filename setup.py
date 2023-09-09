from setuptools import setup, find_packages

setup(
    name='compactletterdisplay',
    version='0.11',
    packages=find_packages(),
    url='https://github.com/sujeet-bhalerao/compact-letter-display',
    author='Sujeet Bhalerao',
    author_email='sujeetbhalerao@gmail.com',
    description='A compact letter display implementation in Python, which summarizes results of posthoc comparisons.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
        'scipy',
        'statsmodels',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',  
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)