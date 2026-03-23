import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assurance running')
@cli.command()
def start(): click.echo('assurance started')
if __name__ == '__main__': cli()
