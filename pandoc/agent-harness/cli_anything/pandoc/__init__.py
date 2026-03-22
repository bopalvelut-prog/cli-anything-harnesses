
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
@click.option('-f', '--from', 'fmt', default='markdown')
@click.option('-t', '--to', 'to_fmt', default='html')
def convert(input, output, fmt, to_fmt):
    subprocess.run(['pandoc', '-f', fmt, '-t', to_fmt, '-o', output, input])
    click.echo(f'Converted: {output}')
if __name__ == '__main__': cli()
