import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('outlook running')
@cli.command()
def start(): click.echo('outlook started')
if __name__ == '__main__': cli()
