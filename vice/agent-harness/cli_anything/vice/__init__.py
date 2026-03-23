import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vice running')
@cli.command()
def start(): click.echo('vice started')
if __name__ == '__main__': cli()
