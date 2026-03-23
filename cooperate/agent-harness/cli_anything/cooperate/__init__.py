import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cooperate running')
@cli.command()
def start(): click.echo('cooperate started')
if __name__ == '__main__': cli()
