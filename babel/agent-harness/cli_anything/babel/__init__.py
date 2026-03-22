import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
def transpile(input, output): subprocess.run(['babel', input, '-o', output])
@cli.command()
def watch(): subprocess.run(['babel', '.', '-w'])
if __name__ == '__main__': cli()
