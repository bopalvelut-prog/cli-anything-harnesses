import click
@click.group()
def cli(): pass
@cli.command()
def quantize(): click.echo('BitsAndBytes quantize')
@cli.command()
def benchmark(): click.echo('BitsAndBytes benchmark')
if __name__ == '__main__': cli()
