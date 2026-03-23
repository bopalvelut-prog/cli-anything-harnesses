import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shed running')
@cli.command()
def start(): click.echo('shed started')
if __name__ == '__main__': cli()
