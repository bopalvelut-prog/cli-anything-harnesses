import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('urge running')
@cli.command()
def start(): click.echo('urge started')
if __name__ == '__main__': cli()
