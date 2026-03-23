import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('commando running')
@cli.command()
def start(): click.echo('commando started')
if __name__ == '__main__': cli()
