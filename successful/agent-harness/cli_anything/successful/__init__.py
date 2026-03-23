import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('successful running')
@cli.command()
def start(): click.echo('successful started')
if __name__ == '__main__': cli()
