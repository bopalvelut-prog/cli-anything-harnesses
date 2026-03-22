
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('-f', '--from', 'fmt', default='epub')
@click.option('-t', '--to', 'to_fmt', default='mobi')
def convert(input, output, fmt, to_fmt):
    subprocess.run(['ebook-convert', input, output, '--input-format', fmt, '--output-format', to_fmt])
    click.echo(f'Converted: {output}')
@cli.command()
@click.argument('book')
def info(book): click.echo(f'Book: {book}')
if __name__ == '__main__': cli()
