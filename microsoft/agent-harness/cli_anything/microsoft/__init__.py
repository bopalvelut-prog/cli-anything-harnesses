import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('microsoft running')
@cli.command()
def start(): click.echo('microsoft started')
if __name__ == '__main__': cli()
