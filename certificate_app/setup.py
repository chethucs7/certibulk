"""Package setup configuration."""
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='certificate-sender',
    version='1.0.0',
    author='Your Company',
    author_email='dev@example.com',
    description='Production-grade Flask application for certificate distribution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourcompany/certificate-app',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Flask>=3.0.0',
        'Flask-SQLAlchemy>=3.0.0',
        'Flask-CORS>=3.0.0',
        'Flask-Mail>=0.10.0',
        'pandas>=2.0.0',
        'openpyxl>=3.0.0',
        'mysql-connector-python>=8.0.0',
        'python-dotenv>=0.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'pytest-flask>=1.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
            'pylint>=2.10.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'certificate-app=run:main',
        ],
    },
    include_package_data=True,
)
