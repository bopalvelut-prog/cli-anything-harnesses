import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amigo running')
@cli.command()
def start(): click.echo('amigo started')
if __name__ == '__main__': cli()
