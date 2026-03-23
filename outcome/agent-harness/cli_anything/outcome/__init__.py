import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('outcome running')
@cli.command()
def start(): click.echo('outcome started')
if __name__ == '__main__': cli()
