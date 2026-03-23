import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Stability AI generate')
@cli.command()
def models(): click.echo('Stability AI models')
if __name__ == '__main__': cli()
