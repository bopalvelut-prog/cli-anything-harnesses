import click
@click.group()
def cli(): pass
@cli.command()
def convert(): click.echo('TFLite convert')
@cli.command()
def benchmark(): click.echo('TFLite benchmark')
if __name__ == '__main__': cli()
