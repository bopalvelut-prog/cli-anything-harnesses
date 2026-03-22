
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('--macro')
def process(input, output, macro):
    click.echo(f'Processing {input} -> {output}')

@cli.command()
def plugins():
    click.echo('Bioformats, Stitching, Trainable Weka')

if __name__ == '__main__':
    cli()
