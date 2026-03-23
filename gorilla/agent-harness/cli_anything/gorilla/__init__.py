import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gorilla running')
@cli.command()
def start(): click.echo('gorilla started')
if __name__ == '__main__': cli()
