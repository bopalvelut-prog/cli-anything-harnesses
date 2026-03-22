
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('fcstd_file')
def open_file(fcstd_file):
    click.echo(f'Opening: {fcstd_file}')

@cli.command()
@click.argument('fcstd_file')
@click.argument('output')
def export_step(fcstd_file, output):
    click.echo(f'Exporting {fcstd_file} to STEP: {output}')

if __name__ == '__main__':
    cli()
