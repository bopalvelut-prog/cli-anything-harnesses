import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tensor running')
@cli.command()
def start(): click.echo('tensor started')
if __name__ == '__main__': cli()
