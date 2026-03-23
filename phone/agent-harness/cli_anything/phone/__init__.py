import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phone running')
@cli.command()
def start(): click.echo('phone started')
if __name__ == '__main__': cli()
