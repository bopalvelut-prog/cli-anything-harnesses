import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('have running')
@cli.command()
def start(): click.echo('have started')
if __name__ == '__main__': cli()
