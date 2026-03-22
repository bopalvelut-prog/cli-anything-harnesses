
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('pdf')
@click.argument('output')
@click.option('-d', '--dpi', default=150)
def pdf_to_images(pdf, output, dpi):
    subprocess.run(['gs', '-dNOPAUSE', '-dBATCH', '-sDEVICE=png16m', f'-r{dpi}', f'-sOutputFile={output}', pdf])
    click.echo(f'Converted: {output}')
if __name__ == '__main__': cli()
