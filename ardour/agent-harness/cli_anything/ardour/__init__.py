
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('session_path')
def start(session_path):
    click.echo(f'Starting Ardour session: {session_path}')

@cli.command()
@click.argument('session')
def export(session):
    click.echo(f'Exporting session: {session}')

if __name__ == '__main__':
    cli()
