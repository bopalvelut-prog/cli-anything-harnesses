import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('knockout running')
@cli.command()
def start(): click.echo('knockout started')
if __name__ == '__main__': cli()
