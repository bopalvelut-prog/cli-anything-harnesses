import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tomorrow running')
@cli.command()
def start(): click.echo('tomorrow started')
if __name__ == '__main__': cli()
