import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('humor running')
@cli.command()
def start(): click.echo('humor started')
if __name__ == '__main__': cli()
