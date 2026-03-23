import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('panic running')
@cli.command()
def start(): click.echo('panic started')
if __name__ == '__main__': cli()
