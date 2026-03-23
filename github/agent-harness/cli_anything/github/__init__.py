import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('github running')
@cli.command()
def start(): click.echo('github started')
if __name__ == '__main__': cli()
