import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hire running')
@cli.command()
def start(): click.echo('hire started')
if __name__ == '__main__': cli()
