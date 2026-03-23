import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minister running')
@cli.command()
def start(): click.echo('minister started')
if __name__ == '__main__': cli()
