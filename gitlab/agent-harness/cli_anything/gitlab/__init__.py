
import click, requests, json, os
@click.group()
def cli(): pass
GL = os.getenv('GITLAB_URL', 'https://gitlab.com')
TOKEN = os.getenv('GITLAB_TOKEN', '')
@cli.command()
def projects():
    h = {'PRIVATE-TOKEN': TOKEN}
    r = requests.get(f'{GL}/api/v4/projects', headers=h, params={'membership': True})
    for p in r.json(): click.echo(f"{p['id']} {p['name']}")
@cli.command()
@click.argument('project_id')
def pipelines(project_id):
    h = {'PRIVATE-TOKEN': TOKEN}
    r = requests.get(f'{GL}/api/v4/projects/{project_id}/pipelines', headers=h)
    for p in r.json(): click.echo(f"{p['id']} {p['status']}")
if __name__ == '__main__': cli()
