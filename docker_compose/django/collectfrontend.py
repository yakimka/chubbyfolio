import os
import shutil


def collect_frontend():
    shutil.copytree('/app/frontend', '/app/public', dirs_exist_ok=True)
    envs = _get_app_envs()
    site_url = envs["VUE_APP_SITE_URL"]

    _replace_sitemap_url(site_url)
    _prepare_html(envs)


def _replace_sitemap_url(new_url, old_url='https://sitemap.url/'):
    new_url = f'{new_url.strip("/")}/'
    with open('/app/frontend/sitemap.xml', 'r') as r, open('/app/public/sitemap.xml', 'w') as w:
        sitemap = r.read()
        sitemap = sitemap.replace(old_url, new_url)
        w.write(sitemap)


def _get_app_envs():
    return {key: value for key, value in os.environ.items() if key.startswith('VUE_APP_')}


def _prepare_html(data: dict):
    with open('/app/frontend/index.html', 'r') as r, open('/app/public/index.html', 'w') as w:
        index = r.read()
        metas = []
        for key, value in data.items():
            index = index.replace(f'${key}', value)
            metas.append(f'<meta property="{key}" content="{value}">')

        metas = ''.join(metas)
        head_index = index.index("<head>") + len("<head>")
        w.write(f"{index[:head_index]}{metas}{index[head_index:]}")


if __name__ == '__main__':
    collect_frontend()
    print('Done')
