import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
def convert(input, output): subprocess.run(['asciidoctor', '-o', output, input])
@cli.command()
def serve(): subprocess.run(['asciidoctor', '-a', 'stylesheet=default.css', 'index.adoc'])
if __name__ == '__main__': cli()
