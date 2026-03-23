import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minor running')
@cli.command()
def start(): click.echo('minor started')
if __name__ == '__main__': cli()
