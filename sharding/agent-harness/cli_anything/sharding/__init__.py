import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sharding running')
@cli.command()
def start(): click.echo('sharding started')
if __name__ == '__main__': cli()
