import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weed running')
@cli.command()
def start(): click.echo('weed started')
if __name__ == '__main__': cli()
