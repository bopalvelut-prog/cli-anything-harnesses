import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('differ running')
@cli.command()
def start(): click.echo('differ started')
if __name__ == '__main__': cli()
