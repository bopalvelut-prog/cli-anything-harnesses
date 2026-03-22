
import click, subprocess

@click.group()
def cli(): pass

@cli.command()
@click.argument('sla_file')
def export_pdf(sla_file):
    click.echo(f'Exporting PDF: {sla_file}')

@cli.command()
@click.argument('sla_file')
def info(sla_file):
    click.echo(f'Scribus file: {sla_file}')

if __name__ == '__main__':
    cli()
