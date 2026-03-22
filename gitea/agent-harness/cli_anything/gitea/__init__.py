
import click, requests, json, os

API = os.getenv('GITEA_URL', 'http://localhost:3000')
TOKEN = os.getenv('GITEA_TOKEN', '')

@click.group()
def cli(): pass

def headers():
    return {'Authorization': f'token {TOKEN}'} if TOKEN else {}

@cli.command()
def repos():
    r = requests.get(f'{API}/api/v1/user/repos', headers=headers())
    repos = r.json()
    for repo in repos:
        click.echo(f"{repo['name']} ({repo['html_url']})")

@cli.command()
@click.argument('name')
@click.option('--desc', default='')
def create(name, desc):
    data = {'name': name, 'description': desc, 'private': False}
    r = requests.post(f'{API}/api/v1/user/repos', json=data, headers=headers())
    if r.status_code == 201:
        click.echo(f'Created: {name}')
    else:
        click.echo(f'Error: {r.text}')

@cli.command()
def user():
    r = requests.get(f'{API}/api/v1/user', headers=headers())
    user = r.json()
    click.echo(f"User: {user.get('login', 'anonymous')}")

if __name__ == '__main__':
    cli()
