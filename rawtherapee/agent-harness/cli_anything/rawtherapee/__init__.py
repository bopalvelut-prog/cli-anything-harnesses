import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
def export(input, output): subprocess.run(['rawtherapee-cli', '-o', output, '-c', input])
@cli.command()
def profiles(): click.echo('Default, Portrait, Landscape')
if __name__ == '__main__': cli()
