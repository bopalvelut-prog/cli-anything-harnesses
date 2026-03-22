
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('kra_file')
def info(kra_file):
    click.echo(f'Krita file: {kra_file}')

@cli.command()
@click.argument('input')
@click.argument('output')
def export_svg(input, output):
    click.echo(f'Exporting {input} to {output}')

if __name__ == '__main__':
    cli()
