
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('tex_file')
@click.option('-o', '--output-dir', default='.')
def compile(tex_file, output_dir):
    subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory', output_dir, tex_file])
    click.echo('Compiled')
if __name__ == '__main__': cli()
