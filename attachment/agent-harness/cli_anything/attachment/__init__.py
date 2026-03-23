import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('attachment running')
@cli.command()
def start(): click.echo('attachment started')
if __name__ == '__main__': cli()
