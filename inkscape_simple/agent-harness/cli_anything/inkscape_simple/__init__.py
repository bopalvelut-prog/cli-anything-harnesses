
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('svg')
@click.argument('output')
@click.option('-f', '--format', default='png')
def export(svg, output, format):
    subprocess.run(['inkscape', svg, '--export-filename', output, '--export-type', format])
    click.echo(f'Exported: {output}')
@cli.command()
@click.argument('svg')
def info(svg): click.echo(f'SVG: {svg}')
if __name__ == '__main__': cli()
