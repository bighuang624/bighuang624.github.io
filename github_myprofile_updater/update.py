if __name__ == '__main__':
    _header = "### Hi there, I'm [Siteng Huang (黄思腾 in Chinese)](https://kyonhuang.top/)! 👋 You can also call me Kyon Huang."
    base_dir = '../_pages/includes/'
    _intro = open(f'{base_dir}/intro.md').read().strip()
    # _homepage = open(f'{base_dir}/homepage.md').read().strip()
    # _pub = open(f'{base_dir}/pub_short.md').read().strip()
    _news = open(f'{base_dir}/news.md').read().strip()
    with open('README.md', 'w') as f:
        # f.write(_header)
        # f.write('\n\n')
        f.write(_intro)
        f.write('\n\n')
        f.write('Please refer to my full paper list at [my personal homepage](https://kyonhuang.top/#-publications).')
        f.write('\n')
        f.write('<p align="center">'+'<a href="https://twitter.com/KyonHuang" target="_blank"><img src="https://img.shields.io/twitter/follow/KyonHuang.svg?style=social" alt="Twitter"></a> '+'<a href="https://github.com/bighuang624?tab=followers" target="_blank"><img src="https://img.shields.io/github/followers/bighuang624.svg?label=Follow%20@bighuang624&style=social" alt="GitHub"></a> '+'<a href="https://github.com/bighuang624" target="_blank"><img src="https://img.shields.io/github/stars/bighuang624.svg?style=social" alt="GitHub"></a>'+'</p>')
        f.write('\n\n##')
        # f.write(_homepage)
        # f.write('\n\n##')
        f.write(_news)
        # f.write('\n\n##')
        # f.write(_pub)