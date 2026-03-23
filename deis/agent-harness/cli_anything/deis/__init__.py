import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deis running')
@cli.command()
def start(): click.echo('deis started')
if __name__ == '__main__': cli()
