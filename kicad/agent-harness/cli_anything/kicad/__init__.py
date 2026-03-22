
import click, subprocess, os

@click.group()
def cli(): pass

@cli.command()
@click.argument('kicad_pro')
def pcbnew(kicad_pro):
    click.echo(f'Opening PCB in Pcbnew: {kicad_pro}')

@cli.command()
@click.argument('kicad_pro')
def eeschema(kicad_pro):
    click.echo(f'Opening schematic in Eeschema: {kicad_pro}')

@cli.command()
@click.argument('kicad_pro')
def export_gerbers(kicad_pro):
    click.echo(f'Exporting gerbers for: {kicad_pro}')

if __name__ == '__main__':
    cli()
