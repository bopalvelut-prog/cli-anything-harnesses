
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('input')
@click.argument('output')
def export_raw(input, output):
    cmd = ['darktable-cli', input, output]
    subprocess.run(cmd)
    click.echo(f'Exported: {output}')

@cli.command()
def presets():
    click.echo('neutral, baseline, Fuji Velvia, Agfacolor')

if __name__ == '__main__':
    cli()
