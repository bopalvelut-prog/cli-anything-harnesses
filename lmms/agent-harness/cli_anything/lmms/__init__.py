
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('project')
def export(project):
    click.echo(f'Exporting: {project}')

@cli.command()
def presets():
    click.echo('Kicker, Bass, sf2player')

if __name__ == '__main__':
    cli()
