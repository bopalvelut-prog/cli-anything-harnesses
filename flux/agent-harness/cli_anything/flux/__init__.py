import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Flux generate')
@cli.command()
def models(): click.echo('Flux models')
if __name__ == '__main__': cli()
