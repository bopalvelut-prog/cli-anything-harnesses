import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('next running')
@cli.command()
def start(): click.echo('next started')
if __name__ == '__main__': cli()
