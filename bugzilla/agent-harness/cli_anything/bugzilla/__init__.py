import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bugzilla running')
@cli.command()
def start(): click.echo('bugzilla started')
if __name__ == '__main__': cli()
