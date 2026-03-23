import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thick running')
@cli.command()
def start(): click.echo('thick started')
if __name__ == '__main__': cli()
