from setuptools import setup, find_packages

__VERSION__ = '2.0.11'

setup(
    name='ak-vendor',
    version=__VERSION__,
    description="Some vendor scripts that we use here at Appknox",
    long_description="All the Vendor/helper files the Appknox relies on",
    url='https://github.com/appknox/vendor',
    author='appknox',
    author_email='engineering@appknox.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='appknox vendor',
    packages=find_packages(),
    data_files=[
        ('excel', ['ak_vendor/translations/ja/vulnerability.xlsx']),
        ('report', [
            'ak_vendor/report/report_template.html',
        ]),
        ('translations', ['ak_vendor/locale/ja/LC_MESSAGES/django.po']),
    ],
    include_package_data=True,
    entry_points='',
    install_requires=[
        'orm-choices==0.3.0',
        'maya>=0.6.0',
        'html2text==2019.8.11',
        'attrs>=19.0.0',
        'cvss>=2.0',
    ],
    zip_safe=False,
    extras_require={
        'dev': [
            'django==3.0',
            'weasyprint==50',
            'bumpversion==0.5.3',
            'twine==3.1.1',
        ],
        'test': [''],
    },
)
