import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pkg running')
@cli.command()
def start(): click.echo('pkg started')
if __name__ == '__main__': cli()
