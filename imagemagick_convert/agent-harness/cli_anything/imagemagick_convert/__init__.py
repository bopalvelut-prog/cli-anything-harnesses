
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
def convert(input, output): subprocess.run(['convert', input, output]); click.echo(f'Converted: {output}')
@cli.command()
@click.argument('images', nargs=-1)
@click.argument('output')
def montage(images, output): subprocess.run(['montage'] + list(images) + [output]); click.echo(f'Montage: {output}')
if __name__ == '__main__': cli()
