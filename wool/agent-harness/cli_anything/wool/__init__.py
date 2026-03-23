import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wool running')
@cli.command()
def start(): click.echo('wool started')
if __name__ == '__main__': cli()
