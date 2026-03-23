import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('skuber running')
@cli.command()
def start(): click.echo('skuber started')
if __name__ == '__main__': cli()
