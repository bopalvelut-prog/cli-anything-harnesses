
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('--resize', default='800x600')
def resize(input, output, resize):
    subprocess.run(['convert', input, '-resize', resize, output]); click.echo(f'Resized: {output}')
@cli.command()
@click.argument('input')
def info(input): subprocess.run(['identify', input])
if __name__ == '__main__': cli()
